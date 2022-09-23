#!/usr/bin/python3
import sys
if __name__ == "__main__":
    if (len(sys.argv) == 2):
        print("{} {}:".format((len(sys.argv) - 1), "argument"))
    elif (len(sys.argv) == 1):
        print("{} {}.".format((len(sys.argv) - 1), "arguments"))
    else:
        print("{} {}:".format((len(sys.argv) - 1), "arguments"))
    for i in range(1, len(sys.argv)):
        print("{}: {}".format(i, sys.argv[i]))
else:
    pass