#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = {}
    for key in list(a_dictionary.keys()):
        newer = a_dictionary[key] * 2
        new.update({key: newer})
    return new
