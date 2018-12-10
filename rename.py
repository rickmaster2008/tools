import os

for filename in os.listdir("./img"):
    new_file_name = filename.replace("-", "")
    os.rename("./img/" + filename, "./img/" + new_file_name)