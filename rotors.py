class Rotor:
    def __init__(self, sequence, notch):
        self.pin_sequence = [letter for letter in sequence]
        self.notch = notch
        self.position = None




class Reflector:
    def __init__(self, sequence):
        self.pin_sequence = [letter for letter in sequence]


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