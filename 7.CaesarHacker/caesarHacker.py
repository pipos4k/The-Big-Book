# I try to use the alphabet as a list but I found a problem with index so I used it as a string instead
#* If you want uppercase letters just delete the .lower(), alphabet and message too!
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.lower()

# I use a default value for message. You can try other if you want
message = "QIIX QI FC XLI VSWI FYWLIW XSRMKLX".lower()

# Passes the message 26 times(alphabet length), changes the letters from the phrash and prints them out
for character in range(len(alphabet)):
    output_text = ""
    # Goes through the message and decrypts it
    for letter in message:
        if letter in alphabet:
            num = alphabet.find(letter) # Finds the letter
            num -= character # Decrypts the number 
            # Fix the problem if number goes under 0
            if num < 0:
                num += len(alphabet)
            # Adds the letter from alphabet to output_text
            output_text += alphabet[num]
        else:
            # Else adds just the letter without decrypt
            output_text += letter
    # Finally prints out the text 
    print((character) +1, output_text)
