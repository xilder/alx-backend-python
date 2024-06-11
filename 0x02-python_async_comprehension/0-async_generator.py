#!/usr/bin/env python3
"""
async generator that loops ten times, sleeps a scond
and yield a random number between 1 and 10
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    async generator
    """

    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
