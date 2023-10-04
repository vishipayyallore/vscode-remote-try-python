import random


def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])


def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "Tie"
    if (
        (player_choice == "rock" and computer_choice == "scissors")
        or (player_choice == "scissors" and computer_choice == "paper")
        or (player_choice == "paper" and computer_choice == "rock")
    ):
        return "You win"
    return "Computer wins"


def main():
    player_score = 0
    computer_score = 0

    while True:
        player_choice = input(
            "Enter your choice (rock/paper/scissors): ").lower()
        if player_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(player_choice, computer_choice)
        print(result)

        if result == "You win":
            player_score += 1
        elif result == "Computer wins":
            computer_score += 1

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

    print(f"Your score: {player_score}")
    print(f"Computer's score: {computer_score}")


if __name__ == "__main__":
    main()
