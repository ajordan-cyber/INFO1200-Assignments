#Name: (Austin Jordan)
#Class: (INFO 1200)
#Section: (002)
#Professor: (Noah Say)
#Date: 9/27/21
#Project #: Future Value Module 4 App (Participation)
#I declare that the source code contained in this assignment was written solely by me.
#I understand that copying any source code, in whole or in part, 
#constitutes cheating, and that I will receive a zero on this project
#if I am found in violation of this policy.

# display a welcome message
print("Welcome to Austin's Future Value Calculator")
print()

choice = "y"
while choice.lower() == "y":

    is_valid = True

    #check the monthly investment value if correct
    while is_valid:
        # get input from the user
        monthly_investment = float(input("Enter monthly investment:\t"))
        if monthly_investment > 0 and monthly_investment <= 1000:
            is_valid = False
        else:
            print("Entry must be greater than 0 and less than 1000. Please try again.")
    #close while 
    is_valid = True
    
    #check if the yearly interest rate is correct
    while is_valid: 
        yearly_interest_rate = float(input("Enter yearly interest rate:\t"))

        if yearly_interest_rate > 0 and yearly_interest_rate <= 15:
            is_valid = False
        else:
            print("Entry must be greater than zero and less than 15. Please try again.")
    #close while       
    is_valid = True
    
    #check if number of years is correct
    while is_valid:
        years = int(input("Enter number of years: "))
        if years > 0 and years <= 50:
            is_valid = False
        else:
            print("Entry must be greater than 0 and less than 150. Please try again.")
    #close while
    is_valid = True
        

    # convert yearly values to monthly values
    monthly_interest_rate = yearly_interest_rate / 12 / 100
    months = years * 12

    # calculate the future value
    future_value = 0
    for i in range(1, months + 1):
        future_value += monthly_investment
        monthly_interest_amount = future_value * monthly_interest_rate
        future_value += monthly_interest_amount
        if i % 12 == 0:
                print("Year = ", i // 12, "\tFuture Value = ", round(future_value, 2))

    # display the result
    print("Future value:\t\t\t" + str(round(future_value, 2)))
    print()

    # see if the user wants to continue
    choice = input("Continue (y/n)? ")
    print()

print("Bye!")
