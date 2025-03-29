alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")

while True:
    direction = input("Do you want to: '(e)ncode' or '(decode)': ").lower()
    is_string = False

    while True:
        try:
            text = input("Type your message:\n").lower()
            for i in text:
                if int(i): 
                    print("You insert a number, try again.")
        except:
            is_string = True
        if is_string:
            break

    shift = int(input("Type the shift number:\n"))
    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
    again = input("Again? 'Yes' or 'No'?").lower()
    if again == "no":
        print("Thanks for playing.")
        break
