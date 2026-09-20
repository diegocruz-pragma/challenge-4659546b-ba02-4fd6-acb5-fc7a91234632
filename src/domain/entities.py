from typing import Literal

from pydantic import BaseModel, Field


class Payment(BaseModel):
    amount: float = Field(gt=0)
    currency: Literal["EUR", "GBP", "USD"]
