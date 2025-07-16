# play with for loops

# create a list

# use a for loop and interate through the list

favorite_things = []
print("My favorite things to do:", favorite_things)

favorite_things.append("Traveling")
favorite_things.append("Playing sports")
favorite_things.append("Spending time with friends and family")

print("Updated list of favorite things:", favorite_things)

favorite_things.insert(1, "Watching movies")
print("After inserting another favorite:", favorite_things)

print("Top favorite:", favorite_things[0])
print("Second favorite:", favorite_things[1])
print("Third favorite:", favorite_things[2])
print("Fourth favorite:", favorite_things[3])

skipped_thing = favorite_things.pop(1)
print("This week I'll skip:", skipped_thing)
print("List after removing one:", favorite_things)

print("All favorites by index:")
for i in range(len(favorite_things)):
    print(f"{i + 1}. {favorite_things[i]}")
