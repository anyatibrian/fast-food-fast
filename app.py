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
    if json_data['location'] == "" or json_data['food'] == "" or json_data['username'] == "" or \
            json_data['deliveryType'] == "" or json_data['pieces'] == "":
        return make_response(jsonify({"error": "some of the values are empty"}), 400)
        return make_response(jsonify({"error": "your data should only contains string"}))
    if not isinstance(json_data['username'], str):
        return make_response(jsonify({'error': 'bad string'}))
    elif not isinstance(json_data['location'], str):
        return make_response(jsonify({'error': 'bad string'}))
    elif not isinstance(json_data['deliveryType'], str):
        return make_response(jsonify({'error': 'bad string'}))
    elif not isinstance(json_data['pieces'], int):
        return make_response(jsonify({'error': ' piece should only be integers'}))

    order = Orders(username=json_data['username'], food=json_data['food'], location=json_data['location'],
                   delivery_type=json_data['deliveryType'], pieces=json_data['pieces'])
    # if order.validate_string():
    # return make_response(jsonify({'error': 'your data should only contain strings'}))
    order.covert_json()
    return make_response(jsonify({'message': 'your order has been placed'}), 201)


@app.route('/api/v1/orders/', methods=['GET'])
def get_orders():
    # creating an endpoint that  returns all the orders made by the user
    if len(order_collection) > 0:
        return make_response(jsonify({'orders made': order_collection}), 200)
    else:
        return make_response(jsonify({'error': 'the order does not exist'}), 404)


@app.route('/api/v1/orders/<int:orderID>', methods=['GET'])
def get_single_order(orderID):
    # end point that enables the fetching of a particular order by the user
    orders = [order for order in order_collection if order['orderID'] == orderID]
    if len(orders) == 0:
        return make_response(jsonify({'error': 'the order does not exist'}), 404)
    return make_response(jsonify({'orders': orders[0]}), 200)


@app.route('/api/v1/orders/<int:orderID>', methods=['PUT'])
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


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({"error": "the order does not exist"}), 404)


@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({"error": "some of the values are empty"}), 400)


if __name__ == '__main__':
    app.run(debug=True)
