#Name: (Austin Jordan)
#Class: (INFO 1200)
#Section: (002)
#Professor: (Noah Say)
#Date: 10/4/2021
#Project #: M05 Project P1
#I declare that the source code contained in this assignment was written solely by me.
#I understand that copying any source code, in whole or in part, 
#constitutes cheating, and that I will receive a zero on this project
#if I am found in violation of this policy.


#define function for main()
def main():
    #print title
    print()
    print("Austin Jordan's Even or Odd Checker")
    print()

    #grab user's input for the number
    my_num = int(input("Enter a number: "))

    #pass that number into the is_even() function and determine if it's even or odd
    #and print out the result of the check
    if is_even(my_num):
        print("The number is even!")
    else:
        print("The number is odd!")






#define function for is_even(), to check if a number is even
def is_even(my_num):
    """This function checks if a number is even or odd"""
    #checks if the given number is even or odd
    if my_num % 2 == 0:
        return True
    else:
        return False


#add an if statement to check if the current module is the main module
if __name__ == "__main__":
    main()

