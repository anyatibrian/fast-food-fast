import unittest
from api.modules import Orders, order_collection


class TestOrders(unittest.TestCase):
    def setUp(self):
        self.order = Orders('pennina', 'fish', 'lira', 'self', '7', 'pending')
        self.single_order = order_collection

    def tearDown(self):
        pass

    def test_order_module(self):
        """ checking various instance of the orders module """
        self.assertEqual(self.order.username, 'pennina')
        self.assertEqual(self.order.food, 'fish')
        self.assertEqual(self.order.delivery_type, 'self')
        self.assertEqual(self.order.location, 'lira')
        self.assertEqual(self.order.pieces, '7')
        self.assertEqual(self.order.orderStatus, 'pending')

    def test_convert_to_json(self):
        """ checking the convert to json functions"""
        self.assertEqual(self.order.covert_json(), self.single_order)
