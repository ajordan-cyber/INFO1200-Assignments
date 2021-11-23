#!/usr/bin/env python3

#Name: (Austin Jordan)
#Class: (INFO 1200)
#Section: (002)
#Professor: (Noah Say)
#Date: 10/27/2021
#Project #: Module 9 Participation
#I declare that the source code contained in this assignment was written solely by me.
#I understand that copying any source code, in whole or in part, 
#constitutes cheating, and that I will receive a zero on this project
#if I am found in violation of this policy.


def display_welcome():
    print("The Test Scores program")
    print("Enter 'x' to exit")
    print("")

def get_scores():
    scores = []

    while True:
        score = input("Enter test score: ")
        if score == "x":
            return scores
        else:
            score = int(score)
            if score >= 0 and score <= 100:
                scores.append(score)
            else:
                print("Test score must be from 0 through 100. " +
                      "Score discarded. Try again.")

def process_scores(scores_list):
    scores_list.sort()

    # counts how many scores there are in the scores list
    num_scores = len(scores_list)

    score_total = 0

    # calculates the total score
    for score in scores_list:
        score_total += score

    #calculate the average score
    average = score_total / num_scores

    #scores = [99, 100, 45]

    #grab the minimum score
    minimum_score = min(scores_list)

    #grab the maximum score
    maximum_score = max(scores_list)

    #grab the median score
    median_index = num_scores // 2

    median = 0
    # checks if the number is odd
    if num_scores % 2 == 1:
        median = scores_list[median_index]
    else:
        median_left = scores_list[median_index - 1]
        median_right = scores_list[median_index]

        median = (median_left + median_right) / 2
        
        

    # format and display the result
    print()
    print("Score total:       ", score_total)
    print("Number of Scores:  ", num_scores)
    print("Average Score:     ", average)
    print("Minimum Score:     ", minimum_score)
    print("Maximum Score:     ", maximum_score)
    print("Median Score:      ", median)

def main():
    display_welcome()
    scores = get_scores()
    process_scores(scores)
    print("")
    print("Bye!")

# if started as the main module, call the main function
if __name__ == "__main__":
    main()


