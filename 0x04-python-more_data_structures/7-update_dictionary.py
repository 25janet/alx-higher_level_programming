#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    """
    Replace or add a key-value pair in a dictionary.

    Args:
        a_dictionary (dict): The input dictionary.
        key (str): The key to replace or add.
        value: The value to assign to the key.

    Returns:
        dict: The updated dictionary.
    """
    a_dictionary[key] = value  # Replace or add the key-value pair
    return a_dictionary

# Test the function with the provided examples
if __name__ == "__main__":
    a_dictionary = { 'language': "C", 'number': 89, 'track': "Low level" }

    new_dict = update_dictionary(a_dictionary, 'language', "Python")
    print_sorted_dictionary(new_dict)
    print("--")
    print_sorted_dictionary(a_dictionary)

    print("--")
    print("--")

    new_dict = update_dictionary(a_dictionary, 'city', "San Francisco")
    print_sorted_dictionary(new_dict)
    print("--")
    print_sorted_dictionary(a_dictionary)
