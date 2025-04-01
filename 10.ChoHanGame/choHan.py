# ChoHan Game
import random, os

# Description and how to play
print('''Cho-Han,
      
In this traditional Japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess if the
dice total to an even (cho) or odd (han) number.
''')

# percentage function, Japan house keeps 10% of your wins
def percentage(whole):
  return int((10 * whole) / 100.0)

# check the user's choice
def check_the_choice(choice):
    global money
    global bet
    bet = int(bet)
    if choice == "even" and sum_dice % 2 == 0:
        money += bet*2 
        money -= percentage(bet)
        print(f"You win {bet*2}")
        print(f"The house keeps fee: {percentage(bet)}")
    elif choice == "odd" and sum_dice % 2 == 1:
        money += bet*2
        money -= percentage(bet)
        print(f"You win {bet*2}")
        print(f"The house keeps fee: {percentage(bet)}")
    else:
        money -= bet
        print(f"You lose {bet}")

# adds money var  
money = 5000

while True and money > 0:
    # creates the dice and sum them
    first_dice = random.randint(1, 6)
    second_dice = random.randint(1, 6)
    sum_dice = first_dice + second_dice

    # var, how much money user bets
    bet = (input(f"You have {money} mon. How much do you bet? (or QUIT)")).lower()
    if bet == "quit": # if choice is quit, exit the game
        break

    print('''The dealer swirls the cup and you hear the rattle of dice.
        The dealer slams the cup on the floor, still covering the
        dice and asks for your bet.''')
    
    # var, for ever/odd
    choice = "even".lower()
    check_the_choice(choice=choice)
    print(f"Your total money {money}\n")
    input("Press Enter to continue> ")
    
    os.system("clear")
