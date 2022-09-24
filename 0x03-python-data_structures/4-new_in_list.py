#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new = my_list.copy()
    if idx < 0 or idx > len(my_list) -1:
        return new
    for i in new:
        if i == idx:
            new[i] = element
            return new
    return new
