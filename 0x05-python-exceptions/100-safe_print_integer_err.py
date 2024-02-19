#!/usr/bin/python3

import sys

def safe_print_integer_err(value):
    try:
        # Try converting the value to an integer and printing it
        print("{:d}".format(value))
        return True
    except Exception as e:
        # If any exception occurs, print the error to stderr
        print("Exception: {}".format(e), file=sys.stderr)
        return False


if __name__ == "__main__":
    value = 89
    has_been_print = safe_print_integer_err(value)
    if not has_been_print:
        print("{} is not an integer".format(value))

    value = -89
    has_been_print = safe_print_integer_err(value)
    if not has_been_print:
        print("{} is not an integer".format(value))

    value = "School"
    has_been_print = safe_print_integer_err(value)
    if not has_been_print:
        print("{} is not an integer".format(value))
