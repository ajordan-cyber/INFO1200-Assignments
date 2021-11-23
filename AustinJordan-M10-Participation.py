#!/usr/bin/env python3
#Name: (Austin Jordan)
#Class: (INFO 1200)
#Section: (002)
#Professor: (Noah Say)
#Date: 11/8/2021
#Project #: Module 10 Participation
#I declare that the source code contained in this assignment was written solely by me.
#I understand that copying any source code, in whole or in part, 
#constitutes cheating, and that I will receive a zero on this project
#if I am found in violation of this policy.


import csv

FILE_NAME = "trips.csv"

def getMilesDriven():
    while (milesDriven := float(input("Enter miles driven:\t"))) <= 0:                    
        print("Entry must be greater than zero. Please try again.\n")       
    return milesDriven
          
def getGallonsUsed():
    while (gallonsUsed := float(input("Enter gallons of gas:\t"))) <= 0:                    
        print("Entry must be greater than zero. Please try again.\n")
    return gallonsUsed
        
def main():
    # display a welcome message
    print("The Miles Per Gallon program")
    print()

    # create a new empty 2d list to hold trip values
    trips = []

    more = "y"
    while more.lower() == "y":
        milesDriven = getMilesDriven()
        gallonsUsed = getGallonsUsed()
                                 
        mpg = round((milesDriven / gallonsUsed), 2)
        print(f"Miles Per Gallon:\t{mpg}")
        print()

        # create a single trip and add it to the list
        singleTrip = [milesDriven, gallonsUsed, mpg]
        trips.append(singleTrip)
        
        more = input("More entries? (y or n): ")
    
    # the with keyword starts a process that will open the file for writing
    with open(FILE_NAME, "w", newline="") as output_file:
        # create a writer object that will write to the csv file
        writer = csv.writer(output_file)
        # tell the writer to write the trips to the csv file
        writer.writerows(trips)


    print("Bye!")

if __name__ == "__main__":
    main()

