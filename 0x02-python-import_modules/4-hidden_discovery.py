#!/usr/bin/python3
import hidden_4
def main():
    myList = dir(hidden_4)
    for i in myList:
        if myList[0:2] =="__":
            continue
        else:
            print("{:s}".format(i))
if __name__ == "__main__":
    main()
