from pydantic import BaseModel
from typing import Optional


class Order(BaseModel):
    user_id: int
    item_description: str
    item_quantity: int
    item_price: float

    @property
    def total_value(self):
        self.item_quantity * self.item_price


class OrderUpdate(BaseModel):
    item_description: Optional[str] = None
    item_quantity: Optional[int] = None
    item_price: Optional[float] = None

    @property
    def total_value(self) -> float:
        self.item_quantity * self.item_price
