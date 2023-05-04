import unittest
from logic.classes.delivery import Delivery
from logic.classes.person import Person
from logic.classes.address import Address
from logic.classes.fdelivery import FDelivery

class TestFDelivery(unittest.TestCase):
    def setUp(self):
        self.buyer = Person(id=1, name='John', surname='Doe')
        self.address = Address(street='Main Street', number='123', city='New York')
        self.contact = Person(id=2, name='Jane', surname='Doe')
        self.delivery = FDelivery(buyer=self.buyer, deliver_id=1, date='2023-05-03', address=self.address,
                                  contact=self.contact, company='ABC Inc.')

    def test_createDelivery(self):
        self.delivery.createDelivery()
        # check that createDelivery method does not raise an exception

    def test_address(self):
        new_address = Address(street='Second Street', number='456', city='Los Angeles')
        self.delivery.address = new_address
        self.assertEqual(self.delivery.address, new_address)

    def test_contact(self):
        new_contact = Person(id=3, name='Bob', surname='Smith')
        self.delivery.contact = new_contact
        self.assertEqual(self.delivery.contact, new_contact)

    def test_company(self):
        new_company = 'XYZ Corp.'
        self.delivery.company = new_company
        self.assertEqual(self.delivery.company, new_company)

    def test_str(self):
        expected_output = {"ID": 1,
                           "Date": '2023-05-03',
                           "Buyer": self.buyer,
                           "Address": self.address,
                           "Contact": self.contact,
                           "Company": 'ABC Inc.'}
        self.assertEqual(self.delivery.__str__(), expected_output)

    def test_eq(self):
        same_delivery = FDelivery(buyer=self.buyer, deliver_id=1, date='2023-05-03', address=self.address,
                                   contact=self.contact, company='ABC Inc.')
        self.assertEqual(self.delivery, same_delivery)

if __name__ == '__main__':
    unittest.main()
