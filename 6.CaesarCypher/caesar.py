# Adds the alphabet as a list
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Makes a function that takes a the text, shift amount, and what user wants to do.
def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    # If decode, multiply with -1 to go backwards in the list
    if encode_or_decode == "decode":
        shift_amount *= -1

    # Checks which one letters are in the text
    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
        else:
            # with shift option jumps to the right letter
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")

while True:
    # Takes the value for encode/decode 
    direction = input("Do you want to: '(e)ncode' or '(decode)': ").lower()
    # Takes the text from user
    text = input("Type your message:\n").lower()
    # Takes the shift amount from user
    shift = int(input("Type the shift number:\n"))
    # Calls the functions and returns the result
    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
    # Asks the user if wants to do it again
    again = input("Again? 'Yes' or 'No'?").lower()
    if again == "no":
        print("Thanks for playing.")
        break
