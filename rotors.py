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

ROTORS = ['I', 'II', 'III', 'IV', 'V']

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# ------------------------------------------------[Define Classes]----------------------------------------------------


class Rotor:
    def __init__(self, sequence, notch, ring_setting):
        self.pin_sequence = sequence
        self.notch = notch
        self.position = -1
        self.ring_setting = ring_setting


class Reflector:
    def __init__(self, sequence):
        self.pin_sequence = sequence
        self.position = 0

# ------------------------------------------------[Define Functions]----------------------------------------------------


def rotate(sequence: str, r_rotor: Rotor, m_rotor: Rotor, l_rotor: Rotor):
    """Imitates the rotation of the rotors by moving the last letter of the sequence to the start
    and increments the rotor position by 1.
    If the rotation aligns with a Notch in the rotor it will turn the left adjacent rotor and double step the initial
    rotor. Just as the Enigma Machine did."""
    r_rotor.position += 1
    if r_rotor.pin_sequence[0] == r_rotor.notch:
        # Double step to prevent free turning of adjacent rotor.
        r_rotor.position += 1
        r_rotor.pin_sequence = pin_sequence_adjust(r_rotor.pin_sequence)
        m_rotor.position += 1
        m_rotor.pin_sequence = pin_sequence_adjust(m_rotor.pin_sequence)
    if m_rotor.pin_sequence[0] == m_rotor.notch:
        # Double step to prevent free turning of adjacent rotor.
        m_rotor.position += 1
        m_rotor.pin_sequence = pin_sequence_adjust(m_rotor.pin_sequence)
        l_rotor.position += 1
        l_rotor.pin_sequence = pin_sequence_adjust(l_rotor.pin_sequence)
    # Create a list of rotors for position checking.
    rotors = [r_rotor, m_rotor, l_rotor]
    # Check if rotor.position needs to be reset
    for rotor in rotors:
        if rotor.position > 25:
            rotor.position = 0
    return pin_sequence_adjust(sequence)


def pin_sequence_adjust(sequence):
    """Imitates the rotation of the rotors by moving the last letter of the sequence to the start."""
    return sequence[-1] + sequence[:len(sequence) - 1]


def pin_sequence_startup(rotor: Rotor):
    """Re-sequences the pin_sequence of the rotor to match the starting position."""
    for i in range(rotor.position):
        rotor.pin_sequence = pin_sequence_adjust(rotor.pin_sequence)
    return rotor.pin_sequence


def passthrough_rotor(char: str, rotor: Rotor or Reflector):
    """Passes the character through the rotor, and returns the encoded character."""
    alpha_index = ALPHABET.index(char)
    return rotor.pin_sequence[alpha_index]
