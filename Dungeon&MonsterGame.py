import random
import os

# draw grid
# When it is written with a capital letter,
# it means that the variable is fixed. it is better not to change
CELLS = [
    (0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
    (0, 1), (1, 1), (2, 1), (3, 1), (4, 1),
    (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
    (0, 3), (1, 3), (2, 3), (3, 3), (4, 3),
    (0, 4), (1, 4), (2, 4), (3, 4), (4, 4)
]


# If the operating system was Windows, it was of "NT" type; Use the "CLS" command...
# If it was something else, use the "CLEAR" command
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# Randomly select 3 cells
def get_location():
    return random.sample(CELLS, 3)


# get the player's location
def move_player(player, move):
    x, y = player

    if move == "LEFT":
        x -= 1
    if move == "RIGHT":
        x += 1
    if move == "UP":
        y -= 1
    if move == "DOWN":
        y += 1

    return x, y


def get_move(player):
    moves = ["LEFT", "RIGHT", "UP", "DOWN"]
    x, y = player
    if x == 0:
        moves.remove("LEFT")
    if x == 0:
        moves.remove("RIGHT")
    if x == 0:
        moves.remove("UP")
    if x == 0:
        moves.remove("DOWN")

    return moves


# Draw a map
def draw_map(player):
    print(" _" * 5)
    tile = "|{}"
    for cell in CELLS:
        x, y = cell
        if x < 4:
            line_end = ""
            if cell == player:
                output = tile.format("x")
            else:
                output = tile.format("_")
        else:
            line_end = "\n"
            if cell == player:
                output = tile.format("x|")
            else:
                output = tile.format("_|")
        print(output, end=line_end)


def game_loop():
    # Giving location to three variables
    monster, door, player = get_location()
    playing = True
    while playing:
        clear_screen()
        draw_map(player)
        valid_moves = get_move(player)
        print("you're currently in room {}".format(player))  # fill with player position
        print("you can move {}".format(", ".join(valid_moves)))  # fill with available moves
        print("enter 'QUIT' to quit.")

        move = input("----> ")
        move = move.upper()

        if move == 'QUIT':
            break

        # move player, unless invalid move (past edges of grid)
        if move in valid_moves:
            player = move_player(player, move)

            # Winner and loser
            if player == monster:
                print("\n ** OH NO! the monster got you! Better luck next time! ** \n")
                playing = False
            if player == door:
                print("\n ** You scape! congratulation general ** \n")
                playing = False
        else:
            input("\n ** Walls are hard! Don't run into them! ** \n")
    else:
        if input("play again? [Y/n]").lower() != "n":
            game_loop()


# Clears the player screen
clear_screen()
print("welcome to the DUNGEON!")
input("press 'return' to start!")
clear_screen()
game_loop()

# Name of the programmer: Maryam Jamali
# Email address: m.jamali16@yahoo.com
# GitHub address: https://github.com/MaryaJamali
