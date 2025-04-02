# Click Bait Headline Generator
import random
from string import Template

# insert our constants
OBJECT_PRONOUNS = ['Her', 'Him', 'Them']
POSSESIVE_PRONOUNS = ['Her', 'His', 'Their']
PERSONAL_PRONOUNS = ['She', 'He', 'They']
STATES = ['California', 'Texas', 'Florida', 'New York', 'Pennsylvania',
          'Illinois', 'Ohio', 'Georgia', 'North Carolina', 'Michigan']
NOUNS = ['Athlete', 'Clown', 'Shovel', 'Paleo Diet', 'Doctor', 'Parent',
         'Cat', 'Dog', 'Chicken', 'Robot', 'Video Game', 'Avocado',
         'Plastic Straw','Serial Killer', 'Telephone Psychic']
PLACES = ['House', 'Attic', 'Bank Deposit Box', 'School', 'Basement',
          'Workplace', 'Donut Shop', 'Apocalypse Bunker']
WHEN = ['Soon', 'This Year', 'Later Today', 'RIGHT NOW', 'Next Week']

# Creates a list of headlines as templates
sentences = [
    Template("Are Millenials Killing the $nouns Industry?"),
    Template("Without This $nouns, $nouns2 Could Kill You $when"),
    Template("Big Companies Hate $objnouns! See How This $state $nouns Invented a Cheaper $nouns2"),
    Template("You Won\'t Believe What This $state $nouns Found in $possnoun $place"),
    Template("What $plurnoun Don\'t Want You To Know About $plurnoun2"),
    Template("$number Gift Ideas to Give Your $nouns From $state"),
    Template("$number Reasons Why $plurnoun Are More Interesting Than You Think (Number $number2 Will Surprise You!)"),
]

print("Our website needs to trick people into looking at ads!")
# Checks if user inputs a numeric value
while True:
    number_of_headlines = input("Enter the number of clickbait headlines to generate:")
    if not number_of_headlines.isdecimal():
        print("You inserted a non numeric value.")
    else:
        number_of_headlines = int(number_of_headlines) # convert number to int
        break

# Prints out randomly headlines 
for i in range(number_of_headlines):
    sentece = (random.choice(sentences))
    print(sentece.substitute(
        objnouns = random.choice(OBJECT_PRONOUNS),
        possnoun = random.choice(POSSESIVE_PRONOUNS),
        persnoun = random.choice(PERSONAL_PRONOUNS),
        state = random.choice(STATES),
        nouns = random.choice(NOUNS),
        nouns2 = random.choice(NOUNS),
        plurnoun = random.choice(NOUNS) + 's',
        plurnoun2 = random.choice(NOUNS) + 's',
        place = random.choice(PLACES),
        when = random.choice(WHEN),
        number = random.randint(8, 23),
        number2 = random.randint(2, 7),
))