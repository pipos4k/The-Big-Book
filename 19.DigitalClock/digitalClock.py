from time import strftime, localtime, sleep
import sevseg, os

try:
    while True:
        # Create 3 variables for time, H, M, S
        hour, mins, secs = strftime("%H %M %S", localtime()).split()

        h_seg = sevseg.getSevSegStr(hour, 2).splitlines()
        m_seg = sevseg.getSevSegStr(mins, 2).splitlines()
        s_seg = sevseg.getSevSegStr(secs, 2).splitlines()

        # Define colon separators
        colons = ["   ", " * ", " * "]  # Only middle and bottom lines have asterisc

        for i in range(3):  # Each 7-segment digit block has 3 lines
            print(f"{h_seg[i]}{colons[i]}{m_seg[i]}{colons[i]}{s_seg[i]}")

        print("\nPress Ctrl+C to exit.")
        sleep(1)
        os.system("clear")
except KeyboardInterrupt:
    print("\nGoodbye.")
