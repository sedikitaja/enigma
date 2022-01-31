# Dictionary containing the output "key" and the notch location.
ROTOR_DETAILS = {
    "rotor_one":
        {
            "pins": "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
            "notch": "Q"
        },
    "rotor_two":
        {
            "pins": "AJDKSIRUXBLHWTMCQGZNPYFVOE",
            "notch": "E"
        },
    "rotor_three":
        {
            "pins": "BDFHJLCPRTXVZNYEIWGAKMUSQO",
            "notch": "V"
        },
    "rotor_four":
        {
            "pins": "ESOVPZJAYQUIRHXLNFTGKDCMWB",
            "notch": "J"
        },
    "rotor_five":
        {
            "pins": "VZBRGITYUPSDNHLXAWMJQOFECK",
            "notch": "Z"
        },
    "reflector": "YRUHQSLDPXNGOKMIEBFZCWVJAT"
}

ALPHABET = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
            "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]


class Rotor:
    def __init__(self, sequence, notch):
        self.pin_sequence = [letter for letter in sequence]
        self.notch = notch
        self.position = -1


class Reflector:
    def __init__(self, sequence):
        self.pin_sequence = [letter for letter in sequence]
        self.position = 1


def rotator(wheel_one, wheel_two, wheel_three, selected_rotors):
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
    for rotor in selected_rotors[:-1]:
        if rotor.position > 25:
            rotor.position = 0