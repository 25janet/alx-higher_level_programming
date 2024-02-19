#!/usr/bin/python3

def raise_exception():
    # Attempting an operation that raises a TypeError
    try:
        # Trying to add an integer and a string which raises a TypeError
        result = 1 + "hello"
    except TypeError:
        # Raise the TypeError explicitly
        raise TypeError("Exception raised")


if __name__ == "__main__":
    try:
        raise_exception()
    except TypeError as te:
        print(te)
