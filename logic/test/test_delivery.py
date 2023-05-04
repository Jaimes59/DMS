import unittest
from logic.classes.person import Person
from logic.classes.delivery import Delivery

class TestDelivery(unittest.TestCase):
    def setUp(self):
        self.buyer = Person(id=1, name='John', surname='Doe')
        self.delivery = Delivery(buyer=self.buyer, deliver_id=123, date='2023-05-03')

    def test_instance(self):
        self.assertIsInstance(self.delivery, Delivery, "It's instance!")

    def test_buyer(self):
        self.assertEqual(self.delivery.buyer, self.buyer)

    def test_deliver_id(self):
        self.assertEqual(self.delivery.deliver_id, 123)

    def test_date(self):
        self.assertEqual(self.delivery.date, '2023-05-03')

    def test_str(self):
        self.assertEqual(str(self.delivery), "{'ID': 123, 'Date': '2023-05-03', 'Buyer': {'id': 1, 'name': 'John', 'surname': 'Doe'}}")

    def test_eq(self):
        other_delivery = Delivery(buyer=self.buyer, deliver_id=123, date='2023-05-03')
        self.assertEqual(self.delivery, other_delivery)

if __name__ == '__main__':
    unittest.main()
