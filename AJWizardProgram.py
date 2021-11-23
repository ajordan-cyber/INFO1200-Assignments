#!/usr/bin/env python3

#Name: (Austin Jordan)
#Class: (INFO 1200)
#Section: (002)
#Professor: (Noah Say)
#Date: 10/3/2021
#Project #: Module 9 Project
#I declare that the source code contained in this assignment was written solely by me.
#I understand that copying any source code, in whole or in part, 
#constitutes cheating, and that I will receive a zero on this project
#if I am found in violation of this policy.



def displayTitle():
    """Displays the title of the application"""
    print("Austin Jordan's Wizard Inventory Program")
    print()

def displayMenu():
    """Shows the menu options that the user can pick"""
    print("COMMAND MENU")
    print("show - Show all items")
    print("grab - Grab an item")
    print("edit - Edit an item")
    print("drop - Drop an item")
    print("exit - Exit program")
    print()

def show(inventory):
    """shows the inventory of the wizard"""
    for number, item in enumerate(inventory, start=1):
        print(f"{number}. {item}")
        print()

def grabItem(inventory):
    """allows user to pick up new items"""
    #check if we have space to add it
    if len(inventory) >= 5:
        print("Hey, you'll be too heavy if you pick up another item!")
    else:
        #ask the user what they picked up
        item = input("What did you pick up? ")
        #show what the user added
        print("You added a(n) " + str(item))
        #add the item
        inventory.append(item)
        #show the updated inventory
        show(inventory)

def editItem(inventory):
    """allows user to edit items in inventory"""
    #grab the user's input for the item to edit
    number = int(input("Enter a number: "))
    #check if the number is valid
    if number < 1 or number > len(inventory):
        print("That item doesn't exist!")
    #if it is valid, edit the assigned with a new value
    else:
        #grab the user's new value
        print(f"You are editing item number {number}, which is a(n) {inventory[number-1]} ")
        newItem = input("New item value: ")
        inventory[number-1] = newItem
        show(inventory)

def dropItem(inventory):
    """allows user to drop items"""
    #get the item number from the user
    number = int(input("Enter a number: "))
    #check if the number is valid
    if number <1 or number > len(inventory):
        print("That item doesn't exist!")
    #if it is valid, drop the item
    else:
        item = inventory.pop(number-1)
        print(f"{item} was dropped!")
        show(inventory)
    
    

def main():
    """main function will execute other functions"""
    displayTitle()
    displayMenu()

    inventory = ["Wand", "Glasses", "Spellbook"]

    while True:
        command = input("Command: ")
        if command == "show":
            show(inventory)
        elif command == "grab":
            grabItem(inventory)
        elif command == "edit":
            editItem(inventory)
        elif command == "drop":
            dropItem(inventory)
        elif command == "menu":
            displayMenu()
        elif command == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye!")

# checks if the current file is the main file or an imported module
if __name__ == "__main__":
    main()