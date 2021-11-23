#!/usr/bin/env python3
#Name: (Austin Jordan)
#Class: (INFO 1200)
#Section: (002)
#Professor: (Noah Say)
#Date: 11/20/2021
#Project #: Module 11 Participation Part 2
#I declare that the source code contained in this assignment was written solely by me.
#I understand that copying any source code, in whole or in part, 
#constitutes cheating, and that I will receive a zero on this project
#if I am found in violation of this policy.


# import modules for reading/writing and for the sys functions
import csv
import sys

FILENAME = "movies.csv"

def exit_program():
    """
    Exit out the program
    """
    print("Terminating program.")
    sys.exit()

def read_movies():
    """
    Open a file for reading and then add the file rows to a movies list
    """
    try:
        movies = []
        with open(FILENAME, newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                movies.append(row)
        return movies
    except FileNotFoundError as e:
        #print(f"Could not find {FILENAME} file.")
        #exit_program()
        return movies
    except Exception as e:
        print(type(e), e)
        exit_program()

def write_movies(movies):
    """
    Open a file for writing and write the "movies" parameter to the file
    """
    try:
        with open(FILENAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(movies)
    # creating an error object and renaming it as e
    except OSError as e:
        # using the renamed object, we're showing the type of the error
        # and the line that the error occurred on
        print(type(e), e)
    except Exception as e:
        print(type(e), e)
        exit_program()

def list_movies(movies):
    """
    interate through a list of movies and display them
    """
    for i, movie in enumerate(movies, start=1):
        print(f"{i}. {movie[0]} ({movie[1]})")
    print()
    
def add_movie(movies):
    """
    takes in user input and adds the movie to the movies list
    """
    name = input("Name: ")
    # Add data validation to the add_movie() function so the year entry is a valid integer that's greater than zero.
    while True:
        try:
            year = int(input("Year: "))
            if year >= 0:
                break
            else:
                print("The year has to be greater than zero.")
                continue
        except:
            print("Please enter a numerical value here! Try Again.")
            continue
    movie = [name, year]
    movies.append(movie)
    write_movies(movies)
    print(f"{name} was added.\n")

def delete_movie(movies):
    """
    takes in user input and removes a movie from the movies list
    """
    while True:
        try:
            number = int(input("Number: "))
        except ValueError:
            print("Invalid integer. Please try again.")
            continue
        if number < 1 or number > len(movies):
            print("There is no movie with that number. Please try again.")
        else:
            break
    movie = movies.pop(number - 1)
    write_movies(movies)
    print(f"{movie[0]} was deleted.\n")

def display_menu():
    """
    show a list of commands to the user
    """
    print("The Movie List program")
    print()
    print("COMMAND MENU")
    print("list - List all movies")
    print("add -  Add a movie")
    print("del -  Delete a movie")
    print("exit - Exit program")
    print()    

def main():
    """
    takes care of the primary logic of the program
    """
    display_menu()
    movies = read_movies()
    while True:        
        command = input("Command: ")
        if command.lower() == "list":
            list_movies(movies)
        elif command.lower() == "add":
            add_movie(movies)
        elif command.lower() == "del":
            delete_movie(movies)
        elif command.lower() == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye!")

if __name__ == "__main__":
    main()
