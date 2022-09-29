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
    return -1


def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    if roman_string == "":
        return 0
    total = i = 0
    while i < len(roman_string):
        s1 = convert(roman_string[i])
        if s1 == -1:
            return 0
        if (i + 1 < len(roman_string)):
            s2 = convert(roman_string[i + 1])
            if s2 == -1:
                return 0
            if s1 >= s2:
                total += s1 + s2
            else:
                total += s2 - s1
            i += 2
        else:
            total += s1
            i += 1
    return total
