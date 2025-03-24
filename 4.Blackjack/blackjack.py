import random

# Set up the constants:
HEARTS   = chr(9829) # Character 9829 is '♥'.
DIAMONDS = chr(9830) # Character 9830 is '♦'.
SPADES   = chr(9824) # Character 9824 is '♠'.
CLUBS    = chr(9827) # Character 9827 is '♣'.
# (A list of chr codes is at https://inventwithpython.com/charactermap)
BACKSIDE = chr(35)

# compares cards
def calculate_cards(user):
    calculate_cards = 0
    if user[0][0] == "A" and user[1][0] == "A":
        calculate_cards += 21
        return calculate_cards
    for i in user:
        if i[0] == "A" or i[0] == "K" or i[0] == "Q" or i[0] == "J" or i[0] == "1":
            calculate_cards += 10
        else:
            calculate_cards += int(i[0])
    return calculate_cards

# Creates deck with 52 cards
def make_deck():
    deck = []
    for i in range(2, 11):
        for j in(HEARTS, DIAMONDS, SPADES, CLUBS):
            deck.append(f"{i} {j}")
    for characters in("J", "Q", "K", "A"):
            for j in(HEARTS, DIAMONDS, SPADES, CLUBS):
                deck.append(f"{characters} {j}")
    random.shuffle(deck)
    return deck

# Shares the cards for dealer and player as visual
def share_visual_cards(hand):
    # Makes 2 lists, one to pop the cards and other to display them on the screen
    rows = ["", "", "", ""]

    if hand == dealers_hand:
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
        if hand == dealers_hand:
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


def game():
    deck = make_deck()

    players_hand = []
    dealers_hand = []
    give_cards(2, players_hand)
    give_cards(2, dealers_hand)

    players_cards_sum = calculate_cards(players_hand)
    dealers_cards_sum = calculate_cards(dealers_hand)
    print(f"Money: {money}")
    bet = int(input("How much do you bet?"))

    print(f"DEALER: ??")
    share_visual_cards(dealers_hand)
    print(f"PLAYER: {players_cards_sum}")
    share_visual_cards(players_hand)
    print(dealers_cards_sum)

    choice = input("(H)it, (S)tand, (D)ouble down: ")

money = 5000

while money > 0:
    deck = make_deck()

    players_hand = []
    dealers_hand = []
    give_cards(2, players_hand)
    give_cards(2, dealers_hand)

    players_cards_sum = calculate_cards(players_hand)
    dealers_cards_sum = calculate_cards(dealers_hand)
    print(f"Money: {money}")
    bet = int(input("How much do you bet?"))

    print(f"DEALER: ??")
    share_visual_cards(dealers_hand)
    print(f"PLAYER: {players_cards_sum}")
    share_visual_cards(players_hand)
    print(dealers_cards_sum)

    choice = input("(H)it, (S)tand, (D)ouble down: ")

    if choice == "H":
        if players_cards_sum > 21:
            print("You overdraw")
            continue
        
        give_cards(1, players_hand)
        share_visual_cards(players_hand)

    elif choice == "S":
        print(calculate(players_cards_sum, dealers_cards_sum))

   
  
      
