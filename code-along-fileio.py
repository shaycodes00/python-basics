import os

'''file_path = 'data.csv'

print(file_path)

file = open(file_path, 'r') # open in read mode
file = open(file_path, 'w') # open in write mode
file = open(file_path, 'a') # open in append mode
file = open(file_path, 'r+') # open im read/write mode'''

file = open("example.txt", "w")
file.write("Hello, World!\n")
file.write("This is line two!\n")
file.close()

# open a file using the 'with' keyword

with open("example-with.txt", "w") as file:
    file.write("We wrote this file using the 'with' keyword!\n")
    file.write("This lis line two.\n")
    file.write("This is line three.\n")


# read funtion to read the contents of a file

with open("example-with.txt", "r") as file:
    contents = file.read()
    print(contents)

# use the loop to read lines from a file

with open("example-with.txt", "r") as file:
    for line in file:
        print(line.strip())

# append to a file using 'with'

with open("example-with.txt", "a") as file:
    file.write("This is an append line!\n")

# delete a file

if os.path.exists("example3.txt"):
    os.remove("example2.txt")
    print("File deleted.")
else:
    print("The file does not exist.")