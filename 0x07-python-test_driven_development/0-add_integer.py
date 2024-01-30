#!/usr/bin/python3
"""Function that adds two integers or floats."""


def add_integer(a, b=98):
    """Return a + b.

    Floats are turned into integers before adding them.

    Raises:
        TypeError: if the passed numbers ain't no floats or integers.
    """
    if (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")
    if (not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
