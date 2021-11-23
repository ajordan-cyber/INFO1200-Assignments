#Name: (Austin Jordan)
#Class: (INFO 1200)
#Section: (002)
#Professor: (Noah Say)
#Date: 9/27/21
#Project #: MPG Module 4 App (Participation)
#I declare that the source code contained in this assignment was written solely by me.
#I understand that copying any source code, in whole or in part, 
#constitutes cheating, and that I will receive a zero on this project
#if I am found in violation of this policy.

#variable for another trip
anotherTrip = "y"

#while loop will execute until the user enters no
while anotherTrip.lower() == "y":

    # display a welcome message
    print("Austin Jordan's Miles Per Gallon App")
    print()

    # get input from the user
    miles_driven = float(input("Enter miles driven:         "))
    gallons_used = float(input("Enter gallons of gas used:  "))
    cost_per_gallon = float(input("Enter cost per gallon:  "))

    #checks if the user's input is greater than zero
    if miles_driven <= 0:
        print("Miles driven must be greater than zero. Please try again.")
    elif gallons_used <= 0:
        print("Gallons used must be greater than zero. Please try again.")
    elif cost_per_gallon <= 0:
        print("Cost per gallon must be greater than 0. Please try again.")
    else:
        # calculate and display miles per gallon
        mpg = round((miles_driven / gallons_used), 2)
        
        #total gas cost and cost mer mile
        total_gas_cost = round((cost_per_gallon * gallons_used), 2)
        cost_per_mile = round((total_gas_cost / miles_driven), 2)
        print("Miles Per Gallon:          ", mpg)
        print("Total Gas Cost:          ", total_gas_cost)
        print("Cost Per Mile:          ", cost_per_mile)
    anotherTrip = input("Another trip? ('y/n'): ")
print()
print("Bye")



