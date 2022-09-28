#!/usr/bin/python3
def number_keys(a_dictionary):
    new = []
    for i in list(a_dictionary.keys()):
        new.append(i)
    return(len(new))
