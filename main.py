# ------------------------------------------------[Import Statements]---------------------------------------------------

from rotors import Rotor, Reflector, ROTOR_DETAILS, ALPHABET
from plugboard import plugboard


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


def encrypt_character(char):
    """Takes in a character, runs it through the sequence of Plugboard, Rotors,
    Reflector, Rotors and Plugboard again and returns the result."""
    encrypted_char = plugboard(char)
    encrypted_char = passthrough_rotor(encrypted_char, right_rotor)
    encrypted_char = passthrough_rotor(encrypted_char, middle_rotor)
    encrypted_char = passthrough_rotor(encrypted_char, left_rotor)
    encrypted_char = passthrough_rotor(encrypted_char, reflector)
    char_index = left_rotor.pin_sequence.index(encrypted_char)
    encrypted_char = ALPHABET[char_index]
    char_index = middle_rotor.pin_sequence.index(encrypted_char)
    encrypted_char = ALPHABET[char_index]
    char_index = right_rotor.pin_sequence.index(encrypted_char)
    encrypted_char = ALPHABET[char_index]
    return plugboard(encrypted_char)


def encrypt_message(plain_text):
    """Takes in the entire input and passes it letter by letter through the encrypt_character function.
    Returns the encoded message."""
    message_output = ""
    for letter in plain_text:
        if letter not in ALPHABET:
            pass
        else:
            right_rotor.pin_sequence = rotate(right_rotor.pin_sequence, right_rotor, middle_rotor, left_rotor)
            encrypted_letter = encrypt_character(letter)

            # Error check, Enigma would never encode a letter as itself.
            if encrypted_letter == letter:
                print(f'Error: {letter} encoded as itself.')
            message_output += encrypted_letter
    return message_output


# ----------------------------------------------[Enigma Configuration]--------------------------------------------------

# List of available rotors
rotor_list = ["I", "II", "III", "IV", "V"]

# User selects their chosen rotor configuration
right_rotor_selection = input(f'Please select the right rotor {rotor_list}: ').upper()
right_rotor = Rotor(ROTOR_DETAILS[right_rotor_selection]["pins"],
                    ROTOR_DETAILS[right_rotor_selection]["notch"])
rotor_list.remove(right_rotor_selection)
middle_rotor_selection = input(f'Please select the middle rotor {rotor_list}: ').upper()
middle_rotor = Rotor(ROTOR_DETAILS[middle_rotor_selection]["pins"],
                     ROTOR_DETAILS[middle_rotor_selection]["notch"])
rotor_list.remove(middle_rotor_selection)
left_rotor_selection = input(f'Please select the left rotor {rotor_list}: ').upper()
left_rotor = Rotor(ROTOR_DETAILS[left_rotor_selection]["pins"],
                   ROTOR_DETAILS[left_rotor_selection]["notch"])
rotor_list.remove(left_rotor_selection)

# Initialise the reflector
reflector = Reflector(ROTOR_DETAILS["reflector"])

# Get the rotor starting positions from the user
right_rotor.position = int(input('Please enter the starting position on the right rotor: '))
middle_rotor.position = int(input('Please enter the starting position on the middle rotor: '))
left_rotor.position = int(input('Please enter the starting position on the left rotor: '))

# Adjust the rotor sequences to the starting position
right_rotor.pin_sequence = pin_sequence_startup(right_rotor)
middle_rotor.pin_sequence = pin_sequence_startup(middle_rotor)
left_rotor.pin_sequence = pin_sequence_startup(left_rotor)

message = input('Message to be encrpyted:\n').upper()

print(encrypt_message(message))

# test message
# tobeornottobethatisthequestiontobeornottobethatisthequestionatthezootodayonthewaytosanjosexmarksthespecificspot
