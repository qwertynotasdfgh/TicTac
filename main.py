import random
import os


# Run the game
def main():
    move_choices = {
        "T1": "_",
        "T2": "_",
        "T3": "_",
        "M1": "_",
        "M2": "_",
        "M3": "_",
        "B1": "_",
        "B2": "_",
        "B3": "_",
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

    # Ask the player for their move and check if it is valid
    def player_move():
        while True:
            print_board()
            player_move = input("Your move: ").strip().lower()

            if player_move in move_choices and move_choices[player_move] == "_":
                return player_move
            else:
                print("Invalid move")

    # Get the computer's move
    def computer_move():
        while True:
            computer_move = random.choice(list(move_choices.keys()))

            if move_choices[computer_move] == "_":
                return computer_move


# Ask player if they want to play the game
print("Would you like to play tik-tac-toe?")
response = input("Y/N: ")

# If the player says yes run the game, end the program if they say no
if response.lower() == "y":
    main()
else:
    print("Ending Program...")
