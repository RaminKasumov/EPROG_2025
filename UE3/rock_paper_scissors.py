import random

def play_rock_paper_scissors(user_choice):
    choices = ["ROCK", "PAPER", "SCISSORS"]
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        return 0
    elif (user_choice == "ROCK" and computer_choice == "SCISSORS") or \
         (user_choice == "PAPER" and computer_choice == "ROCK") or \
         (user_choice == "SCISSORS" and computer_choice == "PAPER"):
        return 1
    else:
        return -1


def play_three_rounds():
    score = 0
    for i in range(3):
        user = input("Choose ROCK, PAPER, or SCISSORS: ")
        result = play_rock_paper_scissors(user)
        score += result
        if result == 1:
            print("You win this round!")
        elif result == -1:
            print("Computer wins this round!")
        else:
            print("Draw!")
    if score > 0:
        print("You win the game!")
    elif score < 0:
        print("Computer wins the game!")
    else:
        print("It's a tie!")

play_three_rounds()