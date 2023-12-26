## Description:
This program is very good for practicing coding with the lovely Python language 💞 because you can become more proficient and interested in Python after you finish playing the program you wrote while enjoying the game.😉
## Instructions:
The game starts with the word `start` In the first stage, the user's position is displayed, and he can reach the door by moving towards the directions.
If he reaches it, he wins 🎆 and if he hits the monster, he loses 😭 At the end, he exits the game by writing the word `QUIT`
```python
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
```
It is so that if your operating system 💻 is Windows and it is `nt` type, the user's page will be cleaned with `cls` command. For others, the page will be cleaned with `clear` command.
```python
def get_location():
    return random.sample(CELLS, 3)
```
It is to randomly select 3 positions from the cells for the door 🚪 and the position of the user 😊 and the monster 🐲
```python
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
```
It is for the user to move towards the directions by writing the words right👉  left👈  up👆  down👇
```python
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
```
It is to prevent the movement bug, for example, if the user reaches the lowest cell, he will not go down again because there is no cell.
```python
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
```
It is for making the coordinate table of the game 👷‍♀️
```python
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
```
 related to the start of the user's game 🎮
 ## Fix and update:
 Currently, there are no planned changes in the game project, however, I welcome any kind of criticism and suggestions to improve the program or fix the game's problems, and thank you in advance, dear friend 🙏 🥰
 ## Author :
 Maryam Jamali 🫶

