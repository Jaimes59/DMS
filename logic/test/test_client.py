import unittest
from logic.classes.client import Client


class TestClient(unittest.TestCase):
    client = Client(id_person=1, name='John', last_name='Doe', phone='1234567890', mail='johndoe@example.com')

    def test_instance(self):
        self.assertIsInstance(self.client, Client, "Its instance!")

    def test_id(self):
        self.assertEqual(self.client.id_person, 1)

    def test_name(self):
        self.assertEqual(self.client.name, "John")

    def test_last_name(self):
        self.assertEqual(self.client.last_name, 'Doe')

    def test_phone(self):
        self.assertEqual(self.client.phone, '1234567890')

    def test_mail(self):
        self.assertEqual(self.client.mail, 'johndoe@example.com')

    def test_buy_history(self):
        self.assertEqual(self.client.buyHistory(), [])

    def test_lease_history(self):
        self.assertEqual(self.client.leaseHistory(), [])

    def test__str__(self):
        expected_output = "{'ID': 1, 'Name': 'John', 'Last Name': 'Doe', 'Phone': '1234567890', 'Email': 'johndoe@example.com'}"
        self.assertEqual(str(self.client), expected_output)

if __name__ == '__main__':
    unittest.main()
