"""
This module contains a function to compute the sum of squares of two numbers.
"""

import math


def messy_func(x: float, y: float) -> float:
    """
    Returns the sum of squares of x and y.

    Args:
        x (float): The first number.
        y (float): The second number.

    Returns:
        float: Sum of x squared and y squared.
    """
    return math.pow(x, 2) + math.pow(y, 2)


print(messy_func(3, 4))
