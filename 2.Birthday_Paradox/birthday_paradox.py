import random
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

day = generate_day(quantity=int(input("How many birthdays shall I generate? (Max 100)\n")))

day.sort()
counter = 0

for i in range(len(day)):
    print(f"{day[i][1][:3]} {day[i][0]}", end=", ")
    # print(i)
    if day[i] == day[i-1]:
        print("True")
        counter +=1

print("\n")
print(f"We find {counter} same days.")