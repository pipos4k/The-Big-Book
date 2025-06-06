import random

# Set up the constants:
HEARTS   = chr(9829) # Character 9829 is '♥'.
DIAMONDS = chr(9830) # Character 9830 is '♦'.
SPADES   = chr(9824) # Character 9824 is '♠'.
CLUBS    = chr(9827) # Character 9827 is '♣'.
# (A list of chr codes is at https://inventwithpython.com/charactermap)
BACKSIDE = chr(35)

# Compares cards
def compare_cards(user):
    calculate_cards = 0
    a_count = 0

    for i in range(len(user)):
        if user[0][0] == "A" and user[1][0] == "A" and len(user) == 2:
            calculate_cards = 21
            return calculate_cards
        if user[i][0] == "A":
            calculate_cards += 11
            a_count +=1
        elif user[i][0] in {"J", "Q", "K"}:
            calculate_cards += 10
        elif user[i][0] == "1" and user[i][1] == "0":
            calculate_cards += 10
        else:
            calculate_cards += int(user[i][0])
            
    while calculate_cards > 21 and a_count > 0:
        calculate_cards -= 10
        a_count -= 1 
    return calculate_cards

# Creates deck with 52 cards
def make_deck():
    deck = []
    for i in range(2, 11):
        for j in(HEARTS, DIAMONDS, SPADES, CLUBS):
            deck.append(f"{i} {j}")
    for characters in("J", "Q", "K","A"): #"J", "Q", "K", 
        for j in(HEARTS, DIAMONDS, SPADES, CLUBS):
            deck.append(f"{characters} {j}")
    random.shuffle(deck)
    return deck

# Shares the cards for dealer and player as visual
def share_visual_cards(hand):
    # Makes 2 lists, one to pop the cards and other to display them on the screen
    global choice
    rows = ["", "", "", ""]

    if hand == dealers_hand and choice != "s" and choice != "d":
        for i in range(1):
            rows[1] += (f"|{BACKSIDE}  |")
            rows[2] += (f"| {BACKSIDE} |")
            rows[3] += (f"|__{BACKSIDE}|")

    for line in range(len(hand)): # Makes the visual and put them on rows list
        rows[0] += (" ___ ")
        for i in range(1):
            if hand[line][0] == "1":
                rows[1] += (f"|{hand[line][0]}{hand[line][1]} |")
                rows[2] += (f"| {hand[line][3]} |")
                rows[3] += (f"|_{hand[line][0]}{hand[line][1]}|")
            else:
                rows[1] += (f"|{hand[line][0]}  |")
                rows[2] += (f"| {hand[line][2]} |")
                rows[3] += (f"|__{hand[line][0]}|")
        if hand == dealers_hand and choice != "s" and choice != "d":
            break

    for row in rows: # Prints them to monitor
        print(row)

# Gives cards
def give_cards(quantity, user_hand):
    for i in range(quantity):
        card = deck.pop()
        user_hand.append(card)
    
# Calculate cards
def calculate(player, dealer):
    result = ""
    global bet, money

    if player > 21:
        result = (f"You lost {bet}!\n")
        money -= bet
    elif dealer == player:
        result = "It's a tie\n"
        # money += bet
    elif dealer > player and dealer < 22:
        result = (F"You lost {bet}!\n")
        money -= bet
    else:
        result = (f"You win {bet*2}\n")
        money += bet*2

    return result

# Coins to play
money = 5000
while money > 0:
    deck = make_deck()
    choice = ""

    # Creates 2 decks and shares cards
    players_hand = []
    dealers_hand = []
    give_cards(2, players_hand)
    give_cards(2, dealers_hand)

    
    # Checks if player and dealer have double "A" and calculates the cards
    players_cards_sum = compare_cards(players_hand)
    dealers_cards_sum = compare_cards(dealers_hand)

    print(f"Money: {money}$")
    while True:
        try:
            bet = int(input("How much do you bet> ")) # bet input
            if bet > money or bet < 1:
                NError = ValueError("You must bet between your money.")
                print(NError)
                continue
            if isinstance(bet, int):
                break
        except ValueError:
            print(ValueError("You insert an invalid input."))
        
    # while loop until player wins or loses
    while players_cards_sum < 22:
        # Shows cards for dealer and player
        print(f"DEALER: ?? {dealers_cards_sum}")
        share_visual_cards(dealers_hand)
        print("\n")
        print(f"PLAYER: {players_cards_sum}")
        share_visual_cards(players_hand)
        
        # Takes player's choice 
        if len(players_hand) == 2:
            choice = input("(H)it, (S)tand, (D)ouble down. >").lower()
        else:
            choice = input("(H)it, (S)tand. >").lower()
            
        if choice == "h":
            give_cards(1, players_hand)
            share_visual_cards(players_hand)
            players_cards_sum = compare_cards(players_hand)

            if players_cards_sum > 21:
                print(f"You overdraw and lost {bet}")
                money -= bet
                break
            
 
        elif choice == "s":
            print("\n" * 4)
            while dealers_cards_sum < 17:
                give_cards(1, dealers_hand)
                dealers_cards_sum = compare_cards(dealers_hand)
            print(f"DEALER: {dealers_cards_sum}")
            share_visual_cards(dealers_hand)
            print(f"PLAYER: {players_cards_sum}")
            share_visual_cards(players_hand)
            print(calculate(players_cards_sum, dealers_cards_sum))
            break

        elif choice == "d":
            while True:
                try:
                    double_bet = int(input(f"How much do you bet> 1 - {bet} > ")) # bet input
                    if double_bet > bet or double_bet < 1:
                        NError = ValueError("You must bet between your money.")
                        print(NError)
                        continue
                    if isinstance(double_bet, int):
                        break
                except ValueError:
                    print(ValueError("You insert an invalid input."))

            bet += double_bet
            give_cards(1, players_hand)
            players_cards_sum = compare_cards(players_hand)

            while dealers_cards_sum < 17:
                give_cards(1, dealers_hand)
                dealers_cards_sum = compare_cards(dealers_hand)

            print(f"DEALER: {dealers_cards_sum}")
            share_visual_cards(dealers_hand)
            print(f"PLAYER: {players_cards_sum}")
            share_visual_cards(players_hand)
            print(calculate(players_cards_sum, dealers_cards_sum))
            break
    
    if money < 1:
        print("You went bankrupt!!")
        break

    # Checks if player want to play again

    while True:
        play_again = input("Play again? y or n > ")
        if play_again == "n":
            print(f"You leave with: {money}$")
            print("Thanks for playing.")
            quit()
        elif play_again == "y":
            break
        else:
            print("You insert an invalid input.")
    
    print("\n" * 4)
