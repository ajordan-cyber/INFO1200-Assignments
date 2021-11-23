#Name: (Austin Jordan)
#Class: (INFO 1200)
#Section: (002)
#Professor: (Noah Say)
#Date: 9/22/21
#Project #: Area and Perimeter App
#I declare that the source code contained in this assignment was written solely by me.
#I understand that copying any source code, in whole or in part, 
#constitutes cheating, and that I will receive a zero on this project
#if I am found in violation of this policy.

# greet the user
print("Welcome to the Area and Perimeter Program")
print("By: Austin Jordan")

# blankline
print()

# get dimensions from user
length = int(input("Enter the length: "))
width = int(input("Enter the width: "))

# calculate stuff behind the scenes
area = length * width
perimeter = ((length * 2) + (width * 2))

# provide the user with the area and perimeter
print("=====================")
print("Area = " + str(area))
print("Perimeter = " + str(perimeter))
print()
print("Thanks for using this program!")