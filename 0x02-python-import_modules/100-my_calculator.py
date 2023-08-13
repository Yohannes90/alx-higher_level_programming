#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv, exit
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    op1 = int(argv[1])
    op2 = int(argv[3])
    operator = argv[2]
    if operator == '+':
        print("{} + {} = {}".format(op1, op2, add(op1, op2)))
    elif operator == '-':
        print("{} - {} = {}".format(op1, op2, sub(op1, op2)))
    elif operator == '*':
        print("{} * {} = {}".format(op1, op2, mul(op1, op2)))
    elif operator == '/':
        print("{} / {} = {}".format(op1, op2, div(op1, op2)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    exit(0)
