import pandas as pd
import matplotlib.pyplot as plt
import csv

with open('Pokedex_Ver_SV1.csv',newline='') as csvfile:
    pokedex = csv.reader(csvfile, dialect ='excel', quotechar='|')
    for row in pokedex:
        print(','.join(row))
    print(len(row))