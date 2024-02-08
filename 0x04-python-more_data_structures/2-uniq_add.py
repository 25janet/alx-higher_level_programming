#!/usr/bin/python3

def uniq_add(my_list=[]):
    """
    Calculate the sum of all unique integers in the list.

    Args:
        my_list (list): The input list.

    Returns:
        int: The sum of unique integers in the list.
    """
    number = 0
    for element in set(my_list):
        number += element
    return number
