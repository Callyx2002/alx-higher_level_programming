#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    for i in matrix:
        total = []
        for j in i:
            total.append(j ** 2)
        new.append(total)
    return new
