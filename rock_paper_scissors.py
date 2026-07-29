import random

choices = ["Rock", "Paper", "Scissors"]

wins = 0
losses = 0
draws = 0

print("=== Rock Paper Scissors Game ===")

while True:
    user_choice = input("\nChoose Rock, Paper, or Scissors: ").capitalize()

    if user_choice not in choices:
        print("Invalid choice. Please choose Rock, Paper, or Scissors.")
        continue

    computer_choice = random.choice(choices)

    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a draw!")
        draws += 1

    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        print("You win!")
        wins += 1

    else:
        print("Computer wins!")
        losses += 1

    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        break

total_games = wins + losses + draws

print("\n===== GAME SUMMARY =====")
print(f"Total Games Played : {total_games}")
print(f"Wins               : {wins}")
print(f"Losses             : {losses}")
print(f"Draws              : {draws}")
print("Thanks for playing!")
