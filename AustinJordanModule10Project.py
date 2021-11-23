#!/usr/bin/env python3
#Name: (Austin Jordan)
#Class: (INFO 1200)
#Section: (002)
#Professor: (Noah Say)
#Date: 11/20/2021
#Project #: Module 10 Project
#I declare that the source code contained in this assignment was written solely by me.
#I understand that copying any source code, in whole or in part, 
#constitutes cheating, and that I will receive a zero on this project
#if I am found in violation of this policy.

# imports csv module
import csv

# defines the FILENAME from an outside source ("monthly_sales.csv")
FILENAME = "monthly_sales.csv"

def displayTitle():
    """
    defines the displayTitle() fn
    """
    print()
    print("Austin Jordan's Monthly Sales App")
    print()

def displayMenu():
    """
    defines the displayMenu() fn
    """
    print()
    # lists available commands to user
    print("COMMAND MENU")
    print("m - Show monthly sales")
    print("y - Show yearly sales")
    print("e - Edit the sales for a specified month")
    print("x - Exit program")

def readSales():
    """
    defines the readSales() fn
    """
    sales = []
    # open the file
    # interact with the file
    # close the file
    with open(FILENAME, newline="") as file:
        # create a new reader (narrator)
        reader = csv.reader(file)
        # iterate through the file and add the rows to our sales list
        for row in reader:
            sales.append(row)
    return sales


def viewMonthlySales(sales):
    """
    defines the viewMonthlySales() fn
    """
    # iterate through the sales list and print out the months and sale values
    for row in sales:
        print(f"{row[0]} - {row[1]}")
        print()

def viewYearlySummary(sales):
    """
    defines the viewYearlySummary() fn
    """
    total = 0
    for row in sales:
        monthlyAmount = int(row[1])
        total += monthlyAmount

    # get count
    count = len(sales)
    
    # calculate average
    average = total / count
    average = round(average, 2)

    # format and display the result
    print("Yearly total:    ", total)
    print("Monthly average: ", average)        
    print()

# defines the edit() command
def edit(sales):
    """
    defines the edit() fn
    """
    # defines the user input options for names of the month
    names = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
    # asks the user to input a month choice
    name = input("What month do you want to edit? (Use 3 letter abbreviations): ")

    # capitalizes the first letter of each word in the string
    # name = name.title()

    # prompts the user to use 3 letter abbreviations for months if they are apes
    if name not in names:
        print("You must use 3-letter abbreviations for your month input, for example, 'feb' = February")
    else: 
        index = names.index(name)
        amount = int(input("Enter the new sales amount: ")) # gets user's input for new sales amount
        month = [] # eg. jan, 123
        month.append(name)
        month.append(amount)

        # overwrites the previous sales row with the new sales row
        sales[index] = month

        writeSales(sales)

        # tells the user which month was modified
        print(f"Sales amount for {month[0]} was modified.")
        print()

def writeSales(sales):
    """
    defines the logic for the writeSales() function
    """
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(sales)


def main():
    """
    defines the main() function logic
    """
    displayTitle()
    displayMenu()

    sales = readSales()

    # logic for command input
    while True:
        command = input("Command: ")
        if command == "m":
            viewMonthlySales(sales)
        elif command == "y":
            viewYearlySummary(sales)
        elif command == "e":
            edit(sales)
        elif command == "x":
            break
        else: # shows user they are ape
            print("Not a valid command. Please try again.\n")
            print("Bye!")

#checks if the current module is the main module
if __name__ =="__main__":
    main()