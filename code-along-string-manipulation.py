string1 = 'This in not a valid string'
string2 = "This is also not a valid string"
# string3 = "This is NOT a value string - see why?"

palidrome = "Go hang a salami, I'm a lasagna hog"

# Using quote inside string

string3 = "'Always look on the bright side of life' - Monty Python"

# Use escape characters to include quotes in strings

#len() function

string4 = "\"Always look on the bright side of life\" - Monty Python"
print(string4)

print(len(string4))

# strip() function

name ="        Shay            "
print (len(name))
print(name)

name_no_spaces = name.strip()
print(len(name_no_spaces))
print(name_no_spaces)

# split()

filepath = "var/shay/here"
folders = filepath.split("/")
print(folders)
print(type(folders))

# print(names): ['Shay', 'Reed']

# firstname = names[0]
# lastname = names[1]

# join

WindowsPath = "\\".join(folders)
print(WindowsPath)

# find()

reservation_name = "Froman, Abe"
char_to_find = ","
# where is comma?

char_location = reservation_name.find(char_to_find)
print(char_location)

# index()

char_location = reservation_name.index(char_to_find)
print(char_location)

# transformations

print(reservation_name.upper())
print(reservation_name.lower())
print(reservation_name.title())
print(reservation_name.swapcase())
print(reservation_name.capitalize())

# f-strings

name = "Shay"
age = 27

print(f"My name is {name} and I am {age} years old.")
print("My name is " + name + " and I am " + str(age) + " years old.")

a = 3
b = 9
print(f'We can count to {b} by {a}: {a} {a*2} {a*3}')

# replacing

name = "Sha Red"
name = name.replace("Sha", "Shay")
name = name.replace("Red", "Reed")
print(name)

