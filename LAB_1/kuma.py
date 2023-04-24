import matplotlib.pyplot as plt
import pandas as pd


# tableau = plt.figure(figsize=(10,10))


mugiwara_no_ichimi = ["Luffy ", "Zoro", "Nami", "usopp", "Sangi", "Chopper", "Robin", "Franky", "Brook", "Jimbe"]
age = [17, 19, 18, 17, 19, 15, 28, 34, 88, 44]
sexe = ["H", "H", "F", "H", "H", "H", "F", "H", "H", "H"]
taille = ["172 cm", "178 cm", "169 cm", "174 cm", "177 cm", "90 cm", "188 cm ", "225 cm", "266 cm", "301 cm "]

titre_colonnes = {"Nom" : mugiwara_no_ichimi,
                  "agee" : age,
                  "taille" : taille,
                  "sexe" : sexe}

data = pd.DataFrame(titre_colonnes)

select_column = data["Nom"][0]

print(data)
# print(select_column)

# tableau(data)

# tableau.show()



