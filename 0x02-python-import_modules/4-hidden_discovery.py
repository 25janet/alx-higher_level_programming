#!/usr/bin/python3

if __name__ == "__main__":
    # Print all names defined by the hidden_4 module.

    # Import the hidden_4 module
    import hidden_4

    # Get a list of all names defined in the module
    names = dir(hidden_4)

    # Iterate through the names and print those that do not start with "__"
    for name in names:
        if not name.startswith("__"):
            print(name)
