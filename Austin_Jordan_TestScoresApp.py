#Name: (Austin Jordan)
#Class: (INFO 1200)
#Section: (002)
#Professor: (Noah Say)
#Date: 9/22/21
#Project #: Test Scores App
#I declare that the source code contained in this assignment was written solely by me.
#I understand that copying any source code, in whole or in part, 
#constitutes cheating, and that I will receive a zero on this project
#if I am found in violation of this policy.

# display a welcome message
print("Austin Jordan's Test Scores App")
print()
print("The Test Scores program")
print()
print("Enter 3 test scores")
print("======================")

# get scores from the user
score1 = int(input("Enter test score #1: "))
score2 = int(input("Enter test score #2: "))
score3 = int(input("Enter test score #3: "))

# calculate average score
totalScore = (score1 + score2 + score3)
averageScore = round(totalScore / 3)
             
# format and display the result
print("======================")
print("Your Scores: " + str(score1) + " " + str(score2) + " " + str(score3))
print("Total Score: " + str(totalScore))
print("Average Score: " + str(averageScore))
print()
print("Bye Felicia")


