#Name: (Austin Jordan)
#Class: (INFO 1200)
#Section: (002)
#Professor: (Noah Say)
#Date: 9/22/21
#Project #: Miles Per Gallon App
#I declare that the source code contained in this assignment was written solely by me.
#I understand that copying any source code, in whole or in part, 
#constitutes cheating, and that I will receive a zero on this project
#if I am found in violation of this policy.

# Display my name
print("Austin Jordan's MPG App")
print()


# display a welcome message
print("The Miles Per Gallon program")
print()

# get input from the user
miles_driven= float(input("Enter miles driven: "))
gallons_used = float(input("Enter gallons of gas used: "))
costGas = float(input("Enter cost per gallon: "))

# calculate miles per gallon
mpg = miles_driven / gallons_used
mpg = round(mpg, 2)

# Calculate gas cost
totalGasCost = gallons_used * costGas

# Calculate cost per mile
costPerMile = (costGas * gallons_used) / miles_driven
            
# format and display the result
print()
print("Miles Per Gallon: " + str(round(mpg, 1)))
print("Total Gas Cost: " + str(round(totalGasCost,1)))
print("Cost Per Mile: " + str(round(costPerMile, 1)))
print()
print("Bye")


