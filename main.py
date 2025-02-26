import random
import os


# Run the game
def main():
    move_choices = {
        "T1": "T1",
        "T2": "T2",
        "T3": "T3",
        "M1": "M1",
        "M2": "M2",
        "M3": "M3",
        "B1": "B1",
        "B2": "B2",
        "B3": "B3",
    }

    # Print the board
    def print_board():
        os.system("cls" if os.name == "nt" else "clear")
        print(
            f"""
        {move_choices["T1"]} | {move_choices["T2"]} | {move_choices["T3"]}
        ---------
        {move_choices["M1"]} | {move_choices["M2"]} | {move_choices["M3"]}
        ---------
        {move_choices["B1"]} | {move_choices["B2"]} | {move_choices["B3"]}
        """
        )

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
