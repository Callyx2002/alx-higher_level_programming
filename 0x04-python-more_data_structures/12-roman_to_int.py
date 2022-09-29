#!/usr/bin/python3
def convert(m):
    if m == "M":
        return 1000
    if m == "D":
        return 500
    if m == "C":
        return 100
    if m == "L":
        return 50
    if m == "X":
        return 10
    if m == "V":
        return 5
    if m == "I":
        return 1
    return None


def roman_to_int(roman_string):
    if type(roman_string) != str:
        return None
    total = i = 0
    while i < len(roman_string):
        s1 = convert(roman_string[i])
        ifs1 is None:
            return None
        if (i + 1 < len(roman_string)):
            s2 = convert(roman_string[i + 1])
            if s2 is None:
                return None
            if s1 >= s2:
                total += s1 + s2
            else:
                total += s2 - s1
            i += 2
        else:
            total += s1
            i += 1
    return total
