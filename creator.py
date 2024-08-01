import os

# Read the contents of the file
with open('test.txt', 'r') as file:
    lines = file.readlines()

# Create folders
for line in lines:
    folder_name = line.strip()
    if folder_name:
        os.makedirs(folder_name, exist_ok=True)

print("Folders created successfully.")
