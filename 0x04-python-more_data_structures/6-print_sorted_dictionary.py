#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """
    Print a dictionary with keys sorted in alphabetical order.

    Args:
        a_dictionary (dict): The input dictionary.

    Returns:
        None
    """
    sorted_keys = sorted(a_dictionary.keys())  # Sort keys alphabetically

    for key in sorted_keys:
        print("{}: {}".format(key, a_dictionary[key]))

# Test the function with the provided example
if __name__ == "__main__":
    a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3] }
    print_sorted_dictionary(a_dictionary)
