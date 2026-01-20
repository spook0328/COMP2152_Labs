# This is the Python file for week 2
import random

choices = ["Rock", "Paper", "Scissors"]

playerChoice = input("Enter your choice (1=Rock, 2=Paper, 3=Scissors): ")
playerChoice = int(playerChoice)

if playerChoice < 1 or playerChoice > 3:
    print("Error: Choice must be between 1 and 3.")
else:
    comChoice = random.randint(1, 3)

    playerChoiceIndex = choices[playerChoice - 1]
    comChoiceIndex = choices[comChoice - 1]

    print("You chose:", playerChoiceIndex)
    print("Computer chose:", comChoiceIndex)

    # Determine the winner
    if playerChoice == comChoice:
        print("It's a tie!")
    elif (playerChoice == 1 and comChoice == 3) or \
         (playerChoice == 2 and comChoice == 1) or \
         (playerChoice == 3 and comChoice == 2):
        print("You win!")
    else:
        print("You lose!")
