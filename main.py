import random


# Run the game
def main():
    move_choices = ["T1", "T2", "T3", "M1", "M2", "M3", "B1", "B2", "B3"]

    # Print the board
    print("T1 | T2 | T3")
    print("-----------")
    print("M1 | M2 | M3")
    print("-----------")
    print("B1 | B2 | B3")

    # Ask the player for their move
    while True:
        player_move = input("Your move: ").strip().upper()
        computer_move = random.choice(move_choices)
        if player_move in move_choices:
            print("Valid move")
        else:
            print("Invalid move")
            continue


# Ask player if they want to play the game
print("Would you like to play tik-tac-toe?")
response = input("Y/N: ")

# If the player says yes run the game, end the program if they say no
if response.lower() == "y":
    main()
else:
    print("Ending Program...")
