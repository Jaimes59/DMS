import unittest
from logic.classes.address import Address

class TestAddress(unittest.TestCase):
    address = Address(country="Colombia", department="Atlántico", city="Barranquilla",
                      post_code="080001", neighborhood="El Prado", street="Carrera 53 # 74-62",
                      complement="Apto 401")

    def test_instance(self):
        self.assertIsInstance(self.address, Address, "Its instance!")

    def test_country(self):
        self.assertEqual(self.address.country, "Colombia")

    def test_department(self):
        self.assertEqual(self.address.department, "Atlántico")

    def test_city(self):
        self.assertEqual(self.address.city, "Barranquilla")

    def test_post_code(self):
        self.assertEqual(self.address.post_code, "080001")

    def test_neighborhood(self):
        self.assertEqual(self.address.neighborhood, "El Prado")

    def test_street(self):
        self.assertEqual(self.address.street, "Carrera 53 # 74-62")

    def test_complement(self):
        self.assertEqual(self.address.complement, "Apto 401")

    def test_str(self):
        self.assertEqual(str(self.address), '{"country": "Colombia", "department": "Atlántico", "city": "Barranquilla", "post_code": "080001", "neighborhood": "El Prado", "street": "Carrera 53 # 74-62", "complement": "Apto 401"}')

if __name__ == '__main__':
    unittest.main()
