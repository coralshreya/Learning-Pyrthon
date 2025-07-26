print("hello")
import os

# Specify the directory (you can also use '.' for current directory)
directory_path = '/'  # or replace with any specific path like 'C:/Users/YourName/Documents'

# Get the list of files and directories
try:
    contents = os.listdir(directory_path)
    print(f"Contents of directory '{directory_path}':")
    for item in contents:
        print(item)
except FileNotFoundError:
    print(f"The directory '{directory_path}' was not found.")
except PermissionError:
    print(f"Permission denied to access '{directory_path}'.")
