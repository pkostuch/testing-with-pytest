from dataclasses import dataclass
from typing import List

from service.item import Item


@dataclass
class Order:
    name: str
    items: List[Item]

    def total(self) -> float:
        return sum(item.total() for item in self.items)
