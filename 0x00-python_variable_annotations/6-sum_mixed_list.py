#!/usr/bin/env python3
"""
takes in list of float and integers and adds them up
"""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """returns the sum of the list of floats and integers"""
    return float(sum(mxd_list))