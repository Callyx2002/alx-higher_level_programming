#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    convert = {
        "M": 1000,
        "D": 500,
        "C": 100,
        "L": 50,
        "X": 10,
        "V": 5,
        "I": 1
    }
    total = 0
    i = 0
    while i < len(roman_string):
        s1 = convert[roman_string[i]]
        if (i + 1 < len(roman_string)):
            s2 = convert[roman_string[i + 1]]
            if s1 >= s2:
                total += s1 + s2
            else:
                total += s2 - s1
            i += 2
        else:
            total += s1
            i += 1
    return total
