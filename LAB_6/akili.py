import torch
import torch.nn as nn
import torch.optim as optim



class LSTMModel(nn.Module):

    def __init__(self,input_size,hidden_size,num_layers, output_size):
        super(LSTMModel,self).__init__()
        self.hidden_size = hidden_size
        self.num_layers = num_layers

        self.lstm = nn.LSTM(input_size,hidden_size,num_layers,batch_first=True) #la couche LSTM avec les paramètres spécifiés.
        self.fc = nn.Linear(hidden_size,output_size) # la couche entièrement connectée (linéaire) qui prend les états cachés de la dernière cellule LSTM et les convertit en sortie de taille output_size.

    def forward(self, x):
        h0 = torch.zeros(self.num_layers, x.size(0),self.hidden_size)  # etat  cachè(hidden)   a  0
        c0 = torch.zeros(self.num_layers,x.size(0),self.hidden_size)   # etat celulle  a  0


        out, _ = self.lstm
        out = self.fc(out[])

    return out

















def get_output_size(input_size, kernel_size, stride=1, padding=1) :
    return (input_size - kernel_size + 2 * padding) // stride + 1



input_size = 3
output_size = get_output_size(input_size, kernel_size=3)  # Conv1
output_size = get_output_size(output_size, kernel_size=3)  # Conv2
output_size = get_output_size(output_size, kernel_size=5)  # Conv3
output_size = get_output_size(output_size, kernel_size=5)  # Conv4

print(f"Output size after conv layers: {output_size}")