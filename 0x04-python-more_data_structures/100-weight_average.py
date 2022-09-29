#!/usr/bin/python3
def weight_average(my_list=[]):
    total = 0
    div = 0
    average = 0
    for i in my_list:
        each = 1
        for j in range(len(i)):
            each *= i[j]
            if (j == (len(i) - 1)):
                div += i[j]
        total += each
    average = total / div
    return average
