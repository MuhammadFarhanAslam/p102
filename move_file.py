import os
import shutil

from_dir = "C:/Users/farha/Downloads/"
to_dir = "C:/Users/farha/OneDrive/Desktop/doc_files/"
file_list = os.listdir(from_dir)

for file_name in file_list:
    name, extension = os.path.splitext(file_name)
    if extension == "":
        continue
    if extension.lower() in [".txt", ".doc", ".docx", ".pdf"]:
        path1 = os.path.join(from_dir, file_name)
        path2 = to_dir
        path3 = os.path.join(to_dir, file_name)

        if not os.path.exists(path2):
            os.makedirs(path2)
        print("Moving " + file_name)
        shutil.move(path1, path3)
