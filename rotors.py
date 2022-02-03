# Dictionary containing the output "key" and the notch location.
ROTOR_DETAILS = {
    "I":
        {
            "pins": "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
            "notch": "Q"
        },
    "II":
        {
            "pins": "AJDKSIRUXBLHWTMCQGZNPYFVOE",
            "notch": "E"
        },
    "III":
        {
            "pins": "BDFHJLCPRTXVZNYEIWGAKMUSQO",
            "notch": "V"
        },
    "IV":
        {
            "pins": "ESOVPZJAYQUIRHXLNFTGKDCMWB",
            "notch": "J"
        },
    "V":
        {
            "pins": "VZBRGITYUPSDNHLXAWMJQOFECK",
            "notch": "Z"
        },
    "reflector": "YRUHQSLDPXNGOKMIEBFZCWVJAT"
}

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


class Rotor:
    def __init__(self, sequence, notch):
        self.pin_sequence = sequence
        self.notch = notch
        self.position = -1


class Reflector:
    def __init__(self, sequence):
        self.pin_sequence = sequence
        self.position = 0

