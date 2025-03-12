import random

MAX_ATTEMPS = 10
numbers_ = list("0123456789")
random.shuffle(numbers_)
code = ""
for i in range(0, 3):
    code += str(numbers_[i])

print(code)
print('''Welcome to Bagel game. Im gonna think a number and you should find it.\nGood luck!
Here are some tips for the game:
Fermi means: Right place, right number.
Pico means: Wrong place, right number.
Bagel means: Nothing is correct.'''
)

def check(script, password):
    answers = []

    if script == password:
        return "You got it!!"

    for i in range(len(script)):
        if script[i] == password[i]:
            answers.append("Fermi")
        elif script[i] in password:
            answers.append("Pico")
        if len(answers) == 0:
            answers = "Bagel"
    return(answers)


while MAX_ATTEMPS > 0:
    guess = input("Enter 3 numbers: ")

    answer = check(guess, code)
    
    MAX_ATTEMPS -= 1
    print(f"{answer}")
    print(f"You have {MAX_ATTEMPS} attemps.")

if MAX_ATTEMPS == 0:
    print("You lose.")

