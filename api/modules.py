order_collection = []


class Orders:
    def __init__(self, username, food, location, delivery_type, pieces, orderStatus='pending'):
        self.username = username
        self.food = food
        self.location = location
        self.delivery_type = delivery_type
        self.pieces = pieces
        self.orderStatus = orderStatus

    def validate_orders(self, orders):
        if "username" in orders and "food " in orders and "location" in orders \
                and "deliveryType" in orders and "pieces" \
                in orders and "orderStatus" in orders:
            return True
        else:
            return False

    def covert_json(self):
        orders = {
            "orderID": len(order_collection)+1,
            "username": self.username,
            "food": self.food,
            "location": self.location,
            "deliveryType": self.delivery_type,
            "pieces": self.pieces,
            "orderStatus": self.orderStatus
        }
        order_collection.append(orders)
        return order_collection


