import unittest
from logic.classes.person import Person
from logic.classes.edelivery import EDelivery

class TestEDelivery(unittest.TestCase):
    def setUp(self):
        self.buyer = Person(id=1, name='Name', surname='Surname')
        self.delivery = EDelivery(buyer=self.buyer, deliver_id=1, date='2023-05-03', deliver_mail='example@example.com')

    def test_instance(self):
        self.assertIsInstance(self.delivery, EDelivery, "It's an instance of EDelivery!")

    def test_buyer(self):
        self.assertEqual(self.delivery.buyer, self.buyer)

    def test_id(self):
        self.assertEqual(self.delivery.deliver_id, 1)

    def test_date(self):
        self.assertEqual(self.delivery.date, '2023-05-03')

    def test_deliver_mail(self):
        self.assertEqual(self.delivery.deliver_mail, 'example@example.com')

    def test_send_document(self):
        self.assertEqual(self.delivery.sendDocument(), None)

    def test__str__(self):
        self.assertEqual(self.delivery.__str__(), {"ID": 1, "Date": '2023-05-03', "Email": 'example@example.com'})

    def test__eq__(self):
        delivery2 = EDelivery(buyer=self.buyer, deliver_id=1, date='2023-05-03', deliver_mail='example@example.com')
        self.assertEqual(self.delivery, delivery2)

if __name__ == '__main__':
    unittest.main()
