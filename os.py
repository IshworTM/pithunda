import os

# Get the current working directory
current_directory = os.getcwd()
print(current_directory)

# List files in a directory
files = os.listdir(current_directory)
print(files)
for folder, subfolders, files in os.walk(current_directory):
    for file in files:
        print(os.path.join(folder, file))
