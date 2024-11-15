import unittest

from orders.order import Order
from orders.order_book import OrderBook


class TestOrderBook(unittest.TestCase):
    def setUp(self):
        self.order_book = OrderBook()
        self.order1 = Order('001', 'Buy', 'Add', 20.00, 100)
        self.order2 = Order('002', 'Sell', 'Add', 25.00, 200)
        self.order3 = Order('003', 'Buy', 'Add', 23.00, 50)
    
    def test_add_order(self):
        self.order_book.add_order(self.order1)
        self.assertIn('001', self.order_book.order_id_map)
        self.assertIn(20.00, self.order_book.buy_orders)
        self.assertEqual(len(self.order_book.buy_orders[20.00]), 1)
    
    def test_remove_order(self):
        self.order_book.add_order(self.order1)
        self.order_book.remove_order(self.order1)
        self.assertNotIn('001', self.order_book.order_id_map)
        self.assertNotIn(20.00, self.order_book.buy_orders)
    
    def test_best_buy_order(self):
        self.order_book.add_order(self.order1)
        self.order_book.add_order(self.order3)
        best_buy_price, total_buy_quantity = self.order_book.get_best_buy_order()
        self.assertEqual(best_buy_price, 23.00)
        self.assertEqual(total_buy_quantity, 50)
    
    def test_best_sell_order(self):
        self.order_book.add_order(self.order2)
        best_sell_price, total_sell_quantity = self.order_book.get_best_sell_order()
        self.assertEqual(best_sell_price, 25.00)
        self.assertEqual(total_sell_quantity, 200)
    
    def test_remove_nonexistent_order(self):
        with self.assertRaises(KeyError):
            self.order_book.remove_order(self.order1)

if __name__ == '__main__':
    unittest.main()
