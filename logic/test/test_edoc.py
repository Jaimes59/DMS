import unittest
from logic.classes.edoc import Edoc

class TestEdoc(unittest.TestCase):
    doc = Edoc(id=1, author='Author', title='Title', price=10.5, topic='Topic', language='eng', pub_date='2022-04-20', size=2.5, doi='doi')

    def test_instance(self):
        self.assertIsInstance(self.doc, Edoc, "Its instance!")

    def test_id(self):
        self.assertEqual(self.doc.id, 1)

    def test_author(self):
        self.assertEqual(self.doc.author, 'Author')

    def test_title(self):
        self.assertEqual(self.doc.title, 'Title')

    def test_price(self):
        self.assertEqual(self.doc.price, 10.5)

    def test_topic(self):
        self.assertEqual(self.doc.topic, 'Topic')

    def test_language(self):
        self.assertEqual(self.doc.language, 'eng')

    def test_pub_date(self):
        self.assertEqual(self.doc.pub_date, '2022-04-20')

    def test_size(self):
        self.assertEqual(self.doc.size, 2.5)

    def test_doi(self):
        self.assertEqual(self.doc.doi, 'doi')

    def test_lease(self):
        self.assertEqual(self.doc.lease(5), 52.5)

    def test__str__(self):
        self.assertEqual(self.doc.__str__(), {'ID': 1, 'Author': 'Author', 'Title': 'Title', 'Price': 10.5, 'Topic': 'Topic', 'Language': 'eng', 'Publication Date': '2022-04-20', 'Size': 2.5, 'DOI': 'doi'})

    def test_eq(self):
        doc2 = Edoc(id=1, author='Author', title='Title', price=10.5, topic='Topic', language='eng', pub_date='2022-04-20', size=2.5, doi='doi')
        self.assertEqual(self.doc, doc2)

if __name__ == '__main__':
    unittest.main()
