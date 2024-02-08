#!/usr/bin/python3

def best_score(a_dictionary):
    """
    Find the key with the largest integer value in a dictionary.

    Args:
        a_dictionary (dict): The input dictionary with integer values.

    Returns:
        str or None: The key with the largest integer value, or None if no score is found.
    """
    return max(a_dictionary, key=lambda key: a_dictionary[key], default=None) if a_dictionary else None
