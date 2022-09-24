#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    new = my_list.copy()
    for i in new:
        if i == idx:
            new[i] = element
            return new
