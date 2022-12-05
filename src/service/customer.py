from dataclasses import dataclass


@dataclass
class Customer:
    name: str
    balance: float
    points: int
