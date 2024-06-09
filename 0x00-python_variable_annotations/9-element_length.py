#!/usr/bin/env python3
"""
a properly annotated function
"""
from typing import Tuple, List, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    properly annotated function"""
    return [(i, len(i)) for i in lst]
