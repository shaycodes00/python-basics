# Functions are reusable pieces of code

def greet(name):
    name = name.lower()
    name = name.capitalize()
    print(f"Hello, {name}!")

def user_input(promt):
    input_value = input(promt)

greet("ReIGN")

def main_menu():
    print("Welcome to the main menu")
    print("1. Start")
    print("2. Exit")

    choice = input("Please choose an option: ")
    
    try:
        choice = int(choice)
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None

    print(f'You chose option {choice}')
    return choice

# Start of the program
print("Hello!")
print("My name is Python.")
greet("ReIGN")

main_menu_choice = main_menu()

if main_menu_choice == 1:
    print("Starting the program...")
elif main_menu_choice == 2:
    print("Exiting the program...")
else:
    print("Invalid choice.")
