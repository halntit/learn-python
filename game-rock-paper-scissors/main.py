import random

choises = ["rock", "paper", "scissors"]

while True:
    computer = random.choice(choises)
    player = None

    while player not in choises:
        player = input("rock, paper or scissors? ").lower()

    print("computer: " + computer + " vs. player: " + player)

    if player == computer:
        print("Draw!")
    elif player == "rock" and computer == "scissors":
        print("Player wins!")
    elif player == "paper" and computer == "rock":
        print("Player wins!")
    elif player == "scissors" and computer == "paper":
        print("Player wins!")
    else:
        print("Computer wins!")

    print("Do you want to play again? (Y/n)", end=" ")
    answer = input()
    if answer in ["no", "n", "No", "N"]:
        break

print("Goodbye!")