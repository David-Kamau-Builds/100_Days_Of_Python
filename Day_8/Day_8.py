import art

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    
    # Adjust the shift to be within the bounds of the alphabet length
    shift_amount %= len(alphabet)

    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:

        # Check if the character is in the alphabet
        if letter not in alphabet:
            output_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount

            # The modulo operation handles wrapping around the alphabet
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]

    print(f"Here is the {encode_or_decode}d result: {output_text}")


should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()

    # Get the shift modulo 26 early to handle large numbers
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    restart = input("Type 'yes' if you want to try again and 'no' if not.\n").lower()

    if restart == "no":
        should_continue = False
        print("Goodbye, Cypher")