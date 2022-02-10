# Plugboard
# The plugboard would swap up to 10 pairs of letters.


def plugboard(char, plugboard_pairs):
    """Checks to see if the letter should be swapped and returns the corresponding letter,
     otherwise returns the original character."""
    for pair in plugboard_pairs:
        if char in pair:
            char_index = pair.index(char)
            if char_index == 0:
                return pair[1]
            else:
                return pair[0]
        else:
            return char
