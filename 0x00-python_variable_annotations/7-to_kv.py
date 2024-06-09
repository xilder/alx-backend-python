#!/usr/bin/env python3
"""
a function that returns a tuple of a string and a float
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """returns a tuple of the string and the square of the
        float or integer
    """
    return (k, v * v)
