#!/usr/bin/python3

# Create a list of lowercase letters excluding 'e' and 'q'
alphabet = [chr(char) for char in range(97, 123) if char not in [101, 113]]

# Print the alphabet without newlines
print("".join(alphabet), end="")
