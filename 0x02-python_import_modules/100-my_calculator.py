#!/usr/bin/python3
def main():
    leng = len(argv)

    if leng != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    oper = argv[2]
    operators = ['+', '-', '*', '/']
    try:
        index_op = operators.index(oper)
    except ValueError:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    if index_op == 0:
        print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    elif index_op == 1:
        print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
    elif index_op == 2:
        print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    else:
        print("{:d} / {:d} = {}".format(a, b, div(a, b)))


if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    main()
