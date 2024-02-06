#!/usr/bin/python3

# Use a loop to iterate from 0 to 99
for num in range(100):
    # Format each number to have two digits and print
    print("{:02d}".format(num), end=", " if num < 99 else "\n")
