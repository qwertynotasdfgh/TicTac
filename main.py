import random


def main():
    pass


# Ask player if they want to play the game
print("Would you like to play tik-tac-toe?")
response = input("Y/N: ")

# If the player says yes run the game, end the program if they say no
if response.lower() == "y":
    main()
else:
    print("Ending Program...")
