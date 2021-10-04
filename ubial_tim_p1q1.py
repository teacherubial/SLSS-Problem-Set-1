# Quiz Creation Activity

import time

# Quiz has 5 questions the user will answer.
# It will keep track of score and give
# a final result.

# Introduction
print("Welcome to QwiZ. 🧐")
time.sleep(2)
print("Good luck!")

# Create a list of questions
questions = [
    ["What is the colour of the sun? ", "yellow"]
]

# For each question, print it out and ask the user to answer
for question in questions:
    # Print the question
    print(question[0])

    # Get the user's answer
    user_answer = input().lower().strip(",..?!")

    # See if they're correct
    if user_answer == question[1]:
        print("YOU GOT IT RIGHT!")
    else:
        print("SOWWWWWIE... You DEAD.")