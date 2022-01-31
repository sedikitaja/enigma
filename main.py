from rotors import Rotor, Reflector, rotator, ROTOR_DETAILS, ALPHABET
from plugboard import plugboard


def encode_letter(pin_in: str, rotor):
    """Takes the input and outputs the corresponding letter from current rotor"""
    pin_in_index = ALPHABET.index(pin_in)
    offset = rotor.position
    # pin_out = rotor.pin_sequence[((pin_in_index + offset) + 26) % 26]
    pin_out = ALPHABET[((pin_in_index + offset) + 26) % 26]
    return pin_out


def decode_letter(pin_in: str, rotor):
    """Takes the input and outputs the corresponding letter from current rotor"""
    # pin_in_index = rotor.pin_sequence.index(pin_in)
    pin_in_index = ALPHABET.index(pin_in)
    offset = rotor.position
    pin_out = ALPHABET[((pin_in_index - offset) + 26) % 26]
    return pin_out


def encrypt(plain_text: str):
    """Takes the unencrypted text and passes it through the sequence of rotors. Outputs the encrypted text."""
    # TODO Filter all punctuation
    if plain_text == " ":
        return ""
    rotator(wheel_one=wheel_one, wheel_two=wheel_two, wheel_three=wheel_three, selected_rotors=selected_rotors)
    encrypted_letter = plain_text
    for rotor in rotor_sequence:
        encrypted_letter = encode_letter(encrypted_letter, rotor)
    if encrypted_letter == plain_text:
        print(f'Error: {plain_text} encrytped as itself')
    return encrypted_letter


def decrypt(encrypted_letter: str):
    """Takes the encrypted text and passes it through the sequence of rotors. Outputs the decrypted text."""
    if encrypted_letter == " ":
        return ""
    rotator(wheel_one=wheel_one, wheel_two=wheel_two, wheel_three=wheel_three, selected_rotors=selected_rotors)
    decrypted_letter = encrypted_letter
    for rotor in rotor_sequence:
        decrypted_letter = decode_letter(decrypted_letter, rotor)
    return decrypted_letter


# Initialise the rotors, leaving the position blank for the user to set
rotor_one = Rotor(
    ROTOR_DETAILS['rotor_one']['pins'],
    ROTOR_DETAILS['rotor_one']['notch']
)
rotor_two = Rotor(
    ROTOR_DETAILS['rotor_two']['pins'],
    ROTOR_DETAILS['rotor_two']['notch']
)
rotor_three = Rotor(
    ROTOR_DETAILS['rotor_three']['pins'],
    ROTOR_DETAILS['rotor_three']['notch']
)
rotor_four = Rotor(
    ROTOR_DETAILS['rotor_four']['pins'],
    ROTOR_DETAILS['rotor_four']['notch']
)
rotor_five = Rotor(
    ROTOR_DETAILS['rotor_five']['pins'],
    ROTOR_DETAILS['rotor_five']['notch']
)
# The reflector loops the letter back through the machine,
# it doesn't move, therefore has no notch
reflector = Reflector(
    ROTOR_DETAILS['reflector']
)

# Assign the specified rotors to their positions
# TODO allow user to choose the rotors
wheel_one = rotor_one
wheel_two = rotor_four
wheel_three = rotor_five


# Create a list of the rotors to simulate the path of encryption/decryption
selected_rotors = [wheel_one, wheel_two, wheel_three]
reversed_rotors = selected_rotors[::-1]
selected_rotors.append(reflector)
rotor_sequence = selected_rotors + reversed_rotors

print('Please enter the starting positions of the rotors.')
for rotor in selected_rotors[:-1]:
    while rotor.position not in range(0, 26):
        rotor.position = int(input(f'Set starting position {selected_rotors.index(rotor) + 1} (0-25): '))


# wheel_three.position = int(input('Set starting position (0-25) of the third rotor: '))
# wheel_two.position = int(input('Set starting position (0-25) of the second rotor: '))
# wheel_one.position = int(input('Set starting position (0-25) of the first rotor: '))

response = input('Would you like to encrypt (E) or decrypt (D) a message? ').title()


if response == "E":
    message = input('Message to encrypt: ').upper()
    encoded_message = ""
    for letter in message:
        swapped_letter = plugboard(letter)
        encoded_letter = plugboard(encrypt(swapped_letter))
        encoded_message += encoded_letter
    print(message)
    print(encoded_message)

elif response == "D":
    message = input('Message to decrypt: ').upper()
    decoded_message = ""
    for letter in message:
        swapped_letter = plugboard(letter)
        decoded_letter = plugboard(decrypt(swapped_letter))
        decoded_message += decoded_letter

    print(decoded_message)


#test message
#tobeornottobethatisthequestiontobeornottobethatisthequestionatthezootodayonthewaytosanjosexmarksthespecificspot
