# Calendar Maker
import calendar

# Takes from user the year and month and split them to make a list
choice = input("Choose a year and a month> 'e.g. 2025 4' >").split(" ")

# Creates the calendar 
cal = calendar.TextCalendar()
result = cal.formatmonth(int(choice[0]), int(choice[1]))

# Creates a variable for txt format.
file_name = f"Calendar_{choice[0]}_{choice[1]}.txt"

# Saves the calendar
with open(file_name, "w") as file:
    file.write(result)

print(f"Calendar saved as {file_name}")
