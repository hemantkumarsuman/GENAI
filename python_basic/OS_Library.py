# OS Library is able to interact with the operating system. 
# It provides functions for creating, removing, and changing directories, as well as for working with files and directories.

# getcwd() - returns the current working directory
import os
print(os.getcwd())

# mkdir() - creates a new directory
new_path = "new_folder"
# os.mkdir(new_path)

# listdir() - returns a list of the files and directories in the specified path
print(os.listdir())

# Joining multiple paths together
# os.path.join() - joins one or more path components intelligently
dir_name = "new_folder"
file_name = "file_data.txt"

full_path = os.path.join(dir_name, file_name)
print(full_path)

complete_path = os.path.join(os.getcwd(), full_path)
print(complete_path)

# os.path.exists() - returns True if the specified path exists, False otherwise
print(os.path.exists(complete_path))

path_exist = r"C:\Users\heman\Desktop\GenAI_Development\python\python_basic\tuple.py"
print(os.path.exists(path_exist))

# path is a file or a directory
print(os.path.isfile(path_exist))  # Check if it's a file
dir_path = r"C:\Users\heman\Desktop\GenAI_Development\python\python_basic\FileHandling"
print(os.path.isdir(dir_path))   # Check if it's a directory