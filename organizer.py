import os
import shutil

path = input("Enter folder path to organize: ")

file_types = {
    "Images": [".jpg", ".png", ".jpeg", ".gif"],
    "Documents": [".pdf", ".txt", ".docx"],
    "Audio": [".mp3", ".wav"],
    "Videos": [".mp4", ".mkv"]
}

for folder in file_types:
    if not os.path.exists(folder):
        os.makedirs(folder)

for file in os.listdir(path):
    file_path = os.path.join(path, file)
    if os.path.isfile(file_path):
        for folder, extensions in file_types.items():
            if file.lower().endswith(tuple(extensions)):
                shutil.move(file_path, os.path.join(folder, file))
                break

print("Files organized successfully!")
