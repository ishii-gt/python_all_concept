# file Handling : To handle our file
# mode  : w(write and create file if not exist ) ,
#  r(read existed file),
# a(append file(update)), 
# +w(write and read) , 
# +r(read and write) , 
# +a(append and read)
# rb(read file in binary)
# wb(write a file in binary)






# Basic File Operations:
# 1. Write a Python program to create a new file and write some text
# into it.



file = open("data1.txt","w")
file.write("where are you.\n")
file.write("How are you\n")


file.close()
print("Data Written")


# 2. Write a Python program to read the contents of a file and display
# them on the screen.


file = open("data1.txt","r")

content = file.read()

print(content)

file.close()



# 3. Write a Python program to append text to an existing file.


file = open("data1.txt","a")

file.write("Good Evening\n")


file.close()


# Working with Different File Modes:
# 1. Explain the different file modes available in Python. Write a Python
# program to demonstrate reading a file in binary mode.

with open("data1.txt","rb") as file:
    data = file.read()
    print(data)


# 2. Write a Python program to demonstrate writing to a file in binary
# mode.


with open("binary_file","wb") as file:
    data = b"Hy ,Its Binary File Here!"
    file.write(data)


print("Data written Successfully ")



# Reading Files:
# 1. Write a Python program to read a file line by line and display each
# line.
# Read a file line by line and display each line



with open("data1.txt","r") as file:
    for line in file:
        print(line)

# 2. Write a Python program to read a file into a list, where each
# element is a line from the file.

with open("data1.txt","r") as file:
    lines = file.readline()
    print(line)



# File Handling Exceptions:
# 1. Write a Python program to handle exceptions when trying to read
# from a non-existent file.

try :
    file=open("data1.txt","r")
    content = file.read()
    print(content)
    file.close()

except FileExistsError:
    print("file does not exits.")




# 2. Write a Python program to handle exceptions when trying to write
# to a read-only file




# File Position:
# 1. Write a Python program to demonstrate the use of the tell() and
# seek() methods.

# tell() shows the current cursor position.
# seek(0) moves the cursor back to the start of morning.txt.
# read(5) reads the first 5 characters from the file.


with open("data1.txt", "r") as file:
    print("Initial Position:", file.tell())

    data = file.read(5)
   

    print(file.tell())

    file.seek(0)  

    print("Position after seek:", file.tell())

    data = file.read(5)
    print(data)





# 2. Write a Python program to move the file pointer to a specific
# position and read from there.


with open("data1.txt","r") as file:
    file.seek(5)

    data = file.read()
    print(data)


# Working with CSV Files:
# 1. Write a Python program to read data from a CSV file and display it.








# 2. Write a Python program to write data to a CSV file.








# File Copying:
# 1. Write a Python program to copy the contents of one file to
# another.




with open("data1.txt", "r") as source:
    data = source.read()

with open("copy.txt", "w") as destination:
    destination.write(data)

print("File copied successfully.")  




with open("data1.txt","r") as file:
    data = source.read()
with open("copy.txt","w") as destination:
    destination.write(data)

    



# 2. Write a Python program to copy a binary file.



# File Deletion:
# 1. Write a Python program to delete a file.




# 2. Write a Python program to check if a file exists before trying to
# delete it.




# File Compression:
# 1. Write a Python program to compress a file using gzip.




# 2. Write a Python program to decompress a gzip file.





# Advanced File Handling:
# 1. Write a Python program to read a large file in chunks.






# 2. Write a Python program to merge multiple files into a single file.


# File Permissions:
# 1. Write a Python program to change the permissions of a file.


# 2. Write a Python program to check the permissions of a file.



# File Comparison:
# 1. Write a Python program to compare the contents of two files and
# print the differences.




# 2. Write a Python program to check if two files are identical.