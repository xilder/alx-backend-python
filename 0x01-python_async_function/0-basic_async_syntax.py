#!/usr/bin/env python3
"""
an async function to that generates a random number
"""
import random
import asyncio


async def wait_random(max_delay: int=10) -> float:
    """
    an async function that generates a random number
    between 0 and a max_delay
    """
    slumber = random.uniform(0, max_delay)
    await asyncio.sleep(slumber)
    return slumber
