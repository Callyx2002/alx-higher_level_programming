#!/usr/bin/python3
def uniq_add(my_list=[]):
    total = 0
    for i in range(len(my_list)):
        if my_list.index(my_list[i]) == i:
            total += my_list[i]
    return total
