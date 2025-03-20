import random

# Set up the constants:
HEARTS   = chr(9829) # Character 9829 is '♥'.
DIAMONDS = chr(9830) # Character 9830 is '♦'.
SPADES   = chr(9824) # Character 9824 is '♠'.
CLUBS    = chr(9827) # Character 9827 is '♣'.
# (A list of chr codes is at https://inventwithpython.com/charactermap)
BACKSIDE = 'backside'

# todo bets/double down/stand
# todo win/lose/draw
# todo compare cards 

# Makes the deck with 52 cards
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

# Shares the cards for dealer and player
def share_cards(hand):
    # Makes 2 lists, one to pop the cards and other to display them on the screen
    rows = ["", "", "", ""]
   
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

    for row in rows: # Prints them to monitor
        print(row)

deck = make_deck()

# Gives cards to player
players_hand = []
for i in range(2): 
    card = deck.pop()
    players_hand.append(card)

# Gives cards to dealer
dealers_hand = []
for i in range(2): 
    card = deck.pop()
    dealers_hand.append(card)


share_cards(players_hand)
share_cards(dealers_hand)

