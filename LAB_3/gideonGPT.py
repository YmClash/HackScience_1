import numpy as np
import torchvision
import torch
import matplotlib.pyplot as plt
import logging
from minGPT.mingpt.utils import set_seed
from torch.utils.data import Dataset
from minGPT.mingpt.model import GPT


set_seed(42)


class ImageDataset(Dataset) :

    def __int__(self, pt_dataset) :
        self.pt_dataset = pt_dataset

        self.vocab_size = 256
        self.block_size = 28 * 28 - 1

    def __len__(self) :
        return len(self.pt_dataset)

    def __getitem__(self, idx) :
        x, y = self.pt_dataset[idx]
        x = torch.from_numpy(np.array(x)).view(-1)
        x = x.long()

        return x[:-1], x[1 :]


mconfig = GPT()

model =GPT(mconfig)

# defini  la configuration du logging
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    datefmt="%m/%d/%Y %H:%M:%S",
    level=logging.INFO,
)



root = './'



# on  telechargement   de  donnée  d'entrainement  et  de  test
train_data = torchvision.datasets.MNIST(root, train=True, transform=None, target_transform=None, download=True)
test_data = torchvision.datasets.MNIST(root, train=False, transform=None, target_transform=None, download=True)

print(len(train_data), len(test_data))

train_dataset = ImageDataset(train_data)
test_dataset = ImageDataset(test_data)
train_dataset[10][0].size()

# le setup des variable pour mes Array  a 2 dimensions

n_samples = 16
ncol = 8
nrow = n_samples // ncol + 1

plt.figure(figsize=(20, 10))

for i in range(n_samples) :
    #   encode  et  decodage dans  des  random data a l'aide   de  Array[]
    # on  encode les donnes  dans  2 variable  x,y

    x, y = train_data[np.random.randint(0, len(train_data))]
    xpt = torch.from_numpy(np.array(x)).float().view(28 * 28)

    # on plot/montre  les donné  de facon random
    plt.subplot(nrow, ncol, i + 1)
    plt.imshow(xpt.view(28, 28).numpy().astype(np.uint8))
    plt.axis('off')

plt.show()
