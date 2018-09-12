import json
from fastfoodfast import app

json_data = {"username": "brian", "deliveryType": "self", "food": "fish", "location": "lira", "orderID": 4,
             "orderStatus": "pending", "pieces": "1"}


def test_post_orders():
    # test case for the post request
    with app.test_client() as test_client:
        res = test_client.post('/orders', json=json_data)
    res.get_json()
    assert res.status_code == 200


def test_get_orders():
    # test case for the get request
    with app.test_client() as test_client:
        # make a post request to the page
        get_res = test_client.post('/orders', json=json_data)
        assert get_res.status_code == 200
        # make a get request to the page
        get_res = test_client.get('/orders')
        assert get_res.status_code == 200


def test_put_order():
    # test case for the put request
    with app.test_client() as test_client:
        edit_order = test_client.post('/orders', json=json_data)
        assert edit_order.status_code == 200
        edit_order = test_client.put('/orders/1', json={"orderStatus": "completed"})
        assert edit_order.status_code == 200


def test_get_single_order():
    # testing the put request
    with app.test_client() as test_client:
        get_single_order = test_client.post('/orders', json=json_data)
        assert get_single_order.status_code == 200
        get_single_order = test_client.get('/orders/4', follow_redirects=True)
        assert get_single_order.status_code == 200
        assert b'viewing single item', get_single_order.data