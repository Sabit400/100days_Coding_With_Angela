import string

LETTERS_ALPHABET = list(string.ascii_lowercase)
NUMBERS_ALPHABET = list(string.digits)

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char.isalpha():
            alphabet = LETTERS_ALPHABET
        elif char.isdigit():
            alphabet = NUMBERS_ALPHABET
        else:
            end_text += char
            continue
        position = alphabet.index(char)
        new_position = (position + shift_amount) % len(alphabet)
        end_text += alphabet[new_position]
    print(f"Here's the {cipher_direction}d result: {end_text}")

from art import logo
print(logo)

should_end = False
while not should_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input(f"Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Goodbye")
