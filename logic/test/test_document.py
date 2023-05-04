import unittest
from logic.classes.document import Document


class TestDocument(unittest.TestCase):
    doc = Document(id_doc=1, author='Author', title='Title', price=9.99, topic='Topic', language='eng')

    def test_instance(self):
        self.assertIsInstance(self.doc, Document, "Its instance!")

    def test_id_doc(self):
        self.assertEqual(self.doc.id_doc, 1)

    def test_author(self):
        self.assertEqual(self.doc.author, "Author")

    def test_title(self):
        self.assertEqual(self.doc.title, 'Title')

    def test_price(self):
        self.assertAlmostEqual(self.doc.price, 9.99)

    def test_topic(self):
        self.assertEqual(self.doc.topic, 'Topic')

    def test_language(self):
        self.assertEqual(self.doc.language, 'eng')

    def test_buy(self):
        self.assertAlmostEqual(self.doc.buy(5), 49.95)

    def test__str__(self):
        self.assertEqual(str(self.doc),
                         "{'id': 1, 'Author': 'Author', 'Title': 'Title', 'Price': 9.99, 'Topic': 'Topic', "
                         "'Language': 'eng'}")


if __name__ == '__main__':
    unittest.main()
