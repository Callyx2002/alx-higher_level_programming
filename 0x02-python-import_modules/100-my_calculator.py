#!/usr/bin/python3
from calculator_1 import add, mul, sub, div


def myfunc(argument):
    myList = ["+", "-", "*", "/"]
    first = int(argument[1])
    second = int(argument[3])
    if (len(argument) != 4):
        print("{}: {} {} {} {}".format(
            "Usage", "./100-my_calculator.py", "<a>", "operator", "<b>"))
        sys.exit(1)
    if (argument[2] not in myList):
        print("{}: {}".format(
            "Unknown operator. Available operators", "+, -, * and /"))
        sys.exit(1)

    if argument[2] == "+":
        result = add(first, second)
        print("{} {} {} = {}".format(first, argument[2], second, result))
    if argument[2] == "-":
        result = sub(first, second)
        print("{} {} {} = {}".format(first, argument[2], second, result))
    if argument[2] == "/":
        result = div(first, second)
        print("{} {} {} = {}".format(first, argument[2], second, result))
    if argument[2] == "*":
        result = mul(first, second)
        print("{} {} {} = {}".format(first, argument[2], second, result))


if __name__ == "__main__":
    import sys
    myfunc(sys.argv)
