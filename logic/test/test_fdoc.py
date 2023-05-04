import unittest
from logic.classes.document import Fdoc


class TestFdoc(unittest.TestCase):
    def setUp(self):
        self.fdoc1 = Fdoc(id_doc=1, author='John Doe', title='Title', price=9.99, topic='Topic', language='eng', publisher='Publisher')

    def test_instance(self):
        self.assertIsInstance(self.fdoc1, Fdoc, "It's an instance of Fdoc!")

    def test_id_doc(self):
        self.assertEqual(self.fdoc1.id_doc, 1)

    def test_author(self):
        self.assertEqual(self.fdoc1.author, 'John Doe')

    def test_title(self):
        self.assertEqual(self.fdoc1.title, 'Title')

    def test_price(self):
        self.assertEqual(self.fdoc1.price, 9.99)

    def test_topic(self):
        self.assertEqual(self.fdoc1.topic, 'Topic')

    def test_language(self):
        self.assertEqual(self.fdoc1.language, 'eng')

    def test_publisher(self):
        self.assertEqual(self.fdoc1.publisher, 'Publisher')

    def test_str(self):
        self.assertEqual(str(self.fdoc1), "{'ID': 1, 'Author': 'John Doe', 'Title': 'Title', 'Price': 9.99, 'Topic': 'Topic', 'Language': 'eng', 'Publisher': 'Publisher'}")

    def test_eq(self):
        fdoc2 = Fdoc(id_doc=1, author='John Doe', title='Title', price=9.99, topic='Topic', language='eng', publisher='Publisher')
        self.assertEqual(self.fdoc1, fdoc2)


if __name__ == '__main__':
    unittest.main()
