# Rock, paper and scissors programs.
# Andre

import random

while True:
    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices) # creating computing choices to play with us
    player = None

    while player not in choices:  # if the input does not match with choices
        player = input("rock, paper or scissors? ").lower() # using lowercase to avoid errors

    print("Computer: ", computer)
    print("Player: ", player)

    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "paper":
        print("You lose!")
    elif player == "rock" and computer == "scissors":
        print("You win!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == "paper" and computer == "scissors":
        print("You lose!")
    elif player == "scissors" and computer == "paper":
        print("You win!")
    elif player == "scissors" and computer == "rock":
        print("You lose!")

    play_again = input("Play again? (yes/no): ").lower()
    if play_again != "yes":
        break

print("Goodbye!")

# shorter version of the same code: applying the OR 

import random

while True:
    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock, paper or scissors? ").lower()

    print("Computer: ", computer)
    print("Player: ", player)

    if player == computer:
        print("It's a tie!")
    elif (player == "rock" and computer == "paper") or \
         (player == "paper" and computer == "scissors") or \
         (player == "scissors" and computer == "rock"):
        print("You lose!")
    else:  # This covers the winning scenarios
        print("You win!")

    play_again = input("Play again? (yes/no): ").lower()
    if play_again != "yes":
        break

print("Goodbye!")
