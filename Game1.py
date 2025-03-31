import random

def get_winner(player, computer):
    """Determines the winner based on the rules"""
    if player == computer:
        return "It's a draw!"
    elif (player == "snake" and computer == "water") or \
         (player == "water" and computer == "gun") or \
         (player == "gun" and computer == "snake"):
        return "You win"
    else:
        return "Computer wins"

# Options available
options = ["snake", "water", "gun"]

# Score
player_score = 0
computer_score = 0

# Game loop
print("------------------Game----------------")
while True:
    print("\nChoose: Snake, Water, or Gun (or exit)")
    player_choice = input("Your choice: ").strip().lower()

    if player_choice == "exit":
        print("Final Scores: \nYou =", player_score, ",\nComputer =", computer_score)
        print("Thanks for playing!")
        break
    
    if player_choice not in options:
        print("Invalid choice! Please enter Snake, Water, or Gun.")
        continue

    # Computer choice
    computer_choice = random.choice(options)
    print(f"Computer chose: {computer_choice}")

    # Determine winner
    result = get_winner(player_choice, computer_choice)
    print(result)

    # Update scores
    if "You win" in result:
        player_score += 1
    elif "Computer wins" in result:
        computer_score += 1
