#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

# Extract the last digit of the number
last_digit = abs(number) % 10

# Check if the last digit is greater than 5, equal to 0,
# Or less than 6 and not 0

if last_digit > 5:
    result = "and is greater than 5"
elif last_digit == 0:
    result = "and is 0"
else:
    result = "and is less than 6 and not 0"

# Print the output
print(f"Last digit of {number} is {last_digit} {result}")
