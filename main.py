# TODO-1: Import and print the logo from art.py when the program starts.
import art
print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""

    if encode_or_decode == "decode":
        shift_amount *= -1

    # if a part of the original_text doesn't exist in the alphabet list
    # then make sure to keep them and in its position.
    for letter in original_text:
        # TODO-2: What happens if the user enters a number/symbol/space?
        # then add it to the output_text without shifting it.
        if letter not in alphabet:
            output_text += letter
        # if the letter is in the alphabet list, then shift it by the shift_amount
        # and add it to the output_text.
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")


# TODO-3: Can you figure out a way to restart the cipher program?
# should_continue = True is used to keep the program running until the user types 'no'.
should_continue = True

# using while loop
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    restart = input("Type 'yes' if you want to go again.  Otherwise, type 'no'. \n").lower()
    if restart == 'no':
        should_continue=False
        print("Goodbye")



