from api import app
from flask import jsonify, request, make_response
from api.modules import Orders, order_collection


@app.route('/', methods=['GET'])
def get_index():
    return make_response(jsonify({'message': 'hi there your welcome to fast food fast'}))


@app.route('/api/v1/orders', methods=['POST'])
def post_orders():
    # function that allow making of orders
    json_data = request.get_json(force=True)
    order = Orders(username=json_data['username'], food=json_data['food'], location=json_data['location'],
                   delivery_type=json_data['deliveryType'], pieces=json_data['pieces'])
    order.covert_json()
    return make_response(jsonify({'message': 'the your order has been placed'}), 201)


@app.route('/api/v1/orders', methods=['GET'])
def get_orders():
    # creating an endpoint to return all the orders made by the user
    if len(order_collection) > 0:
        return make_response(jsonify({'orders made': order_collection}), 200)
    else:
        return make_response(jsonify({'orders made': 'you dont have any orders yet'}), 204)


@app.route('/api/v1/orders/<int:orderID>', methods=['GET'])
def get_single_order(orderID):
    # end point that enables the fetching of a single order by the user
    if request.method == 'GET':
        if orderID != 0:
            orders = [order for order in order_collection if order['orderID'] == orderID]
            return make_response(jsonify({'orders': orders[0]}), 200)
        else:
            return make_response(jsonify({'error': 'the order does not exist'}), 404)
    return make_response(jsonify({'error': 'request method not allowed'}), 405)


@app.route('/api/v1/orders/<int:orderID>', methods=['PUT'])
def put_orders(orderID):
    # the end point for updating the order list
    if request.method == 'PUT':
        json_data = request.get_json(force=True)
        if orderID != 0:
            orders = [order for order in order_collection if order['orderID'] == orderID]
            orders[0]['orderStatus'] = json_data['orderStatus']
            return make_response(jsonify({'orders': orders[0]}))
        else:
            return make_response(jsonify({'error': 'the order does not exist'}), 404)

    else:
        return make_response(jsonify({'error': 'request method not allowed'}), 405)


if __name__ == '__main__':
    app.run(debug=True)
