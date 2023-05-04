import unittest
from logic.classes.magazine import Magazine


class TestMagazine(unittest.TestCase):
    magazine = Magazine(id_doc=1, author='Author', title='Title', price=2.99, topic='Topic', language='eng',
                        pub_date='2022-01-01', size=10.0, doi='doi', edition=2, pages=50)

    def test_instance(self):
        self.assertIsInstance(self.magazine, Magazine, "It's instance!")

    def test_id(self):
        self.assertEqual(self.magazine.id_doc, 1)

    def test_author(self):
        self.assertEqual(self.magazine.author, 'Author')

    def test_title(self):
        self.assertEqual(self.magazine.title, 'Title')

    def test_price(self):
        self.assertEqual(self.magazine.price, 2.99)

    def test_topic(self):
        self.assertEqual(self.magazine.topic, 'Topic')

    def test_language(self):
        self.assertEqual(self.magazine.language, 'eng')

    def test_pub_date(self):
        self.assertEqual(self.magazine.pub_date, '2022-01-01')

    def test_size(self):
        self.assertEqual(self.magazine.size, 10.0)

    def test_doi(self):
        self.assertEqual(self.magazine.doi, 'doi')

    def test_edition(self):
        self.assertEqual(self.magazine.edition, 2)

    def test_pages(self):
        self.assertEqual(self.magazine.pages, 50)

    def test__str__(self):
        self.assertEqual(str(self.magazine), {'id': 1, 'Author': 'Author', 'Title': 'Title', 'Price': 2.99,
                                              'Topic': 'Topic', 'Language': 'eng', 'Publication Date': '2022-01-01',
                                              'Size': 10.0, 'DOI': 'doi', 'Edition': 2, 'Pages': 50})

    def test__eq__(self):
        magazine2 = Magazine(id_doc=1, author='Author', title='Title', price=2.99, topic='Topic', language='eng',
                             pub_date='2022-01-01', size=10.0, doi='doi', edition=2, pages=50)
        magazine3 = Magazine(id_doc=2, author='Author2', title='Title2', price=3.99, topic='Topic2', language='spa',
                             pub_date='2023-01-01', size=20.0, doi='doi2', edition=1, pages=30)
        self.assertEqual(self.magazine, magazine2)
        self.assertNotEqual(self.magazine, magazine3)


if __name__ == '__main__':
    unittest.main()
