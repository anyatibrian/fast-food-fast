import unittest
import json
from app import app


class TestEndPoints(unittest.TestCase):
    # checking whether the post was made by a user
    def setUp(self):
        """set up method for our testing """
        self.orders = {
            "deliveryType": "self",
            "food": "fish",
            "location": "lira",
            "orderID": 1,
            "orderStatus": "pending",
            "pieces": "1",
            "username": "brian"
        }
        # setting up the test client
        self.test_client = app.test_client(self)

    def tearDown(self):
        """setting up the tear down methods to clear up test data"""
        # clearing up my array list
        self.orders.clear()

    def test_post_order_endpoints(self):
        response = self.test_client.post('/api/v1/orders', content_type='html/text', data=json.dumps(self.orders))
        self.assertEqual(response.status_code, 201)

    def test_successive_post(self):
        """checking were the posting of data was made"""
        response = self.test_client.post('/api/v1/orders', content_type='html/text', data=json.dumps(self.orders))
        self.assertTrue(b'the your order has been placed' in response.data)

    def test_get_all_orders_endPoints(self):
        """ making sure data is posted before were retrieve the all orders"""
        response = self.test_client.post('/api/v1/orders', content_type='html/text', data=json.dumps(self.orders))
        self.assertEqual(response.status_code, 201)
        """getting data posted data"""
        response = self.test_client.get('/api/v1/orders/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_order_not_found(self):
        response = self.test_client.get('/api/v1/orders', content_type='html/text')
        self.assertFalse(b'you dont have any orders yet' in response.data)

    def test_get_single_order_endpoints(self):
        """ making a post request before we can edit the list"""
        response = self.test_client.post('/api/v1/orders', content_type='html/text', data=json.dumps(self.orders))
        self.assertEqual(response.status_code, 201)
        """ making get request for single  project"""
        response = self.test_client.get('/api/v1/orders/1')
        self.assertEqual(response.status_code, 200)

    def test_check_whether_order_notExist(self):
        response = self.test_client.get('/api/v1/orders/4')
        self.assertFalse(b'you dont have any orders yet' in response.get_data())

    def test_put_request_for_endPoints(self):
        # editing each order
        response = self.test_client.put('/api/v1/orders/0', data=json.dumps(dict(orderStaus="orderStatus")))
        self.assertTrue(response.status, 200)

    def testing_no_order_in_the_list(self):
        # checking whether data exist or not
        response = self.test_client.put('/api/v1/orders/0', data=json.dumps(dict(orderStaus="orderStatus")))
        self.assertTrue(b'the order does not exist' in response.data)

    def test_index_page_loaded(self):
        response = self.test_client.get('/')
        self.assertTrue(b'hi there your welcome to fast food fast' in response.data)


if __name__ == '__main__':
    unittest.run()
