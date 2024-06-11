#!/usr/bin/python3
"""
Defines the function async_comprehension
"""
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """return 10 random number from async_generator"""
    return [i async for i in async_generator()]
