# This is a bitmap, that will print in the screen.
bitmap = """
....................................................................
   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   **        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                 ********        *************    *  ** ***
                   ********         ********          * *** ****
                   *********         ******  *        **** ** * **
                   *********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    *
                    **     *                    *
.................................................................... """

# Splits bitmap 
splitmap = bitmap.splitlines()
word = input("Say the line for our bitmap: ")

# Loops through splitmap
for line in splitmap:
    # Loops to every single enumarate line
    for i, letter in enumerate(line):
        if letter == " ": # Checks for empty space and prints " " 
            print(" ", end=" ")
        else: # if not prints the word from the input
            print(word[i % len(word)], end=" ")
    print() # print a new line
