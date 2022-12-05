from service.customer_service import CustomerService
from service.order import Order


class InvalidCustomerError(Exception):
    pass


class OrderService:

    def __init__(self):
        self.__customer_service = CustomerService()

    def create_order(self, customer_name: str, order: Order) -> bool:
        customer = self.__customer_service.find_customer(customer_name)
        if not customer:
            raise InvalidCustomerError()
        total = order.total()
        if customer.points > 10 or total > 200:
            total *= 0.95
        if customer.balance < total:
            return False
        self.__customer_service.charge_customer(customer_name, total)
        return True

