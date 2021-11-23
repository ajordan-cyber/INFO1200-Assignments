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
print("Austin Jordan's Change Calculator")

#blank after title
print()

choice = "y"
#while loop to prompt the user for cents
while choice.lower() == "y":
    #grab the user's input for cents and assign to variable
    cents = int(input("Enter a number of cents, 0-99: "))
    print() #blank line

    #calc how many quarters are in the cents
    quarters = cents // 25
    #assign cents to leftover amount after taking out quarters
    cents = cents % 25
    #calc how many dimes are in the cents
    dimes = cents // 10
    #assign cents to leftover amount after taking out dimes
    cents = cents % 10
    #calc how many nickels are in the cents
    nickels = cents // 5
    #assign cents to leftover amount after taking out nickels
    cents = cents % 5
    #remainder assigned to pennies
    pennies = cents

    #print how many quarters are in the cents
    print("Quarters: ", quarters)
    #print how many dimes are in the cents
    print("Dimes:    ", dimes)
    #print how many nickels are in the cents
    print("Nickels:  ", nickels)
    #print how many pennies are in the cents
    print("Pennies:  ", pennies)
    
    #ask if the user wants to continue
    print() #blank line
    choice = input("Continue? (y/n): ")
    print() #blank line

#print goodbye message
print("Adios!")