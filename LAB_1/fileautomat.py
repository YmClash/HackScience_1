import os


def create_folders(base_path, folders,subfolders) :
    for folder in folders :
        folder_path = os.path.join(base_path, folder)
        os.makedirs(folder_path, exist_ok=True)
        for subfolder in subfolders:
            subfolder_path = os.path.join(folder_path, subfolder)
            os.makedirs(subfolder_path, exist_ok=True)


base_path = 'C:\Users\y_mc\Desktop\AI\Ajuna\ASSET'
folders = ['Layer0', 'Layer1', 'Layer2', 'Layer3']
subfolders = ['1', '2', '3']

create_folders(base_path, folders)
