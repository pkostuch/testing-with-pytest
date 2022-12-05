from service.item import Item
from service.order import Order
from service.order_service import OrderService


def test_create_order():
    order_service = OrderService()
    assert order_service.create_order('Bob', Order('books', [Item('Unit Tests', 15.0, 1)]))
