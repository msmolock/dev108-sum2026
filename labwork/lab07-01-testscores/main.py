#!/usr/bin/env python3
# Michael Smolock
# 7/30/2026
# Lab 7-1
# Dev 108

# Welcome 
def display_welcome():
    print("The Test Scores program")
    print("Enter 'x' to exit")
    print("")

# Enter test scores loop
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
# Complete calculations and print
def process_scores(scores):
    if len(scores) > 0:
        total = sum(scores)
        count = len(scores)
        average = round(total / count)
        low = min(scores)
        high = max(scores)

        sorted_scores = sorted(scores)
        if count % 2 == 1:
            median_score = sorted_scores[count // 2]
        else:
            median_score = (sorted_scores[count // 2 - 1] + sorted_scores[count // 2]) / 2

        print()
        print("Total:            ", total)
        print("Number of Scores: ", count)
        print("Average Score:    ", average)
        print("Low Score:        ", low)
        print("High Score:       ", high)
        print("Median Score:     ", round(median_score))
    else:
        print()
        print("No scores were entered.")

def main():
    display_welcome()
    scores = get_scores()
    process_scores(scores)
    print("")
    print("Bye!")

# if started as the main module, call the main function
if __name__ == "__main__":
    main()
