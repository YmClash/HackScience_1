import torch
import torch.nn as nn
import torch.optim as optim

# on  class  une classe d'reseau
class LSMTModel(nn.Module):
    def __init__(self,input_size,hidden_size,num_layers,output_size):
        super(LSMTModel, self).__init__()
        self.hidden_size = hidden_size
        self.num_layers = num_layers

        self.lstm = nn.LSTM(input_size,hidden_size,num_layers,batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)


    def forward(self,x):
        h0 = torch.zeros(self.num_layers,x.size(0),self.hidden_size)
        c0 = torch.zeros(self.num_layers,x.size(0),self.hidden_size)


        out, _ = self.lstm(x, (h0, c0))
        out = self.fc(out[:, -1,:])
        return out


#donne    pour   l'eintrainement
x_train =  torch.randn(1000,10,5)
y_train = torch.randn(1000,1)
x_test = torch.randn(100,10,5)
y_test = torch.randn(100,1)
print(x_train)
print(y_train)

# on  initiliase le model


input_size = 5
hidden_size = 50
num_layers = 1
output_size = 1

bethowen = LSMTModel(input_size,hidden_size,num_layers,output_size)

perte = nn.MSELoss()
optimizer = optim.Adam(bethowen.parameters(), lr=0.001)



num_epoch = 50
batch_size = 32

for epoch in range(num_epoch):
    for i in range(0,len(x_train),batch_size):
        x_batch = x_train[i:i+batch_size]
        y_batch = y_train[i:i+batch_size]

        outputs=bethowen(x_batch)
        loss = perte(outputs,y_batch)


        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        print(f'epoch[{epoch+1}/{num_epoch}],  Loss: {loss.item():.4f}')




print(f'Fin du test ')