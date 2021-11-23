#!/usr/bin/env python3
#Name: (Austin Jordan)
#Class: (INFO 1200)
#Section: (002)
#Professor: (Noah Say)
#Date: 11/8/2021
#Project #: Module 10 Participation P2
#I declare that the source code contained in this assignment was written solely by me.
#I understand that copying any source code, in whole or in part, 
#constitutes cheating, and that I will receive a zero on this project
#if I am found in violation of this policy.

import csv
FILE_NAME = "trips.csv"

def writeTrips(trips):
    # take in a 2d list and then write the contents to a csv file

    # the with keyword starts a process that will open the file for writing
    with open(FILE_NAME, "w", newline="") as output_file:
        # create a writer object that will write to the csv file
        writer = csv.writer(output_file)
        # tell the writer to write the trips to the csv file
        writer.writerows(trips)

def readTrips():
    previousTrips = []
    # read from a csv file and return to the user
    # the with keyword starts a process that will open the file for writing
    with open(FILE_NAME, "r", newline="") as input_file:
        # create a reader object that will read to the csv file
        reader = csv.reader(input_file)
        # tell the reader to read the trips to the csv file
        for row in reader:
            previousTrips.append(row)
    # return the list
    return previousTrips


def listTrips(trips):
    # this will display the trips to the user in a user-friendly format
    # headers
    print("Distance\tGallons\t\tMPG")
    # iterate through all the trips and print out each of the trips
    for singleTrip in trips:
        print(f"{singleTrip[0]}\t\t{singleTrip[1]}\t\t{singleTrip[2]}")

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

    # bla bla
    trips = readTrips()


    more = "y"

    while more.lower() == "y":
        milesDriven = getMilesDriven()
        gallonsUsed = getGallonsUsed()
                                 
        mpg = round((milesDriven / gallonsUsed), 2)
        print(f"Miles Per Gallon:\t{mpg}")
        print()

        singleTrip = [milesDriven, gallonsUsed, mpg]
        trips.append(singleTrip)
        
        more = input("More entries? (y or n): ")
    
    
    # call the writeTrips() function
    writeTrips(trips)
    # call the listTrips() fn
    listTrips(trips)

    print("Bye!")

if __name__ == "__main__":
    main()

