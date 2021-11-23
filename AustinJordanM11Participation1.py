#!/usr/bin/env python3
#Name: (Austin Jordan)
#Class: (INFO 1200)
#Section: (002)
#Professor: (Noah Say)
#Date: 11/20/2021
#Project #: Module 11 Participation Part 1
#I declare that the source code contained in this assignment was written solely by me.
#I understand that copying any source code, in whole or in part, 
#constitutes cheating, and that I will receive a zero on this project
#if I am found in violation of this policy.



def get_number(prompt, low, high):
    """
    Grabs a valid floating point number.
    """
    while True:
        try: # catches errors in the following code
            number = float(input(prompt))
            if number > low and number <= high:
                is_valid = True
                return number
            else:
                print(f"Entry must be greater than {low} " 
                      f"and less than or equal to {high}.")
        except ValueError: # Prompts the user to enter valid input
            print("Enter a valid number please! Try Again.")
            
def get_integer(prompt, low, high):
    """
    Grabs a valid integer value.
    """
    while True:
        try: # catches errors in the following code
            number = int(input(prompt))
            if number > low and number <= high:
                is_valid = True
                return number
            else:
                print(f"Entry must be greater than {low} " 
                    f"and less than or equal to {high}.")
        except ValueError: # Prompts the user to enter valid input
            print("Please enter a valid number!")


def calculate_future_value(monthly_investment, yearly_interest, years):
    """
    Calculates the future value using monthly investment, yearly interest, number of years.
    """
    # convert yearly values to monthly values
    monthly_interest_rate = yearly_interest / 12 / 100
    months = years * 12

    # calculate future value
    future_value = 0.0
    for i in range(months):
        future_value += monthly_investment
        monthly_interest = future_value * monthly_interest_rate
        future_value += monthly_interest

    return future_value

def main():
    """
    Contains the main logic of the program
    """
    choice = "y"
    while choice.lower() == "y":
        # get input from the user
        monthly_investment = get_number("Enter monthly investment:\t", 0, 1000)
        yearly_interest_rate = get_number("Enter yearly interest rate:\t", 0, 15)
        years = get_integer("Enter number of years:\t\t", 0, 50)

        # get and display future value
        future_value = calculate_future_value(
            monthly_investment, yearly_interest_rate, years)
        
        print()
        print(f"Future value:\t\t\t{round(future_value, 2)}")
        print()

        # see if the user wants to continue
        choice = input("Continue? (y/n): ")
        print()

    print("Bye!")
    
if __name__ == "__main__":
    main()
