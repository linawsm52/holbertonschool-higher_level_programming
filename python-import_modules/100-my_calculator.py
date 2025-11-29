#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = sys.argv[1]
    operator = sys.argv[2]
    b = sys.argv[3]

    if not a.lstrip('-').isdigit() or not b.lstrip('-').isdigit():
        print("Unknown operator. Only: +, -, * and /")
        sys.exit(1)

    a = int(a)
    b = int(b)

    if operator == "+":
        print(f"{a} + {b} = {add(a, b)}")
    elif operator == "-":
        print(f"{a} - {b} = {sub(a, b)}")
    elif operator == "*":
        print(f"{a} * {b} = {mul(a, b)}")
    elif operator == "/":
        print(f"{a} / {b} = {div(a, b)}")
    else:
        print("Unknown operator. Available operators: +, -, *, /")
        sys.exit(1)
