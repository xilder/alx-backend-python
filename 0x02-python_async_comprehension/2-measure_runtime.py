#!/usr/bin/env python3
"""
Measures the runtime for the function async_comprehension
"""
import asyncio
from time import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    measure_time async function
    """
    start = time()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    return time() - start
