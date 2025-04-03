import random, time
# Cave's max width 
maxWIDTH = 36

# print until user press ctrl+c the cave
print("ctrl+C for EXIT!")
while True:
    # random value for left wall
    lWIDTH = random.randint(11, 14)
    gap = " " * 8 # gap between walls
    # calculates the right wall 
    rWIDTH = (maxWIDTH - 8 - lWIDTH)

    try: 
        # prints out #
        print("#" * lWIDTH, end="")
        print(gap, end="")
        print("#" * rWIDTH)
        time.sleep(0.3)
    except KeyboardInterrupt:
        print("Deep Cave, Thanks for playing.")
        break
