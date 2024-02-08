#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    # Use list comprehension to get the first two integers from each tuple
    a = [tuple_a[i] if i < len(tuple_a) else 0 for i in range(2)]
    b = [tuple_b[i] if i < len(tuple_b) else 0 for i in range(2)]

    # Add the corresponding elements of the two lists
    result = (a[0] + b[0], a[1] + b[1])

    return result

if __name__ == "__main__":
    tuple_a = (1, 89)
    tuple_b = (88, 11)
    new_tuple = add_tuple(tuple_a, tuple_b)
    print(new_tuple)

    print(add_tuple(tuple_a, (1,)))
    print(add_tuple(tuple_a, ()))
