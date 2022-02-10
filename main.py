# ------------------------------------------------[Import Statements]---------------------------------------------------

from rotors import ROTOR_DETAILS, ALPHABET, Rotor, Reflector, rotate, pin_sequence_startup, passthrough_rotor
from plugboard import plugboard
from generator import key_generator, current_date
import json
# from flask import Flask, render_template, url_for

# ------------------------------------------------[Define Functions]----------------------------------------------------


def encrypt_character(char):
    """Takes in a character, runs it through the sequence of Plugboard, Rotors,
    Reflector, Rotors and Plugboard again and returns the result."""
    encrypted_char = plugboard(char, day_plugboard)
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
    return plugboard(encrypted_char, day_plugboard)


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


def get_keys():
    """Returns the key_list.json file as"""
    with open('key_lists/key_list.json', 'r') as keys:
        data = json.load(keys)
        return data


# ----------------------------------------------[Enigma Configuration]--------------------------------------------------

# Check for key_list file, if it doesn't exist, create it
try:
    key_data = get_keys()
except FileNotFoundError:
    key_generator()
    key_data = get_keys()

# Get the keys for today and assign them to variables
day_data = key_data[current_date() - 1][f'{current_date()}']
day_rotors = day_data['rotors']
day_ring_settings = day_data['ring_setting']
day_plugboard = day_data['plugboard_pairs']
day_reflector_wiring = day_data['reflector_wiring']
day_rotor_position = day_data['rotor_position']

# Initialise the Rotors
right_rotor_selection = day_rotors[2]
right_rotor = Rotor(sequence=ROTOR_DETAILS[right_rotor_selection]["pins"],
                    notch=ROTOR_DETAILS[right_rotor_selection]["notch"],
                    ring_setting=day_ring_settings[2])
middle_rotor_selection = day_rotors[1]
middle_rotor = Rotor(sequence=ROTOR_DETAILS[middle_rotor_selection]["pins"],
                     notch=ROTOR_DETAILS[middle_rotor_selection]["notch"],
                     ring_setting=day_ring_settings[1])
left_rotor_selection = day_rotors[0]
left_rotor = Rotor(sequence=ROTOR_DETAILS[left_rotor_selection]["pins"],
                   notch=ROTOR_DETAILS[left_rotor_selection]["notch"],
                   ring_setting=day_ring_settings[0])

# Initialise the reflector
reflector = Reflector(ROTOR_DETAILS[day_reflector_wiring])

# Get the rotor starting positions from the user and offset by the ring setting.
right_rotor.position = (ALPHABET.index(day_rotor_position[2]) + right_rotor.ring_setting) % 26
middle_rotor.position = (ALPHABET.index(day_rotor_position[1]) + right_rotor.ring_setting) % 26
left_rotor.position = (ALPHABET.index(day_rotor_position[0]) + right_rotor.ring_setting) % 26

# Adjust the rotor sequences to the starting position
right_rotor.pin_sequence = pin_sequence_startup(right_rotor)
middle_rotor.pin_sequence = pin_sequence_startup(middle_rotor)
left_rotor.pin_sequence = pin_sequence_startup(left_rotor)

message = input('Message to be encrypted:\n').upper()

print(encrypt_message(message))

# test message
# tobeornottobethatisthequestiontobeornottobethatisthequestionatthezootodayonthewaytosanjosexmarksthespecificspot
