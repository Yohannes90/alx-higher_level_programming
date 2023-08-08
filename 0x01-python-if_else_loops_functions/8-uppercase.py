#!/usr/bin/python3

def uppercase(str):
    for ch in str:
        if ord(ch) in range(97, 123):
            ch = chr(ord(ch) - 32)
        print("{:s}".format(ch), end="")
    print("")
