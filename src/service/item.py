from dataclasses import dataclass


@dataclass
class Item:
    name: str
    cost: float
    quantity: int

    def total(self) -> float:
        return self.cost * self.quantity
