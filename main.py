from rotors import Rotor, Reflector, ROTOR_DETAILS

ALPHABET = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
            "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]


# Initialise the rotors
rotor_one = Rotor(
    ROTOR_DETAILS["rotor_one"]["key"],
    ROTOR_DETAILS["rotor_one"]["notch"]
)
rotor_two = Rotor(
    ROTOR_DETAILS["rotor_two"]["key"],
    ROTOR_DETAILS["rotor_two"]["notch"]
)
rotor_three = Rotor(
    ROTOR_DETAILS["rotor_three"]["key"],
    ROTOR_DETAILS["rotor_three"]["notch"]
)
rotor_four = Rotor(
    ROTOR_DETAILS["rotor_four"]["key"],
    ROTOR_DETAILS["rotor_four"]["notch"]
)
rotor_five = Rotor(
    ROTOR_DETAILS["rotor_five"]["key"],
    ROTOR_DETAILS["rotor_five"]["notch"]
)
# The reflector loops the letter back through the machine,
# it doesn't move, therefore has no notch
reflector = Reflector(
    ROTOR_DETAILS["reflector"]
)

wheel_one = rotor_one
wheel_two = rotor_three
wheel_three = rotor_five

selected_rotors = [wheel_one, wheel_two, wheel_three]
reversed_rotors = selected_rotors[::-1]

message = "h"

# Malleable code

new_message = ""
for letter in message:
    pin = ALPHABET.index(letter.title())
    for rotor in selected_rotors:
        new_letter = rotor.combination[pin]
        pin = rotor.combination.index(new_letter)
        print(new_letter)
    # pass through the reflector
    new_letter = reflector.combination[pin]
    pin = reflector.combination.index(new_letter)
    for rotor in reversed_rotors:
        new_letter = rotor.combination[pin]
        pin = rotor.combination.index(new_letter)
    new_message += new_letter
print(new_message)

decoded_message = ""
for letter in new_message:
    pin = reversed_rotors[0].combination.index(letter)
    for rotor in reversed_rotors:
        new_letter = rotor.combination[pin]
        pin = rotor.combination.index(new_letter)
    # pass through the reflector
    new_letter = reflector.combination[pin]
    pin = reflector.combination.index(new_letter)
    for rotor in selected_rotors:
        new_letter = rotor.combination[pin]
        pin = rotor.combination.index(new_letter)
    new_letter = ALPHABET[pin]
    decoded_message += new_letter
print(decoded_message)

# Original code

new_message_orig = ""
step = 0
for letter in message:
    pin = ALPHABET.index(letter.title())
    new_letter = wheel_one.combination[pin + step]
    step += 1
    pin = wheel_one.combination.index(new_letter)
    new_letter = wheel_two.combination[pin]
    new_message_orig += new_letter
print(new_message_orig)

decoded_message = ""
step = 0
for letter in new_message_orig:
    pin = wheel_two.combination.index(letter)
    new_letter = wheel_one.combination[pin]
    pin = wheel_one.combination.index(new_letter)
    new_letter = ALPHABET[pin - step]
    decoded_message += new_letter
    step += 1
print(decoded_message)
