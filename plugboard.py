# Plugboard
# The plugboard would swap 10 pairs of letters
plugboard_pairs = [
    [
        "A",
        "D"
    ],
    [
        "E",
        "N"
    ],
    [
        "R",
        "U"
    ],
    [
        "Q",
        "Z"
    ],
    [
        "I",
        "J"
    ],
    [
        "Y",
        "B"
    ],
    [
        "K",
        "P"
    ],
    [
        "O",
        "S"
    ],
    [
        "T",
        "C"
    ],
    [
        "F",
        "M"
    ]
]

def plugboard(char):
    for pair in plugboard_pairs:
        if char in pair:
            char_index = pair.index(char)
            if char_index == 0:
                return pair[1]
            else:
                return pair[0]
        else:
            return char

print(plugboard("V"))