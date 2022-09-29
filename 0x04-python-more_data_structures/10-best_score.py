#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    mylist = list(a_dictionary.keys())
    biggest = None
    for i in mylist:
        for j in mylist[mylist.index(i) + 1:]:
            if a_dictionary[i] > a_dictionary[j]:
                biggest = i
            else:
                biggest = j
    return biggest
