import random
from datetime import datetime
import calendar

def generate_day(quantity):
    months = []

    for i in range(quantity):
        month_ = calendar.month_name[random.randint(1, 12)]
        months_30 = ['4', '6', '9', '11']

        if month_ in months_30:
            day_ = str(random.randint(1, 30))
        elif month_ == 2:
            day_ = str(random.randint(1, 29))
        else:
            day_ = str(random.randint(1, 31))

        birthday = [day_, month_]
        months.append(birthday)

    return months

day = generate_day(quantity=int(input("How many birthdays shall I generate? (Max 100)")))

print(day)