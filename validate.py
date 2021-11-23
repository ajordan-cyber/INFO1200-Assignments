#Name: (Austin Jordan)
#Class: (INFO 1200)
#Section: (002)
#Professor: (Noah Say)
#Date: 10/4/2021
#Project #: Validation Participation
#I declare that the source code contained in this assignment was written solely by me.
#I understand that copying any source code, in whole or in part, 
#constitutes cheating, and that I will receive a zero on this project
#if I am found in violation of this policy.

#Austin Jordan's Validation File for the Future Value App

#This will validate the user's input and make sure it's a valid float
#pass in three parameters
def get_float(prompt, low, high):
    while True:
        number = float(input(prompt))

        if number >= low and number <= high:
            return number
        else:
            print("Entry must be greater than", low, "and less than or equal to" , high)



#This will validate the user's input and make sure it's a valid integer
#pass in three parameters
def get_int(prompt, low, high):
    while True:
        number = int(input(prompt))

        if number > low and number <= high:
            return number
        else:
            print("Entry must be greater than", low, "and less than or equal to" , high)



#defines the main logic of the function
def main():
    choice = "y"
    while choice.lower() == "y":
        valid_number = get_float("Enter a number: ", 0, 1000)
        print("Valid number = ", valid_number)
        print()

        valid_integer = get_int("Enter an integer: ", 0, 50)
        print("Valid integer = ", 0, 50)
        print()

        choice = input("Repeat? (y/n): ")

    print("Bye!")

#calling the main function
main()

