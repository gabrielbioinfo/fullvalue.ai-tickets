"""Async Redis client utilities for setting and getting key-value pairs.

This module provides functions to interact with Redis using asyncio.
"""

from redis.asyncio import Redis

from app.core.app_config import config

redis_client = Redis(
    host=config.redis_host,
    port=config.redis_port,
    db=config.redis_db,
)


async def set_value(key: str, value: str) -> None:
    """Set a value for a given key in Redis asynchronously.

    Parameters
    ----------
    key : str
        The key to set in Redis.
    value : str
        The value to associate with the key.

    Returns
    -------
    None

    """
    await redis_client.set(key, value)


async def get_value(key: str) -> str | None:
    """Get the value associated with a given key from Redis asynchronously.

    Parameters
    ----------
    key : str
        The key to retrieve from Redis.

    Returns
    -------
    str or None
        The value associated with the key, or None if the key does not exist.

    """
    return await redis_client.get(key)
