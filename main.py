import random
import os


# Run the game
def main():

    # Set up the possible moves
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
    # Full board condition
    spaces_available = 9
    if spaces_available == 0:
        print("Game Over")
        return
    # Winning condition
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

    # Set up players
    player = "X"
    computer = "O"

    # Check for a win condition
    def check_win(player):
        for condition in winning_conditions:
            if all(move_choices[move] == player for move in condition):
                print_board()
                print(f"{player} wins!")
                return True
        return False

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
        global spaces_available
        while True:
            print_board()
            player_move = input("Your move: ").strip().lower()

            if player_move in move_choices and move_choices[player_move] == "_":
                move_choices[player_move] = player
                check_win(player)
                spaces_available -= 1
                return player_move
            else:
                print("Invalid move")

    # Get the computer's move
    def computer_move():
        global spaces_available
        available_moves = [pos for pos, val in move_choices.items() if val == "_"]

        if available_moves:
            computer_move = random.choice(available_moves)
            move_choices[computer_move] = computer
            check_win(computer)
            spaces_available -= 1
            return computer_move


# Ask player if they want to play the game
print("Would you like to play tik-tac-toe?")
response = input("Y/N: ")

# If the player says yes run the game, end the program if they say no
if response.lower() == "y":
    print("You play by entering the location of your move")
    print("Type 'T' for top, 'M' for middle, 'B' for bottom")
    print("Type '1' for the left, '2' for the middle, '3' for the right")
    print("For example, 'T1' would be the top left")
    main()
else:
    print("Ending Program...")
