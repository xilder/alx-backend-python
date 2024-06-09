#!/usr/bin/env python3
"""
function returns the first element of the list
"""
from typing import Union, Sequence, Any
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    if lst:
        return lst[0]
    else:
        return None
