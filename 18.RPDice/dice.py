import random

quantity_dice = 1
whice_dice = 6
extras = 1
sum_dice = 0


for die in range(quantity_dice):
    die_roll = random.randint(1, whice_dice)
    sum_dice += die_roll
    print(f"{die+1} die= {die_roll}")

