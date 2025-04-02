# Collatz Sequence
print("Collatz Sequence, or, the 3n + 1 Problem\n")

# Checks if input is either a positive number or the string 'quit'
while True:
    number = input("Enter a starting number (greater than 0) or QUIT:").lower()
    if number == "quit":
        print("Thanks for playing.")
        exit()
    if not number.isdecimal():
        print("You inserted a non numeric value.")
    else:
        number = int(number)
        break

# Counts down the number until it reaches 1.
while number > 0:
    print(number, end=" ")
    if number == 1:
        input("\nDone.")
        break

    number = number // 2 if number % 2 == 0 else number * 3 + 1
