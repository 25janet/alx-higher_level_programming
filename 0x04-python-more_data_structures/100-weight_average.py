#!/usr/bin/python3

def weight_average(my_list=[]):
    # Check if my_list is a non-empty list
    if not isinstance(my_list, list) or len(my_list) == 0:
        return 0

    # Initialize variables for weighted average calculation
    av = 0
    size = 0

    # Calculate weighted sum and total weight
    for t in my_list:
        av += (t[0] * t[1])
        size += t[1]

    # Calculate and return the weighted average
    return (av / size)
