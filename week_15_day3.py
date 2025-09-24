import os

fav_coute = input("Enter Your Favorite quote: ")
file_name = input("Enter the file name(file_name.txt) you wish to store your quote : ")

root, extension = os.path.splitext(file_name)
if extension != ".txt":
    print("Does not support this file extension!")
elif extension == ".txt":
    open(root, "x")
    with open(root, "a") as f:
        f.write(fav_coute)
    with open(root) as f:
        print(f.read())
else:
    pass