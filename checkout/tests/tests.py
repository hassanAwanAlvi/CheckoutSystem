import unittest
from checkout.tiny_pulse_checkout.Checkout import promotional_rules





class MyTestCase(unittest.TestCase):

    def test_input_1(self):
        order_ids = ['001', '001']
        price  = promotional_rules(order_ids)
        self.assertEqual(17, price)

    def test_input_2(self):
        order_ids = ['001', '001', '002', '003']
        price = promotional_rules(order_ids)
        self.assertEqual(73.75, price)


    def test_input_3(self):
        order_ids = ['001', '001' , '003']
        price = promotional_rules(order_ids)
        self.assertEqual(36.95, price)


