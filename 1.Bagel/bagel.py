import random

# Creates 1 random numbers convert them to str, for each variable 
x, y, z = str(random.randint(0, 9)), str(random.randint(0, 9)), str(random.randint(0, 9))
code = [x, y, z]
print(code)

guess = input("Enter 3 numbers: ")


def check(script, password):
    answers = []
    for i in range(len(script)):
        if script[i] == password[i]:
            answers.append("Fermi")
            break
        elif script[i] in password:
            answers.append("Pico")
            continue
        if len(answers) == 0:
            answers = "Bagel"

    return(answers)

answer = check(guess, code)

print(f"{answer}")



