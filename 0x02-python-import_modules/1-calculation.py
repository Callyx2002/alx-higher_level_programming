#!/usr/bin/python3
from calculator_1 import add, sub, div, mul
"""
include the if __name__ == "__main__" so my program wont run when imported
"""
if __name__ == "__main__":
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))
else:
    pass