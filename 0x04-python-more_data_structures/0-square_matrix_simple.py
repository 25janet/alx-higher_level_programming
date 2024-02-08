#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """
    Square the integers in a matrix.

    Args:
        matrix (list of lists): Input matrix.

    Returns:
        list of lists: New matrix with squared values.
    """
    return [list(map(lambda x: x ** 2, row)) for row in matrix]
