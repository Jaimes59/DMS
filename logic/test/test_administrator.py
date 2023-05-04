import unittest
from logic.classes.administrator import Administrator


class TestAdministrator(unittest.TestCase):
    admin = Administrator(id_person=1, name='Name', last_name='Surname', phone='123456789', mail='test@test.com')

    def test_instance(self):
        self.assertIsInstance(self.admin, Administrator, "It's an instance of the Administrator class!")

    def test_id_person(self):
        self.assertEqual(self.admin.id_person, 1)

    def test_name(self):
        self.assertEqual(self.admin.name, "Name")

    def test_last_name(self):
        self.assertEqual(self.admin.last_name, "Surname")

    def test_phone(self):
        self.assertEqual(self.admin.phone, "123456789")

    def test_mail(self):
        self.assertEqual(self.admin.mail, "test@test.com")

    def test_addDocument(self):
        self.assertIsNone(self.admin.addDocument(), "addDocument method works fine!")

    def test_deleteDocument(self):
        self.assertIsNone(self.admin.deleteDocument(), "deleteDocument method works fine!")

    def test_modifyDocument(self):
        self.assertIsNone(self.admin.modifyDocument(), "modifyDocument method works fine!")

    def test__str__(self):
        self.assertEqual(self.admin.__str__(), {"Admin ID": 1, "Admin name": "Name", "Admin last name": "Surname",
                                                "Admin phone": "123456789", "Admin mail": "test@test.com"})

    def test__eq__(self):
        admin2 = Administrator(id_person=1, name='Name', last_name='Surname', phone='123456789', mail='test@test.com')
        admin3 = Administrator(id_person=2, name='Name2', last_name='Surname2', phone='987654321', mail='test2@test.com')
        self.assertTrue(self.admin == admin2, "The two objects are equal!")
        self.assertFalse(self.admin == admin3, "The two objects are not equal!")


if __name__ == '__main__':
    unittest.main()
