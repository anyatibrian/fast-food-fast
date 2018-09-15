import unittest
from api.modules import Orders


class TestOrders(unittest.TestCase):
    def test_order_module(self):
        order = Orders("self", "fish", "lira", "pending", "1", "brian")
