from api import app
from flask import jsonify, request, make_response
from api.modules import Orders, order_collection


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({"error": "the order does not exist"}), 404)


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


@app.route('/api/v1/orders/', methods=['GET', 'POST'])
def get_orders():
    # creating an endpoint that  returns all the orders made by the user
    if len(order_collection) > 0:
        return make_response(jsonify({'orders made': order_collection}), 200)
    else:
        return make_response(jsonify({'error': 'the order does not exist'}), 404)


@app.route('/api/v1/orders/<int:orderID>', methods=['GET', 'POST'])
def get_single_order(orderID):
    # end point that enables the fetching of a particular order by the user
    orders = [order for order in order_collection if order['orderID'] == orderID]
    if len(orders) == 0:
        return make_response(jsonify({'error': 'the order does not exist'}), 404)
    return make_response(jsonify({'orders': orders[0]}), 200)


@app.route('/api/v1/orders/<int:orderID>', methods=['GET', 'PUT'])
def put_orders(orderID):
    # the end point for updating the order list
    if request.method == 'PUT':
        json_data = request.get_json(force=True)
        orders = [order for order in order_collection if order['orderID'] == orderID]
        if len(orders) == 0:
            return make_response(jsonify({'error': 'the order does not exist'}), 404)
        else:
            orders[0]['orderStatus'] = json_data['orderStatus']
            return make_response(jsonify({'message': 'successfully updated'}), 200)

    else:
        return make_response(jsonify({'error': 'request method not allowed'}), 405)


if __name__ == '__main__':
    app.run(debug=True)
