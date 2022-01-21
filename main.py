from rotors import Rotor, Reflector, ROTOR_DETAILS

ALPHABET = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
            "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]


# Initialise the rotors
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

wheel_one = rotor_one
wheel_two = rotor_three
wheel_three = rotor_five

selected_rotors = [wheel_one, wheel_two, wheel_three]
reversed_rotors = selected_rotors[::-1]
selected_rotors.append(reflector)
rotor_sequence = selected_rotors + reversed_rotors
message = "hello"

# rotor needs pin_in & pin_out, pin in corresponds to path = ALPHABET.index() while pin_out = pins.index(path)

def encode(pin_in, rotor):
    """Takes the input and outputs the corresponding letter"""
    pin_in_index = ALPHABET.index(pin_in.title())
    pin_out = rotor.pin_sequence[(pin_in_index + 1) % 26]
    return pin_out

def decode(pin_in, rotor):
    pin_in_index = rotor.pin_sequence.index(pin_in.title())
    pin_out = ALPHABET[(pin_in_index - 1) % 26]
    return pin_out

def encrypt(input):
    output = encode(
        encode(
            encode(
                encode(
                    encode(
                        encode(
                            encode(
                                input,
                                rotor_one),
                            rotor_two),
                        rotor_three),
                    reflector),
                rotor_three),
            rotor_two),
        rotor_one)
    return output

def decrypt(input):
    output = decode(
        decode(
            decode(
                decode(
                    decode(
                        decode(
                            decode(
                                input,
                                rotor_one),
                            rotor_two),
                        rotor_three),
                    reflector),
                rotor_three),
            rotor_two),
        rotor_one)
    return output

encoded_message = ""
for letter in message:
    encoded_letter = encrypt(letter)
    encoded_message += encoded_letter

print(encoded_message)

decoded_message = ""
for letter in encoded_message:
    decoded_letter = decrypt(letter)
    decoded_message += decoded_letter
print(decoded_message)