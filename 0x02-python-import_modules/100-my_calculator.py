#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv, exit
    if len(argv) != 4:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    operand_1 = int(argv[1])
    operand_2 = int(argv[3])
    operator = argv[2]
    match operator:
        case '+':
            print("{} + {} = {}".format(operand_1, operand_2, add(operand_1, operand_2)))
        case '-':
            print("{} - {} = {}".format(operand_1, operand_2, sub(operand_1, operand_2)))
        case '*':
            print("{} * {} = {}".format(operand_1, operand_2, (operand_1 * operand_2)))
        case '/':
            print("{} / {} = {}".format(operand_1, operand_2, div(operand_1, operand_2)))
        case _:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
    exit(0)