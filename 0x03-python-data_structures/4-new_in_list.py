#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new = my_list[:]
    if idx < 0 or idx >= len(my_list):
        return my_list
    for i in range(len(new)-1):
        if i == idx:
            new[i] = element
            return new
    return new
