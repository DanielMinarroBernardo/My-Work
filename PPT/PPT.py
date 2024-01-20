import random
import sys

# Constants for choices
ROCK = 1
PAPER = 2
SCISSORS = 3

def main():
    print("\nChoose what you want to play: \n1. Rock\n2. Paper\n3. Scissors")
    user_choice = int(input("Enter the number of your choice: "))
    play_round(user_choice)

def display_choices(user, pc):
    choices = {ROCK: "Rock", PAPER: "Paper", SCISSORS: "Scissors"}
    print(choices[user], " vs ", choices[pc])

def repeat_game():
    print("\nDo you want to play again?")
    print("1. Yes\n2. No")
    repeat = int(input("Enter the number of the action to perform: "))
    if repeat == 1:
        main()
    else:
        sys.exit()

def play_round(user_choice):
    # Generate a random choice for the computer
    pc_choice = random.randint(1, 3)
    display_choices(user_choice, pc_choice)

    # Determine the winner of the round
    if user_choice == pc_choice:
        print("It's a tie")
    elif (user_choice == ROCK and pc_choice == SCISSORS) or \
         (user_choice == PAPER and pc_choice == ROCK) or \
         (user_choice == SCISSORS and pc_choice == PAPER):
        print("You won")
    else:
        print("You lost")

    # Ask if the player wants to play again
    repeat_game()

if __name__ == "__main__":
    main()
