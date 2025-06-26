
#Create a shopping cart programethat willcontinuously ask the user for a fodd product and the price of that procduct
#Have an exit clause  if the user wishes to stop adding more things to their cart 
#At the end show food items and the total cost to the user

foods = []
prices = []
total = 0

while True:
    food = input("Enter food to buy or press q to quit: ")
    if  food.lower() =='q':
      break 
    else:
        price= float(input(f"Enter the price of the {food}: R"))
        foods.append(food)
        prices.append(price)

print("-----YOUR CART-----")
for food in foods:
    print(food, end=" ")


for price in prices:
    total+=price

print("\n")
print(f"Your total is :R{total }")