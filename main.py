import random
import os


# Run the game
def main():

    # Set up the game board
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
    # Game ending conditoins
    # Full boad condition
    spaces_available = 9
    if spaces_available == 0:
        print("Game Over")
        return
    # Winning conditions
    winning_conditions = [
        ["T1", "T2", "T3"],
        ["M1", "M2", "M3"],
        ["B1", "B2", "B3"],
        ["T1", "M1", "B1"],
        ["T2", "M2", "B2"],
        ["T3", "M3", "B3"],
        ["T1", "M2", "B3"],
        ["T3", "M2", "B1"],
    ]

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
                spaces_available -= 1
                return player_move
            else:
                print("Invalid move")

    # Get the computer's move
    def computer_move():
        while True:
            computer_move = random.choice(list(move_choices.keys()))

            if move_choices[computer_move] == "_":
                spaces_available -= 1
                return computer_move


# Ask player if they want to play the game
print("Would you like to play tik-tac-toe?")
response = input("Y/N: ")

# If the player says yes run the game, end the program if they say no
if response.lower() == "y":
    main()
else:
    print("Ending Program...")
