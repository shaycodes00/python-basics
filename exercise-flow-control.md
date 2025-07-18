# Interactive vending machine

1. Displays a menu of items with prices.
1. Prompts the user to insert money.
1. Allows the user to select an item.
1. Checks if the user has enough funds to purchase the selected item
1. Dispenses the item (i.e., displays a success message) and subtracts its cost from
   the user’s funds.
1. Offers the user the opportunity to make additional purchases or exit the
   simulation.

## Initiate

1. Welcome screen "select item NOW!"
1. Display menu opens when promted
1. Items and prices are listed

### List of menu items (For loop?)

1. Water 5.00
2. Gatorade 7.50
3. Diet Coke 6.50
4. Monster 8.00
5. Sprite 6.00

#### Payment and item selection (While loop/if statement)

1. Promts "choose method of payment" (Cash or Card)
1. User selects desired item (if)
1. Checks if the user has enough funds to purchase the selected item.

##### Dispenses the item (i.e., displays a success message) and subtracts its cost from the user’s funds.

1. Vending machine locates item
1. Vending machine despenses item
1. If vening machine does not locate
1. Tells customer "Item is not found, please select another item"
1. If item found, item dispensed
1. Total is subtracted from users fund

##### Offers the user the opportunity to make additional purchases or exit the simulation

1. Would you like to buy more
1. If "Yes" the process repeats
1. If no, exit the loop
   1. print "Have a nice day!"
