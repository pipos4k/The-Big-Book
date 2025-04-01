import random
import re

pattern = r"\d{3}"

print('''Welcome to Bagel game. Im gonna think a number and you should find it.\nGood luck!
Here are some tips for the game:
Fermi means: Right place, right number.
Pico means: Wrong place, right number.
Bagel means: Nothing is correct.'''
)

def generate_number():
    # * Generator number, convert it to str
    numbers_ = list("0123456789")
    random.shuffle(numbers_)
    code = ""   
    for i in range(0, 3):
        code += str(numbers_[i])

    return code

def check(user_guess, password):
    # * Checks the code with user's guess and returns the answer
    answers = []
    for i in range(len(user_guess)):
        if user_guess[i] == password[i]:
            answers.append("Fermi")
        elif user_guess[i] in password:
            answers.append("Pico")
        else:
            continue

        if len(answers) == 0:
            return "Bagel"

    return " ".join(answers)

def game():
    MAX_ATTEMPS = 10
    code = generate_number()

    while MAX_ATTEMPS > 0:
        guess = input("Enter 3 numbers: ")

        if not re.fullmatch(pattern, guess):
            print("Your input is not correct. Try again:")
            continue
        if guess == code:
            print("You got it!!")
            break

        answer = check(guess, code)
        MAX_ATTEMPS -= 1
        print(f"{answer}")
        print(f"You have {MAX_ATTEMPS} attemps.")
    
    if MAX_ATTEMPS == 0:
        print("You lose.")

stop = True 
while stop:
    game()
    answer = input("Keep playing? yes or no? \n")
    if answer == "yes":
        continue
    else:
        print("Good bye!")
        stop = False
        