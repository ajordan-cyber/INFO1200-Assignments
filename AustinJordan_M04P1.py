#Name: (Austin Jordan)
#Class: (INFO 1200)
#Section: (002)
#Professor: (Noah Say)
#Date: 10/1/2021
#Project #: MO4_P1
#I declare that the source code contained in this assignment was written solely by me.
#I understand that copying any source code, in whole or in part, 
#constitutes cheating, and that I will receive a zero on this project
#if I am found in violation of this policy.

#print a blank line before title
print()
#display title of app
print("Privyet! Austin Jordan's Letter Grade Converter:")

#print a blank line
print()

choice = "y"
#create a while loop that will prompt the user for numerical grade values
while choice.lower() == "y":
    #ask the user to enter a numerical grade value
    number = float(input("Enter a numerical grade: "))
    #determine the letter grade equivalent of the numerical value
    if number > 100:
        print("Wowaweewoo... very nice! I like! Number 1 grade in a Kazakhstan! King in the castle, King in the castle!")
        break
    if number > 93:
        letter = "A"
    elif number > 89:
        letter = "A-"
    elif number > 86:
        letter = "B+"
    elif number > 82:
        letter = "B"
    elif number > 79:
        letter = "B-"
    elif number > 76:
        letter = "C+"
    elif number > 72:
        letter = "C"
    elif number > 69:
        letter = "C-"
    elif number > 66:
        letter = "D+"
    elif number > 62:
        letter = "D"
    elif number > 59:
        letter = "D-"
    elif number >= 0:
        letter = "E"
    else:
        print("Please enter a positive number.")
        continue
    
    #print out a letter grade
    print("Letter Grade:", letter)
    print()
    #ask if the user wants to continue
    choice = input("Continue(y/n?): ")
#print out goodbye
print("Do Svidaniya!")

