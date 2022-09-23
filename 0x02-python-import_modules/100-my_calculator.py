#!/usr/bin/python3
import calculator_1
import sys


def main():
    myList = ["+", "-", "*", "/"]
    first = int(sys.argv[1])
    second = int(sys.argv[3])
    if (len(sys.argv) != 4):
        print("{}: {} {} {} {}".format(
            "Usage", "./100-my_calculator.py", "<a>", "operator", "<b>"))
        sys.exit(1)
    if (sys.argv[2] not in myList):
        print("{}: {}".format(
            "Unknown operator. Available operators", "+, -, * and /"))
        sys.exit(1)

    if sys.argv[2] == "+":
            result = calculator_1.add(first, second)
            print("{} {} {} = {}".format(first, sys.argv[2], second, result))
    if sys.argv[2] ==  "-":
            result = calculator_1.sub(first, second)
            print("{} {} {} = {}".format(first, sys.argv[2], second, result))
    if sys.argv[2] ==  "/":
            result = calculator_1.div(first, second)
            print("{} {} {} = {}".format(first, sys.argv[2], second, result))
    if sys.argv[2] ==  "*":
            result = calculator_1.mul(first, second)
            print("{} {} {} = {}".format(first, sys.argv[2], second, result))


if __name__ == "__main__":
    main()
