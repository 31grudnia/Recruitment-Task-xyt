from orders.order import Order
from orders.order_book import OrderBook
from data.sample_orders import order_data

def main():
    order_book = OrderBook()

    for data in order_data:
        id, order_type, operation, price, quantity = data
        order = Order(id, order_type, operation, price, quantity)
        print(f"Processing Order ID {order.id}: {order.operation} {order.order_type} at {order.price} for {order.quantity}")
        
        if operation == 'Add':
            order_book.add_order(order)
        elif operation == 'Remove':
            order_book.remove_order(order)
        else:
            print(f"Unknown operation {operation}")

        order_book.display_best_orders()
        print('-' * 40)


if __name__ == "__main__":
    main()