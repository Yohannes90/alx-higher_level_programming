#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    num = len(argv)
    print("{} arguments.".format(num - 1))
    for i in range(1, num):
        print("{}: {}".format(i, argv[i]))
