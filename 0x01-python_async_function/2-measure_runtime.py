#!/usr/bin/env python3
"""
returns the average time for the list of function in wait_n
to execute
"""
import asyncio
from time import time

wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    returns the average time for the list of function in wait_n
    to execute
    """

    start = time()
    asyncio.run(wait_n(n, max_delay))

    return (time() - start) / n
