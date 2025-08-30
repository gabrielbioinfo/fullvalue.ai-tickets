"""Bar repository module for managing bar data in Redis.

Provides the BarRepository class for saving and retrieving bars.
"""

import ast
from typing import Any

from redis.asyncio import Redis

from app.core.redis import redis_client


def get_bar_repository() -> "BarRepository":
    """Dependency provider for BarRepository."""
    return BarRepository(redis_client)


class BarRepository:
    """Repository for managing bar data in Redis.

    Provides methods to save and retrieve bar data using a Redis list.
    """

    def __init__(self, redis_client: Redis, redis_key: str = "bars") -> None:
        """Initialize BarRepository with a Redis client and key.

        Args:
            redis_client: The Redis client instance.
            redis_key: The Redis key to store bar data (default: "bars").

        """
        self.redis_client = redis_client
        self.redis_key = redis_key

    async def save_bar(self, bar: dict[str, Any]) -> None:
        """Save a bar to the Redis list.

        Args:
            bar: A dictionary containing bar data.

        """
        await self.redis_client.rpush(self.redis_key, str(bar))

    async def get_bars(self, start: int = 0, end: int = -1) -> list[dict[str, Any]]:
        """Retrieve bars from the Redis list.

        Args:
            start: The starting index of the range (default: 0).
            end: The ending index of the range (default: -1, meaning all items).

        Returns:
            A list of dictionaries containing bar data.

        """
        items = await self.redis_client.lrange(self.redis_key, start, end)
        return [ast.literal_eval(item) for item in items]  # Use json.loads se salvar como JSON
