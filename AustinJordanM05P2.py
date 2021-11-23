#Name: (Austin Jordan)
#Class: (INFO 1200)
#Section: (002)
#Professor: (Noah Say)
#Date: 10/4/2021
#Project #: M05 Project P2
#I declare that the source code contained in this assignment was written solely by me.
#I understand that copying any source code, in whole or in part, 
#constitutes cheating, and that I will receive a zero on this project
#if I am found in violation of this policy.

#imports the converter module as "c"
import converter as c


#this is our main file

#defines the main function
def main():
    #calls the welcome message
    fm_welcome()
    #starts a while loop to run the program until user enters "n"
    while True:
        fm_menu()

        #defines a choice for the user to continue or quit at the end of the program
        choice = input("Choose a conversion a/b: ")

        # convert from feet to meters
        if choice.lower() == "a":
            feet = float(input("Enter number of feet: "))
            meters = c.to_meters(feet)
            # show the converted value
            print("====================")
            print(f"{feet} = {round(meters, 2)} meters")
            print("====================")
            print()

        #convert from meters to feet
        elif choice.lower() == "b":
            meters = float(input("Enter number of meters: "))
            feet = c.to_feet(meters)
            # show the converted value
            print("====================")
            print(f"{meters} = {round(feet, 2)} feet")
            print("====================")
            print()


        #prompt the user to only enter a or b
        else:
            print("Sorry, not a valid letter. Please try again. Choose 'a' or 'b'.")
            print()
        #ask the user if they want to run the program again or quit
        repeat = input("Go again? (y/n): ")

        #takes user input and either quits or reruns the program
        if repeat != "y":
            print()
            print("See ya later calculator!")
            print()
            break
    
#defines the welcome message
def fm_welcome():
    print()
    print("Austin Jordan's Feet/Meters Converter")
    print()

#defines the conversion menu
def fm_menu():
    print("Conversions Menu:")
    print("a. Feet to Meters")
    print("b. Meters to Feet")
    print()

#something about importing stuff?
if __name__ == "__main__":
    main()