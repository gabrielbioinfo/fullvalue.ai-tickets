"""API endpoints for handling bar data.

This module defines FastAPI routes for posting bar batches to Redis.
"""

from typing import Annotated

from fastapi import APIRouter, Depends

from app.entities.barbatch import BarBatch
from app.repository.bar_repository import BarRepository, get_bar_repository

router = APIRouter()


@router.post("/bars")
async def post_bars(batch: BarBatch, repo: Annotated[BarRepository, Depends(get_bar_repository)]) -> dict:
    """Accept a batch of bar data and push each bar to Redis.

    Parameters
    ----------
    batch : BarBatch
        The batch of bar data to be processed.
    repo : BarRepository
        Repository for saving bars in Redis.

    Returns
    -------
    dict
        A dictionary containing the number of accepted bars.

    """
    for it in batch.items:
        await repo.save_bar(it.model_dump())
    return {"accepted": len(batch.items)}
