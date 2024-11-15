class Order:
    VALID_ORDER_TYPES = {'Buy', 'Sell'}
    VALID_OPERATIONS = {'Add', 'Remove'}
    
    def __init__(self, id, order_type, operation, price, quantity):
        if order_type not in self.VALID_ORDER_TYPES:
            raise ValueError(f"Invalid order type: {order_type}")
        if operation not in self.VALID_OPERATIONS:
            raise ValueError(f"Invalid operation: {operation}")
        
        self.id = id
        self.order_type = order_type # Buy Sell
        self.operation = operation  # Add Remove
        self.price = price
        self.quantity = quantity