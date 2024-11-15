from collections import defaultdict


class OrderBook:
    def __init__(self):
        self.order_id_map = {}
        self.buy_orders = defaultdict(list)   
        self.sell_orders = defaultdict(list)  
    
    def add_order(self, order):
        self.order_id_map[order.id] = order
        order_book = self.buy_orders if order.order_type == 'Buy' else self.sell_orders
        order_book[order.price].append(order)
    
    def remove_order(self, order):
        existing_order = self.order_id_map.pop(order.id, None)
        if not existing_order:
            raise KeyError(f"Order ID {order.id} not found.")
        
        order_book = self.buy_orders if order.order_type == 'Buy' else self.sell_orders
        orders_at_price = order_book.get(order.price, [])
        order_book[order.price] = [o for o in orders_at_price if o.id != order.id]
        if not order_book[order.price]:
            del order_book[order.price]
    
    def get_best_buy_order(self):
        if self.buy_orders:
            best_buy_price = max(self.buy_orders.keys())
            total_buy_quantity = sum(o.quantity for o in self.buy_orders[best_buy_price])
            return best_buy_price, total_buy_quantity
        else:
            return None, 0
    
    def get_best_sell_order(self):
        if self.sell_orders:
            best_sell_price = min(self.sell_orders.keys())
            total_sell_quantity = sum(o.quantity for o in self.sell_orders[best_sell_price])
            return best_sell_price, total_sell_quantity
        else:
            return None, 0
    
    def display_best_orders(self):
        best_buy_price, total_buy_quantity = self.get_best_buy_order()
        if best_buy_price is not None:
            print(f"Best Buy Order: Price {best_buy_price}, Total Quantity {total_buy_quantity}")
        else:
            print("No Buy Orders.")
        
        best_sell_price, total_sell_quantity = self.get_best_sell_order()
        if best_sell_price is not None:
            print(f"Best Sell Order: Price {best_sell_price}, Total Quantity {total_sell_quantity}")
        else:
            print("No Sell Orders.")