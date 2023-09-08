def add_integer(a, b=98):
    """
    Return the integer addition of a and b.

    Float arguments are typecasted to ints before addition is performed.

    Args:
        a (int or float): The first number.
        b (int or float, optional): The second number. Defaults to 98.

    Returns:
        int: The addition of a and b as integers.

    Raises:
        TypeError: If either of a or b is a non-integer and non-float.
    """
    # Check if a is an integer or float, and convert it to an integer if it's a float.
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    a = int(a)

    # Check if b is an integer or float, and convert it to an integer if it's a float.
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    b = int(b)

    # Return the addition of a and b as integers.
    return a + b
