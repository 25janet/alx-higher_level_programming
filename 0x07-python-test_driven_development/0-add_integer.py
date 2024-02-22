#!/usr/bin/python3

def add_integer(a=None, b=98):
    """
    Adds two integers.

    Args:
    a (int): The first integer.
    b (int): The second integer. Defaults to 98.

    Returns:
    int: The sum of a and b.

    Raises:
    TypeError: If a or b is not an integer or a float.

    Examples:
    >>> add_integer(1, 2)
    3
    >>> add_integer(-1, 2)
    1
    >>> add_integer(1.5, 2.9)
    3
    >>> add_integer(-2.9, 1)
    -1
    >>> add_integer(1)
    99
    >>> add_integer(None)
    Traceback (most recent call last):
    ...
    TypeError: a must be an integer
    >>> add_integer(float("inf"))
    Traceback (most recent call last):
    ...
    TypeError: a must be an integer
    """

    if a is not None and not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if a is None:
        raise TypeError("a must be an integer")

    return int(a) + int(b)
