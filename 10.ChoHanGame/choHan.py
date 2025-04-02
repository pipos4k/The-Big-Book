# ChoHan Game
import random, os

# Description and how to play
print('''Cho-Han,
      
In this traditional Japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess if the
dice total to an even (cho) or odd (han) number.
''')
input("Press Enter to continue.")

# percentage function, Japan house keeps 10% of your wins
def percentage(whole):
  return int((10 * whole) / 100.0)

# check the user's choice
def check_the_choice(choice):
    global money
    global bet
    bet = int(bet)
    if (choice == "cho" and sum_dice % 2 == 0) or (choice == "han" and sum_dice % 2 == 1):
        money += bet*2 
        money -= percentage(bet)
        print(f"You win {bet*2}¥")
        print(f"The house keeps fee: {percentage(bet)}¥")
    else:
        money -= bet
        print(f"You lose {bet}¥")

# adds money var  
money = 5000
# Adds the japanase numbers
japan_nums = {1: 'ICHI', 2: 'NI', 3: 'SAN', 4: 'SHI', 5: 'GO', 6: 'ROKU'}

# checks money and if player wants to keep playing
while True and money > 0:
    # creates the dice and sum them
    first_dice = random.randint(1, 6)
    second_dice = random.randint(1, 6)
    sum_dice = first_dice + second_dice

    print('''The dealer swirls the cup and you hear the rattle of dice.
        The dealer slams the cup on the floor, still covering the
        dice and asks for your bet.''')
    
    # var, how much money user bets and checks for problems
    while True:
        bet = input(f"You have {money} mon. How much do you bet? (or QUIT)")
        if bet == "quit": # if choice is quit, exit the game
            print("Thanks for playing.")
            exit()
        elif not bet.isdecimal():
            print("Please enter a number.")
        elif int(bet) > money or int(bet) < 1:
            print("Please insert a value you have.")
        else:
            bet = int(bet)
            break

    # var, for ever/odd and checks for problems
    while True:
        choice = input("CHO (even) or HAN (odd)?").lower()
        if choice != "cho" and choice != "han":
            print("Please insert 'CHO' for even, or 'HAN' for odd.")
            continue
        else:
            break

    # Prints out the dice, sum, and results 
    print(f"The dealer lifts the cup to reveal:\n {japan_nums[first_dice]}-{first_dice} | {japan_nums[second_dice]}-{second_dice}")
    print(f"Total sum: {sum_dice}\n")
    check_the_choice(choice=choice)
    print(f"Your total money {money}\n")
    input("Press Enter to continue> ")
    
    os.system("clear")
