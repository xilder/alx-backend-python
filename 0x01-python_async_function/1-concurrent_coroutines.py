#!/usr/bin/python3
"""
a function that returns a list of delays
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    calls wait_random n times
    """

    return sorted(await asyncio.gather(*[wait_random(max_delay) for _ in range(n)]))
