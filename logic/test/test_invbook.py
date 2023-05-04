import unittest
from logic.classes.invbook import InvBook


class TestInvBook(unittest.TestCase):

    def setUp(self):
        self.book = InvBook(id_doc=1, author='Author', title='Title', price=10.99,
                            topic='Topic', language='eng', pub_date='2022-01-01',
                            size=2.5, doi='doi', pages=250, abstract='Abstract')

    def test_instance(self):
        self.assertIsInstance(self.book, InvBook, "Its instance!")

    def test_id(self):
        self.assertEqual(self.book.id_doc, 1)

    def test_author(self):
        self.assertEqual(self.book.author, 'Author')

    def test_title(self):
        self.assertEqual(self.book.title, 'Title')

    def test_price(self):
        self.assertAlmostEqual(self.book.price, 10.99, places=2)

    def test_topic(self):
        self.assertEqual(self.book.topic, 'Topic')

    def test_language(self):
        self.assertEqual(self.book.language, 'eng')

    def test_pub_date(self):
        self.assertEqual(self.book.pub_date, '2022-01-01')

    def test_size(self):
        self.assertAlmostEqual(self.book.size, 2.5, places=2)

    def test_doi(self):
        self.assertEqual(self.book.doi, 'doi')

    def test_pages(self):
        self.assertEqual(self.book.pages, 250)

    def test_abstract(self):
        self.assertEqual(self.book.abstract, 'Abstract')

    def test__str__(self):
        self.assertEqual(self.book.__str__(), {'id': 1, 'Author': 'Author', 'Title': 'Title', 'Price': 10.99, 'Topic': 'Topic', 'Language': 'eng', 'Publication Date': '2022-01-01', 'Size': 2.5, 'DOI': 'doi', 'Pages': 250, 'Abstract': 'Abstract'})

    def test_eq(self):
        book2 = InvBook(id_doc=1, author='Author', title='Title', price=10.99,
                        topic='Topic', language='eng', pub_date='2022-01-01',
                        size=2.5, doi='doi', pages=250, abstract='Abstract')
        book3 = InvBook(id_doc=2, author='Author', title='Title', price=10.99,
                        topic='Topic', language='eng', pub_date='2022-01-01',
                        size=2.5, doi='doi', pages=250, abstract='Abstract')
        self.assertEqual(self.book, book2)
        self.assertNotEqual(self.book, book3)


if __name__ == '__main__':
    unittest.main()
