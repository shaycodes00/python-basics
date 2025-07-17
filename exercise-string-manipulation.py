# Split by delimiter
to_be_changed = "John Glenn|Neil Armstrong|Sally Ride|Douglas Wheelock|Mae Jemison"
changed_values = to_be_changed.split("|")
print(changed_values)

# Split lyrics by line using split()
lyrics = """
Katie Casey was baseball mad,
Had the fever and had it bad.
Just to root for the home town crew,
Ev'ry sou
Katie blew.
On a Saturday her young beau
Called to see if she'd like to go
To see a show, but Miss Kate said "No,
I'll tell you what you can do:"
"""
lyrics_split = lyrics.split("\n")
print(lyrics_split)

# Split lyrics using another method (splitlines)
lyrics_alt = lyrics.splitlines()
print(lyrics_alt)

# String length of long village name
long_village_name = "Llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch"
string_length = len(long_village_name)
print(string_length)

# Strip spaces from path
my_path = ' /c/Users/instructor/Downloads/Submit Relating the Nonrelational Assessment Download May 10, 2021 917 AM '
my_folders = my_path.strip().split("/")
print(my_folders)

# Composer list fix
composers = "Beethoven,Ludwig von;Liszt,Franz;Mozart,Wolfgang;Copland,Aaron"
composers_split = composers.split(";")
third_composer = composers_split[2]
comma_position = third_composer.find(",")

# Join the names to get the 3rd composer's name in "first last" format
first_name = "Wolfgang"
last_name = "Mozart"
full_name = first_name + " " + last_name
print(f"{first_name} {last_name}")
print(full_name)

# Pad strings left and right and combine
left_padded = ' Operators are standing by'
right_padded = 'Call now '
full_message = right_padded.strip() + "! " + left_padded.strip()
print(full_message)
