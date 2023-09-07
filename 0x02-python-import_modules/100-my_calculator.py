#!/usr/bin/python3

if __name__ == "__main__":
    """Perform Simple Math Operation."""
    import calculator_1 as calc
    import sys

    argc = len(sys.argv) - 1
    ops = {"+": calc.add, "-": calc.sub, "*": calc.mul, "/": calc.div}
    if argc != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    elif sys.argv[2] not in list(ops.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    print("{} {} {} = {}".format(a, sys.argv[2], b, ops[sys.argv[2]](a, b)))
