"""Defines the BarBatch model for grouping multiple Bar instances."""

from pydantic import BaseModel

from app.entities.bar import Bar


class BarBatch(BaseModel):
    """A batch of Bar instances grouped by timeframe and timestamp.

    Attributes
    ----------
    items : list[Bar]
        The list of Bar instances in the batch.

    """

    items: list[Bar]
