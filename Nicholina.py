# Below are the requirements for the program:



# The program should ask the user to enter the charge for the food.

# It should then calculate the amounts of an 18 percent tip and 7 percent sales tax on the charge of the food and display each of these amounts.

# Finally, it should add everything together and display the charge of the food plus tip and sales tax.

# Based on this data, your program should generate script that meets the requirements. 

 

# Below is an example execution of the program: 

# input

# Charge for food = $50.00



# output

# Tip = $9.00

# Sales tax = $3.50

# Grand total = $62.50

charge_of_food = float(input('Charge for food = $'))
tip = (18/100)* charge_of_food
sales_tax = (7/100)* charge_of_food
grand_total = charge_of_food + tip + sales_tax  
print(f'Tip = ${tip:1.2f}')
print(f'Sales tax = ${sales_tax:1.2f}')
print(f'Grand Total = ${grand_total:1.2f}')