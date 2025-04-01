# Carrot in a Box
import random, os

# How to play the game
print('''Carrot in a Box, by Al Sweigart al@inventwithpython.com
      
This is a bluffing game for two human players. Each player has a box.
One box has a carrot in it. To win, you must have the box with the
carrot in it.

This is a very simple and silly game.

The first player looks into their box (the second player must close
their eyes during this.) The first player then says "There is a carrot
in my box" or "There is not a carrot in my box". The second player then
gets to decide if they want to swap boxes or not.
''')

input("Press Enter to start")
# Names of users
first_user = input("First player. Enter your name: ")
second_user = input("Second player. Enter your name: ")

# Format the names' display with boxes
playerNames = first_user[:11].center(11) + '    ' + second_user[:11].center(11)

print('''HERE ARE TWO BOXES:
  __________     __________
 /         /|   /         /|
+---------+ |  +---------+ |
|   RED   | |  |   GOLD  | |
|   BOX   | /  |   BOX   | /
+---------+/   +---------+/''')
print(playerNames + "\n")

print(f"{first_user} you have the Red box.")
print(f"{second_user} you have the Gold box.\n")
input(f'''{first_user}, you will see into your box.
{second_user}, close your eyes!!
When {second_user} has closed their eyes, press Enter>
''')

# red_box variable with randint for carrot
red_box = "carrot!!!" if random.randint(1, 2) == 1 else "no carrot"
print(f"{first_user}, here is your box! Look!")
print(f'''
   ___VV____
  |   VV    |
  |   VV    |
  |___||____|    __________
 /    ||   /|   /         /|
+---------+ |  +---------+ |
|   RED   | |  |   GOLD  | |
|   BOX   | /  |   BOX   | /
+---------+/   +---------+/
 {red_box}''')
input("Press enter to contintue>")

print(f"{first_user}, tell {second_user} to open their eyes.")
input("Press enter to contintue>")

# Clear the screen 
os.system("clear")

print(f'''
{first_user} say one of the following sentences to {second_user}.
  1) There is a carrot in my box.
  2) There is not a carrot in my box.''')
input("Press enter to contintue>")

# choice variable, asks second user to keep the box
choice = input(f"{second_user} do you want to swap boxes with {first_user}? YES/NO").lower()

# prints out the results and the winner
print("Here are the boxes:")
if red_box == "carrot!!!":
    print(f'''
   ___VV____      _________
  |   VV    |    |         |
  |   VV    |    |         |
  |___||____|    |_________|
 /    ||   /|   /         /|
+---------+ |  +---------+ |
|         | |  |         | |
|   BOX   | /  |   BOX   | /
+---------+/   +---------+/
 {red_box}''')
else:
    print(f'''
   _________      ___VV____
  |         |    |   VV    |
  |         |    |   VV    |
  |_________|    |___||____|
 /         /|   /    ||   /|
+---------+ |  +---------+ |
|         | |  |         | |
|   BOX   | /  |   BOX   | /
+---------+/   +---------+/
                carrot!!''')
    
if choice == "no" and red_box == "no carrot":
    print(f"{second_user} your have faith on your box! You win!")
else:
    print(f"{first_user} You have a good persuation! You win!!")
