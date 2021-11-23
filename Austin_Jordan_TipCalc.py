#Name: (Austin Jordan)
#Class: (INFO 1200)
#Section: (002)
#Professor: (Noah Say)
#Date: 9/22/21
#Project #: Tip Calculator App
#I declare that the source code contained in this assignment was written solely by me.
#I understand that copying any source code, in whole or in part, 
#constitutes cheating, and that I will receive a zero on this project
#if I am found in violation of this policy.

#displays the app name
print("Austin Jordan's Tip Calculator!")

# creates variable for the cost of the meal
costOfMeal = float(input("Cost of meal: "))

# asks user for their desired tip percentage and creates a variable for it
tipPercentage = float(input("Tip Percentage: "))

# creates a variable for the tip amount after calculations
tipAmount = costOfMeal * (tipPercentage / 100)

# tells the user how much the tip is by itself
print("Tip Amount: " + str(round(tipAmount, 2)))

# creates a variable for the total amount of the meal plus the tip
totalAmount = tipAmount + costOfMeal

# tells the user how much the total price of the meal and tip added together
print("Total Amount: " + str(round(totalAmount, 2)))