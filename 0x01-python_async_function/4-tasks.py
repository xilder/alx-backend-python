#!/usr/bin/env python3
"""
a function that returns a list of delays
"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    calls wait_random n times
    """
    results = await asyncio.gather(
        *[task_wait_random(max_delay) for _ in range(n)])

    return sorted(results)
