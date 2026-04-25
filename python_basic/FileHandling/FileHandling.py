# File Handling in Python: 
# in computer system information can be stored in RAM (Random Access Memory) or in a file.
# RAM is volatile memory, which means that the information stored in it is lost when the computer is turned off.
#  On the other hand, a file is a non-volatile storage medium that can store information permanently. 

# In case of NLP-> text data(sequencial data)-> text file(.txt) or csv file(.csv) or json file(.json)
# but in machine learning models are stored in binary files(.pkl) or in hdf5 files(.h5)

# types of file handling in python:
#1) text file handling -> .txt, .csv, .json, .docx, .pdf
#2) binary file handling -> .png, .jpg, .mp4, .pkl, .h5

# STeps to handle file in python:
#1) open the file -> open() function is used to open a file in python.
#2) read or write data -> read() or write() methods are used to read or write data from/to the file.
#3) close the file -> close() method is used to close the file.

# Task 1: Read the content from a text file.
# Open the file
# open() function takes two arguments: the name of the file and the mode in which the file is opened.
# The mode can be 'r' for reading, 'w' for writing, "r+" for reading and then writing, 'w+' for writing and then reading
# Read the file
# read() method is used to read the content of the file. It returns the content as a string.
# Close the file
# close() method is used to close the file. It is important to close the file after
# you are done with it to free up system resources.

f = open("Filehandlingexample.txt", "r")

content = f.read()
print(content)
f.close()

# Task 2: Writing content to a text file.
f = open("Filehandlingexample.txt", "w")
f.write("This is an example of writing to a file in python.")
# It overwrites the existing content of the file. 
# If the file does not exist, it creates a new file.
# if you want to append the content to the existing file, you can use 'a' mode instead of 'w' mode.
f.close()

# task 3: Appending content to a text file.
f = open("Filehandlingexample.txt", "a")
f.write("\nThis is an example of appending to a file in python.")
# It appends the content to the existing file.
f.close()

# with statement is used to handle files in python. It is a context manager that automatically closes the file 
# after the block of code is executed.
with open("Filehandlingexample.txt", "r") as f:
    content = f.read()
    # print(content)

with open("Filehandlingexample.txt", "w") as f:
    f.write("This is an example of writing to a file using with statement in python.")


# write the content line by line using writelines() method
lines = ["This is line 1.\n", "This is line 2.\n", "This is line 3.\n"]
with open("Filehandlingexample.txt", "w") as f:
    f.writelines(lines)

# write content in binary file
# Mode 'wb' is used to write in binary mode. It is used to write binary data to a file.
# Mode 'rb' is used to read in binary mode. It is used to read binary data from a file.
# data = b'\x0x48\x65\x6c\x6c\x6f'  # This is the binary representation of "Hello"
# with open("Filehandlingexample.txt", "wb") as binary_data:
#     binary_data.write(data)


# read the file from Filehandlingexample.txt and write in distinationFile.txt
with open("Filehandlingexample.txt", "r") as source_file:
    content = source_file.read()
    print("source\n",content)
with open("distinationFile.txt", "w") as dest_file:
    dest_file.write(content)
with open("distinationFile.txt", "r") as dest_file:
    content = dest_file.read()
    print("destination\n",content)

# Reading total line, total word and total character from a text file.

def count_file_content(file_name):
    with open(file_name, "r") as f:
        lines = f.readlines()
        Total_line = len(lines)
        Total_word = sum(len(line.split()) for line in lines)
        Total_Character = sum(len(line) for line in lines)
    
    return Total_line, Total_word, Total_Character

file_name = "Total_data.txt"
Total_line, Total_word, Total_Character = count_file_content(file_name)
print(f"Total line: {Total_line}")
print(f"Total word: {Total_word}")
print(f"Total character: {Total_Character}")