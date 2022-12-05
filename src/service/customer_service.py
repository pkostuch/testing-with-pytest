from typing import Optional

from service.customer import Customer


class PaymentError(Exception):
    pass

class CustomerService:

    def __init__(self):
        self.__customers = {
            'Alice': Customer('Alice', 85.43, 11),
            'Bob': Customer('Bob', 100.0, 0),
        }

    def find_customer(self, name: str) -> Optional[Customer]:
        return self.__customers.get(name, None)

    def charge_customer(self, name: str, value: float) -> None:
        customer = self.__customers.get(name, None)
        if not customer:
            raise PaymentError
        customer.balance = customer.balance - value
        return True

