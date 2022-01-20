from main import ALPHABET
from random import choice
# Plugboard
# The plugboard would swap 10 pairs of letters
plugboard_pairs = []
alphabet = ALPHABET
# Generate the 10 pairs and populate the list.
for i in range(10):
    letter_one = choice(alphabet)
    alphabet.remove(letter_one)
    letter_two = choice(alphabet)
    alphabet.remove(letter_two)
    letter_pair = (letter_one, letter_two)
    plugboard_pairs.append(letter_pair)

print(plugboard_pairs)
print(alphabet)