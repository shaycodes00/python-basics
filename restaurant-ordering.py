# Define prices for each menu item

burger_price = 5.99
pizza_price = 8.49
salad_price = 4.49
drink_price = 1.99

# Display welcome message and (combine text with variables)

print("Welcome, we hope you're hungry!")
print("Check out our updated menu!")
print(f"1. Burger - ${burger_price}")
print(f"2. Pizza  - ${pizza_price}")
print(f"3. Salad  - ${salad_price}")
print(f"4. Drink  - ${drink_price}")

# Initial item quantity (variables)

burger_qty = 0
pizza_qty = 0
salad_qty = 0
drink_qty = 0

### Start order loop (input varibale stored in item)

item = input("What would you like to order? (Type done to finish): ")

### Quantity of items (convert string to a number (int))

'''quantity = int(input(f"How many [item] would you like? "))

# Add quantity to item count (if)

if item == "burger":'''
