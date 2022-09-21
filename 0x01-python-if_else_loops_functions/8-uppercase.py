#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            print("{}".format(chr(ord(i)-32)),end="" if str.index(i) < len(str)-1 else "{}\n".format(chr(ord(i)-32)))
        else:
            print("{}".format(i), end="" if str.index(i) < len(str)-1 else "{}\n".format(i))
# uppercase("best")
# uppercase("Best School 98 Battery street")
