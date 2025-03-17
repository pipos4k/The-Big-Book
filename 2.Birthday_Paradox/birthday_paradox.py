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

def calculates_thousand(the_day):
    global counter
    for i in range(len(the_day)):
        if the_day[i] == the_day[i-1]:
            counter +=1
            return

people = int(input("How many birthdays shall I generate? (Max 100)\n"))

while people > 100 or people < 1:
    print("You entered an invalid number\nPlease insert something between 1 and 100.")
    people = int(input())
    continue

day = generate_day(quantity=people)
day.sort()
counter = 0

print(f"Here are {people} birthdays:\n")
for i in range(len(day)):
    print(f"{day[i][1][:3]} {day[i][0]}", end=", ")
    if day[i] == day[i-1]:
        counter +=1

print(f"\nWe find {counter} same days.")

print(f"\nLets generate 100000 times, 23 random birthdays:")
input()
for i in range(100000):
    ejento_day = generate_day(people)
    ejento_day.sort()
    calculates_thousand(ejento_day)

percentage = (counter / 100000) * 100

print(f"Out of 100,000 simulations of {people} people, there was a matching birthday in that group {counter} times.")
print(f"So we have {percentage:.2f}% chance for {people} people.")
