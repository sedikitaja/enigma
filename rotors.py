class Rotor:
    def __init__(self, combo, notch):
        self.combination = [letter for letter in combo]
        self.notch = notch


class Reflector:
    def __init__(self, combo):
        self.combination = [letter for letter in combo]


# Dictionary containing the output "key" and the notch location.
ROTOR_DETAILS = {
    "rotor_one":
        {
            "key": "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
            "notch": "Q"
        },
    "rotor_two":
        {
            "key": "AJDKSIRUXBLHWTMCQGZNPYFVOE",
            "notch": "E"
        },
    "rotor_three":
        {
            "key": "BDFHJLCPRTXVZNYEIWGAKMUSQO",
            "notch": "V"
        },
    "rotor_four":
        {
            "key": "ESOVPZJAYQUIRHXLNFTGKDCMWB",
            "notch": "J"
        },
    "rotor_five":
        {
            "key": "VZBRGITYUPSDNHLXAWMJQOFECK",
            "notch": "Z"
        },
    "reflector": "YRUHQSLDPXNGOKMIEBFZCWVJAT"
}