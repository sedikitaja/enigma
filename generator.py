from random import randint, choice
from calendar import monthrange
from datetime import date
from rotors import ALPHABET, ROTORS
import json

year = date.today().year
month = date.today().month

days_curr_month = monthrange(year, month)

month_settings = []
previous_day_rotors = []


def current_date():
    """Simply returns an int of the date."""
    return date.today().day


def key_generator():
    """Generates a json file with randomly generated key settings for the enigma machine."""
    global previous_day_rotors
    for day in range(days_curr_month[1]):
        date_num = day + 1
        temp_rotors = ROTORS.copy()
        selected_rotors = []

        # Ensure that no rotor is in the same position as the previous day
        if len(previous_day_rotors) == 3:
            for rotor in previous_day_rotors:
                rotor_choice = choice(temp_rotors)

                # If rotor is in the same position, reselect a different rotor.
                if rotor_choice == rotor:
                    temp = rotor_choice
                    temp_rotors.remove(temp)
                    rotor_choice = choice(temp_rotors)
                    temp_rotors.append(temp)
                    temp_rotors.remove(rotor_choice)
                    selected_rotors.append(rotor_choice)

                else:
                    selected_rotors.append(rotor_choice)
                    temp_rotors.remove(rotor_choice)

        else:
            # Get the rotors for the first day
            for i in range(3):
                rotor_choice = choice(temp_rotors)
                temp_rotors.remove(rotor_choice)
                selected_rotors.append(rotor_choice)

        # create the ring settings for the rotors
        # TODO Implement these in main.py
        ring_setting = [randint(1, 26) for _ in range(3)]

        # Generate the pairs of letters for the plugboard
        temp_alpha = ALPHABET
        plugboard_pairs = []
        for i in range(10):
            letter_one = choice(temp_alpha)
            temp_alpha = temp_alpha.replace(letter_one, '')
            letter_two = choice(temp_alpha)
            # Ensure the pairs are not located next to each other in the alphabet
            if (ALPHABET.index(letter_two) - 1) == ALPHABET.index(letter_one) or \
                    (ALPHABET.index(letter_two) + 1) == ALPHABET.index(letter_one):
                temp = letter_two
                temp_alpha = temp_alpha.replace(letter_two, '')
                letter_two = choice(temp_alpha)
                temp_alpha = temp_alpha + temp
            temp_alpha = temp_alpha.replace(letter_two, '')
            pair = [letter_one, letter_two]
            plugboard_pairs.append(pair)

        # Generate the rotor starting positions
        rotor_positions = [ALPHABET[randint(0, 25)] for _ in range(3)]

        # Create a dictionary with the settings for the day
        day_settings = {
            date_num: {
                'rotors': selected_rotors,
                'ring_setting': ring_setting,
                'plugboard_pairs': plugboard_pairs,
                # TODO Add multiple reflector settings.
                'reflector_wiring': 'reflector',
                'rotor_position': rotor_positions
            }
        }
        previous_day_rotors = selected_rotors.copy()
        month_settings.append(day_settings)

    with open('key_lists/key_list.json', 'w+') as json_file:
        json.dump(month_settings, json_file)
