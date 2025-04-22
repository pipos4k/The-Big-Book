import random

again = True
while again:
    final_dice_list = []
    while True:
        try: 
            quantity_dice = input("How many dice: ")
            type_dice = input("What type of die: ")
            extras = input("Extras: ")

            if quantity_dice.isdecimal and type_dice.isdecimal and extras.isdecimal:
                quantity_dice = int(quantity_dice)
                type_dice = int(type_dice)
                extras = int(extras)
                break

        except:
            print("Some of your value was not a numeric.")

    for die in range(quantity_dice):
        die_roll = random.randint(1, type_dice)
        final_dice_list.append(die_roll)

    print("\n")
    print(f"Total: {sum(final_dice_list) + extras}, Each die: {final_dice_list} Extra: {f'+{extras}' if extras > 0 else extras})")
    
    check_again = input("Want to roll again> (QUIT or EXIT) ").lower()
    if check_again == "quit" or check_again == "exit":
        print("Thanks for rollings!!")
        again = False
    else:
        continue
    