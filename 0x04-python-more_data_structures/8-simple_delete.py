#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    """
    Delete a key from a dictionary if it exists.

    Args:
        a_dictionary (dict): The input dictionary.
        key (str): The key to delete (default is an empty string).

    Returns:
        dict: The updated dictionary.
    """
    a_dictionary.pop(key, None)  # Remove the key if it exists, or do nothing
    return a_dictionary
