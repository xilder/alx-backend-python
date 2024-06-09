#!/usr/bin/env python3
"""
takes an a float as an argument and returns a function that
multiplies a float by a given multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    returns a multiplier function
    """

    def multiplier_fn(n: float) -> float:
        """
        returns the product of the multiplier and n
        """
        return n * multiplier

    return multiplier_fn
