import random  # Importing the random library for computer's choice

def get_computer_choice():
    """Function to randomly choose rock, paper, or scissors for the computer."""
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def get_winner(user_choice, computer_choice):
    """Function to determine the winner of a single round."""
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

def play_game(rounds):
    """Main function to play the game."""
    user_points = 0
    computer_points = 0

    for round_number in range(1, rounds + 1):
        print(f"\n--- Round {round_number} ---")
        user_choice = input("Choose rock, paper, or scissors: ").lower()

        # Validate user input
        while user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            user_choice = input("Choose rock, paper, or scissors: ").lower()

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        # Determine the winner of the round
        winner = get_winner(user_choice, computer_choice)
        if winner == "user":
            print("You win this round!")
            user_points += 1
        elif winner == "computer":
            print("Computer wins this round!")
            computer_points += 1
        else:
            print("It's a tie!")

        # Print the current scores
        print(f"Score -> You: {user_points}, Computer: {computer_points}")

        # Stop the game early if there's already a clear winner
        if user_points > rounds // 2 or computer_points > rounds // 2:
            break

    # Declare the final winner
    print("\n--- Final Result ---")
    if user_points > computer_points:
        print(f"Congratulations! You won the game with {user_points} points.")
    elif computer_points > user_points:
        print(f"Computer wins the game with {computer_points} points. Better luck next time!")
    else:
        print("The game is a tie!")

# Run the game
print("Welcome to Rock, Paper, Scissors!")
rounds = int(input("Enter the number of rounds (3 or 5): "))

# Validate number of rounds
while rounds not in [3, 5]:
    print("Invalid number of rounds. Please choose either 3 or 5.")
    rounds = int(input("Enter the number of rounds (3 or 5): "))

play_game(rounds)

play_again =input("\nDo you want to play again? (yes/no):").lower()
while play_again not in ["yes", "no"]:
    play_again = input("Invalid input. Please type 'yes' or 'no':").lower()
    
    if play_again == "no":
     print("Thanks for playing! Goodbye!")
    break
