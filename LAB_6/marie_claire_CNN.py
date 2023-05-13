import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
from torch.utils.data import DataLoader
import torchvision.datasets as datasets
import torchvision.transforms as transforms
import matplotlib.pyplot as plt


def main() :
    def tag() :
        print("Marie Claire Dev by Y_mC")
        if torch.cuda.is_available():
            print("Cuda")
        else :
            print("CPU")

    tag()

    # valeur   de  parametre du  reseau
    transform = transforms.Compose(
        [
            transforms.RandomHorizontalFlip(),
            transforms.RandomCrop(32, padding=4),
            transforms.ToTensor(),
            transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
        ])

    trainset = datasets.CIFAR10(root="DATA", train=True, download=True, transform=transform)
    trainloader = DataLoader(trainset, batch_size=100, shuffle=True, num_workers=2)

    testset = datasets.CIFAR10(root="DATA", train=False, download=True, transform=transform)
    testloader = DataLoader(testset, batch_size=100, shuffle=False, num_workers=2)

    class Net_Convo(nn.Module) :
        def __init__(self, num_filters_1, num_filters_2, num_filters_3, num_fc1, num_fc2, dropout_rate) :
            super(Net_Convo, self).__init__()

            self.conv1 = nn.Conv2d(3, num_filters_1, 3, padding=1)
            self.conv2 = nn.Conv2d(num_filters_1, num_filters_2, 3, padding=1)
            self.conv3 = nn.Conv2d(num_filters_2, num_filters_3, 3, padding=1)
            self.pool = nn.MaxPool2d(2, 2)

            self.fc1 = nn.Linear(num_filters_3 * 4 * 4, num_fc1)
            self.fc2 = nn.Linear(num_fc1, num_fc2)
            self.dropout = nn.Dropout(p=dropout_rate)

        def forward(self, x) :
            x = self.pool(F.relu(self.conv1(x)))
            x = self.pool(F.relu(self.conv2(x)))
            x = self.pool(F.relu(self.conv3(x)))
            x = x.view(-1, 128 * 4 * 4)
            x = F.relu(self.fc1(x))
            x = self.dropout(x)
            x = self.fc2(x)
            return x

    num_filters_1 = 32
    num_filters_2 = 64
    num_filters_3 = 128
    num_fc1 = 128
    num_fc2 = 10
    dropout_rate = 0.5

    marie_claire = Net_Convo(num_filters_1, num_filters_2, num_filters_3, num_fc1, num_fc2, dropout_rate)

    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(marie_claire.parameters(), lr=0.001)

    train_losses = []
    train_accuracies = []
    test_losses = []
    test_accuracies = []

    train_correct = 0
    train_total = 0

    num_epochs = 300

    for epoch in range(num_epochs) :
        train_loss = 0.0
        train_correct = 0
        train_total = 0

        marie_claire.train()
        for i, data in enumerate(trainloader, 0) :
            inputs, labels = data
            optimizer.zero_grad()
            outputs = marie_claire(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

            train_loss += loss.item()
            _, predicted = outputs.max(1)
            train_total += labels.size(0)
            train_correct += predicted.eq(labels).sum().item()

        train_accuracy = 100.0 * train_correct / train_total
        train_losses.append(train_loss)
        train_accuracies.append(train_accuracy)

        marie_claire.eval()
        test_loss = 0.0
        test_correct = 0
        test_total = 0

        with torch.no_grad() :
            for i, data in enumerate(testloader, 0) :
                inputs, labels = data
                outputs = marie_claire(inputs)
                loss = criterion(outputs, labels)

                test_loss += loss.item()
                _, predicted = outputs.max(1)
                test_total += labels.size(0)
                test_correct += predicted.eq(labels).sum().item()

        test_accurancy = 100.0 * test_correct / test_total
        test_losses.append(test_loss)
        test_accuracies.append(test_accurancy)

        print(f'Epoch{epoch + 1} /{num_epochs}, Train Loss: {train_loss:.2f}, Train Accuracy : {train_accuracy:.2f} ,Test Loss: {test_loss:.2f}, Test Accurancy: {test_accurancy}')

    print(f'Test Accurancy of the model on the test images: {100 * train_correct / train_total:.2f}%')

    torch.save(marie_claire.state_dict(), "Marie_Claire_model_1.pth")

    plt.figure(figsize=(12, 4))
    epochs = range(1, num_epochs + 1)

    # Tracer l'évolution de la perte (loss) au fil des époques
    plt.subplot(1, 2, 1)
    plt.plot(epochs, train_losses, label='Train')
    plt.plot(epochs, test_losses, label='Test')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.legend()
    plt.title('Loss vs. Epochs')

    # Tracer l'évolution de la précision (accuracy) au fil des époques
    plt.subplot(1, 2, 2)
    plt.plot(epochs, train_accuracies, label='Train')
    plt.plot(epochs, test_accuracies, label='Test')
    plt.xlabel('Epochs')
    plt.ylabel('Accuracy')
    plt.legend()
    plt.title('Accuracy vs. Epochs')

    plt.show()

    tag()


if __name__ == '__main__' :
    main()
