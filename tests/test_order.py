import unittest

from orders.order import Order


class TestOrder(unittest.TestCase):
    def setUp(self):
        self.order = Order('001', 'Buy', 'Add', 20.00, 100)
    
    def test_order_attributes(self):
        self.assertEqual(self.order.id, '001')
        self.assertEqual(self.order.order_type, 'Buy')
        self.assertEqual(self.order.operation, 'Add')
        self.assertEqual(self.order.price, 20.00)
        self.assertEqual(self.order.quantity, 100)
    
    def test_order_type_values(self):
        with self.assertRaises(ValueError):
            Order('002', 'InvalidType', 'Add', 25.00, 200)
    
    def test_order_operation_values(self):
        with self.assertRaises(ValueError):
            Order('003', 'Buy', 'InvalidOperation', 23.00, 50)

if __name__ == '__main__':
    unittest.main()