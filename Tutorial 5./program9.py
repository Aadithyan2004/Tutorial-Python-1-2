import os

current_directory = os.getcwd()
items = os.listdir(current_directory)

for item in items:
    print(item)