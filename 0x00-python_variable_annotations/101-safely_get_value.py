#!/usr/bin/env python3
"""
Defines the annotated function safely_get_value
"""
from typing import TypeVar, Mapping, Union, Any


T = TypeVar("T")


def safely_get_value(
    dct: Mapping,
    key: Any,
    default: Union[T, None] = None
) -> Union[Any, T]:
    """
    Returns a value from a dictionary if it exists,
    else returns None
    """
    if key in dct:
        return dct[key]
    else:
        return default
    