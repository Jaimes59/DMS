import unittest
from logic.classes.person import Person

class TestPerson(unittest.TestCase):
    person = Person(id_person=1, name='John', last_name='Doe', phone='1234567890', mail='john.doe@example.com')

    def test_instance(self):
        self.assertIsInstance(self.person, Person, "Its instance!")

    def test_id_person(self):
        self.assertEqual(self.person.id_person, 1)

    def test_name(self):
        self.assertEqual(self.person.name, "John")

    def test_last_name(self):
        self.assertEqual(self.person.last_name, 'Doe')

    def test_phone(self):
        self.assertEqual(self.person.phone, '1234567890')

    def test_mail(self):
        self.assertEqual(self.person.mail, 'john.doe@example.com')

    def test__str__(self):
        self.assertEqual(str(self.person), '{"Person": 1, "Name": "John", "Last Name": "Doe", "Phone": "1234567890", "Mail": "john.doe@example.com"}')
        
if __name__ == '__main__':
    unittest.main()
