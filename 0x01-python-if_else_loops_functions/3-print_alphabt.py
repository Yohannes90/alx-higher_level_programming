#!/usr/bin/python3
for ch in range(97, 123):
    if chr(ch) == 'q' or chr(ch) == 'e':
        continue
    print("{}".format(chr(ch)), end="")
