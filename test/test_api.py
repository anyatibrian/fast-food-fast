import unittest
import json
from app import app

orders = {
    "deliveryType": "self",
    "food": "fish",
    "location": "lira",
    "orderID": 1,
    "orderStatus": "pending",
    "pieces": "1",
    "username": "brian"
}


class TestEndPoints(unittest.TestCase):
    # checking whether the post was made
    def test_post_order_endpoints(self):
        test_client = app.test_client(self)
        response = test_client.post('/orders', content_type='html/text', data=json.dumps(orders))
        self.assertEqual(response.status_code, 201)

    def test_loaded_post_page(self):
        # checking were the posting of data was made
        test_client = app.test_client(self)
        response = test_client.post('/orders', content_type='html/text', data=json.dumps(orders))
        self.assertTrue(b'the your order has been placed' in response.data)

    def test_get_all_orders_endPoints(self):
        test_client = app.test_client(self)
        # making post in order to get data
        response = test_client.post('/orders', content_type='html/text', data=json.dumps(orders))
        self.assertEqual(response.status_code, 201)
        # getting response that has been posted
        response = test_client.post('/orders', content_type='html/text', data=json.dumps(orders))
        self.assertEqual(response.status_code, 201)

    def test_put_request_for_order_endpoints(self):
        # posting data before editing it
        test_client = app.test_client(self)
        response = test_client.post('/orders', content_type='html/text', data=json.dumps(orders))
        self.assertEqual(response.status_code, 201)
        # edit data using the put request
        response = test_client.get('/orders/1')
        self.assertEqual(response.status_code, 200)

    def test_check_whether_order_notExist(self):
        test_client = app.test_client(self)
        response = test_client.get('/orders/0')
        self.assertTrue(b'the order does not exist' in response.data)

    def test_put_request_for_endPoints(self):
        # editing each order
        test_client = app.test_client(self)
        response = test_client.put('orders/0', data=json.dumps(dict(orderStaus="orderStatus")))
        self.assertTrue(response.status, 200)

    def testing_no_order_in_the_list(self):
        # checking whether data exist or not
        test_client = app.test_client(self)
        response = test_client.put('orders/0', data=json.dumps(dict(orderStaus="orderStatus")))
        self.assertTrue(b'the order does not exist' in response.data)


if __name__ == '__main__':
    unittest.run()
