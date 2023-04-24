import os
import requests
from bs4 import BeautifulSoup


def Create_folders(base_path, folders):
    for folder in folders:
        folder_path = os.path.join(base_path, folder)
        os.makedirs(folder_path, exist_ok=True)
        subfolders = ['0', '1', '2', '3']
        for subfolder in subfolders :
            subfolder_path = os.path.join(folder_path, subfolder)
            os.makedirs(subfolder_path, exist_ok=True)

#comment  utilisé la fonction Create Folder
#  base_path = r'C:\Users\y_mc\Desktop\AI\Ajuna\ASSET'
# folders = ['Layer0', 'Layer1', 'Layer2', 'Layer3']

# create_folders(base_path, folders)


# Scrapper

def Scraper():
    url = str
    destination_folder = str
    response = requests.get(url)
    if response.status_code == 200:
        filename = url.split("/")[-1]
        with open(destination_folder + filename,"wb") as f :
            f.write(response.content)
            print(f"Le fichier {filename} a été téléchargé avec succès dans {destination_folder}.")
    else :
        print("Erreur lors du telechargemet du fichier ")





#
#
# url = r'https://aaa.ajuna.io/components_/Layer10/0/AAAL10D220.webp'
#
# #destination_folder = r'C:\Users\y_mc\Desktop\AI\Ajuna\ASSET\Layer10
#
# response = requests.get(url)
#
# if response.status_code == 200 :
#
#     filename = url.split("/")[-1]
#
#     with open(destination_folder + filename, "wb") as f :
#         f.write(response.content)
#
#         print(f"Le fichier {filename} a été téléchargé avec succès dans {destination_folder}.")
# else :
#     print("Erreur lors du téléchargement du fichier.")
