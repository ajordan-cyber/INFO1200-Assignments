#Name: (Austin Jordan)
#Class: (INFO 1200)
#Section: (002)
#Professor: (Noah Say)
#Date: 10/1/2021
#Project #: MO4_P2
#I declare that the source code contained in this assignment was written solely by me.
#I understand that copying any source code, in whole or in part, 
#constitutes cheating, and that I will receive a zero on this project
#if I am found in violation of this policy.

#blank before title
print()

#title
print("Austin Jordan's Tip Calculator v.2")

#blank after title
print()

#get the user's input for the meal cost and assign to a var
mealCost = float(input("Cost of meal: "))
print() #blank line

#create a for loop that will go through 15%, 20%, 25% values for the tip
for percentage in range(15, 30, 5):
    #print the tip percentage
    print(f"{percentage}%")

    #convert the percentage into a deminal
    tipPercent = percentage / 100

    #calculate the tip amount
    tipAmount = round(mealCost * tipPercent, 2)
    
    #calculate the total cost
    total = round(mealCost + tipAmount, 2)

    #display the tip amount based on the tip percentage and meal cost
    print(f"Tip amount:\t${tipAmount}")

    #display the total cost by adding the meal cost and tip amount
    print(f"Total amount:\t${total}")

    #show a blank line
    print()