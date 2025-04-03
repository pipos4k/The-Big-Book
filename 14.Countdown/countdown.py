# Countdown
import time, sevseg, os

# function for countdown
def countdown(t): 
    # try, checks if user press ctrl+c
    try:
        while t:
            mins, secs = divmod(t, 60)
            hours, mins = divmod(mins, 60) # divide number of minutes by 60 to get hours
            days, hours = divmod(hours, 24) # divide number of hours by 24 to get days
            timer = "{:02d}.{:02d}.{:02d}".format(hours, mins, secs) 
            # print the time with sevseg module
            print(sevseg.getSevSegStr(timer), end="") 
            print("\nPress ctrl+C to Exit.")
            # sleep the bash and clear the screen
            time.sleep(1) 
            os.system("clear")
            t -= 1

            if t == 0:
                print("DONE!!!")

    except KeyboardInterrupt:
        print("\nCountdown.\nGood bye.")

while True:
    # checks if user's input is numeric
    t = input("How many seconds do you want to count?")
    if not t.isnumeric():
        print("You inserted a non numeric value.")
    else:
        t = int(t)
        break

countdown(int(t))
