#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new = []
    compressed = list(a_dictionary.keys())
    compressed.sort()
    for i in compressed:
        print("{}: {}".format(i, a_dictionary[i]))
