order_collection = []


class Orders:
    def __init__(self, username, food, location, delivery_type, pieces, orderStatus='pending'):
        self.username = username
        self.food = food
        self.location = location
        self.delivery_type = delivery_type
        self.pieces = pieces
        self.orderStatus = orderStatus

    def validate_string(self):
        if not isinstance(self.username, str) \
                or not isinstance(self.food, str) \
                or not isinstance(self.location, str) \
                or not isinstance(self.delivery_type, str) \
                or not isinstance(self.orderStatus, str)\
                or not isinstance(self.pieces, str):
            return True

    def covert_json(self):
        if not isinstance(self.username, str):
            return "error string"
        orders = {
            "orderID": len(order_collection) + 1,
            "username": self.username,
            "food": self.food,
            "location": self.location,
            "deliveryType": self.delivery_type,
            "pieces": self.pieces,
            "orderStatus": self.orderStatus
        }
        order_collection.append(orders)
        return order_collection
