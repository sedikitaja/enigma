from rotors import Rotor, Reflector, ROTOR_DETAILS, ALPHABET


def encode_letter(pin_in: str, rotor):
    """Takes the input and outputs the corresponding letter from current rotor"""
    pin_in_index = ALPHABET.index(pin_in)
    pin_out = rotor.pin_sequence[((pin_in_index + 1) + rotor.position) % 26]
    return pin_out


def decode_letter(pin_in: str, rotor):
    """Takes the input and outputs the corresponding letter from current rotor"""
    pin_in_index = rotor.pin_sequence.index(pin_in)
    pin_out = ALPHABET[((pin_in_index - 1) - rotor.position) % 26]
    return pin_out


def encrypt(plain_text: str):
    """Takes the unencrypted text and passes it through the sequence of rotors. Outputs the encrypted text."""
    # TODO Filter all punctuation
    if plain_text == " ":
        return ""
    encrypted_letter = plain_text
    for rotor in rotor_sequence:
        encrypted_letter = encode_letter(encrypted_letter, rotor)
    return encrypted_letter


def decrypt(encrypted_letter: str):
    """Takes the encrypted text and passes it through the sequence of rotors. Outputs the decrypted text."""
    if encrypted_letter == " ":
        return ""
    decrypted_letter = encrypted_letter
    for rotor in rotor_sequence:
        decrypted_letter = decode_letter(decrypted_letter, rotor)
    return decrypted_letter


def rotator():
    """Increments the position of the first rotor by one, when it reaches the notch then steps the next rotor,
    when that reaches the notch then the third rotor is stepped."""
    turnover_one = False
    turnover_two = False
    wheel_one.position += 1
    if wheel_one.position == wheel_one.pin_sequence.index(wheel_one.notch):
        turnover_one = True
    if turnover_one:
        wheel_two.position += 1
        turnover_one = False
    if wheel_two.position == wheel_two.pin_sequence.index(wheel_two.notch):
        turnover_two = True
    if turnover_two:
        wheel_three.position += 1
        turnover_two = False


# Initialise the rotors, leaving the position blank for the user to set
rotor_one = Rotor(
    ROTOR_DETAILS["rotor_one"]["pins"],
    ROTOR_DETAILS["rotor_one"]["notch"]
)
rotor_two = Rotor(
    ROTOR_DETAILS["rotor_two"]["pins"],
    ROTOR_DETAILS["rotor_two"]["notch"]
)
rotor_three = Rotor(
    ROTOR_DETAILS["rotor_three"]["pins"],
    ROTOR_DETAILS["rotor_three"]["notch"]
)
rotor_four = Rotor(
    ROTOR_DETAILS["rotor_four"]["pins"],
    ROTOR_DETAILS["rotor_four"]["notch"]
)
rotor_five = Rotor(
    ROTOR_DETAILS["rotor_five"]["pins"],
    ROTOR_DETAILS["rotor_five"]["notch"]
)
# The reflector loops the letter back through the machine,
# it doesn't move, therefore has no notch
reflector = Reflector(
    ROTOR_DETAILS["reflector"]
)

# Assign the specified rotors to their positions
# TODO allow user to choose the rotors and order
wheel_one = rotor_one
wheel_two = rotor_four
wheel_three = rotor_five


# Create a list of the rotors to simulate the path of encryption/decryption
selected_rotors = [wheel_one, wheel_two, wheel_three]
reversed_rotors = selected_rotors[::-1]
selected_rotors.append(reflector)
rotor_sequence = selected_rotors + reversed_rotors


wheel_one.position = 1
wheel_two.position = 1
wheel_three.position = 1
# message = input('Message to encrypt: ').upper()
message = "A"

encoded_message = ""
for letter in message:
    encoded_letter = encrypt(letter)
    encoded_message += encoded_letter

print(encoded_message)

wheel_one.position = 1
wheel_two.position = 1
wheel_three.position = 1
decoded_message = ""
for letter in encoded_message:
    decoded_letter = decrypt(letter)
    decoded_message += decoded_letter

print(decoded_message)
