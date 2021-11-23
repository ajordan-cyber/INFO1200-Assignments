#Name: (Austin Jordan)
#Class: (INFO 1200)
#Section: (002)
#Professor: (Noah Say)
#Date: (9/22/21)
#Project #: Module 3 Project
#I declare that the source code contained in this assignment was written solely by me.
#I understand that copying any source code, in whole or in part, 
#constitutes cheating, and that I will receive a zero on this project
#if I am found in violation of this policy.

print("Austin Jordan's Student Registration App")

# grab the user's input
firstName = input("First Name: ")
lastName = input("Last Name: ")
birthYear = int(input("Birth Year: "))

# add a blank line
print()

# welcome message
print("Welcome " + firstName, lastName)

tempPassword = (firstName + "*" + lastName)

print()
print("Temporary password is: " + firstName + "*")
