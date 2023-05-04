import unittest
from logic.classes.book import Book


class TestBook(unittest.TestCase):
    def setUp(self):
        self.book = Book(id_doc=1, author='Author', title='Title', price=10.0,
                          topic='Topic', language='eng', publisher='Publisher',
                          editor='Editor', pages=100, synopsis='Synopsis',
                          presentation='Presentation')

    def test_instance(self):
        self.assertIsInstance(self.book, Book, "Its instance!")

    def test_id(self):
        self.assertEqual(self.book.id_doc, 1)

    def test_author(self):
        self.assertEqual(self.book.author, 'Author')

    def test_title(self):
        self.assertEqual(self.book.title, 'Title')

    def test_price(self):
        self.assertAlmostEqual(self.book.price, 10.0)

    def test_topic(self):
        self.assertEqual(self.book.topic, 'Topic')

    def test_language(self):
        self.assertEqual(self.book.language, 'eng')

    def test_publisher(self):
        self.assertEqual(self.book.publisher, 'Publisher')

    def test_editor(self):
        self.assertEqual(self.book.editor, 'Editor')

    def test_pages(self):
        self.assertEqual(self.book.pages, 100)

    def test_synopsis(self):
        self.assertEqual(self.book.synopsis, 'Synopsis')

    def test_presentation(self):
        self.assertEqual(self.book.presentation, 'Presentation')

    def test__str__(self):
        self.assertEqual(self.book.__str__(), {'ID': 1,
                                               'Author': 'Author',
                                               'Title': 'Title',
                                               'Price': 10.0,
                                               'Topic': 'Topic',
                                               'Language': 'eng',
                                               'Publisher': 'Publisher',
                                               'Editor': 'Editor',
                                               'Pages': 100,
                                               'Synopsis': 'Synopsis',
                                               'Presentation': 'Presentation'})

    def test_eq(self):
        book1 = Book(id_doc=1, author='Author', title='Title', price=10.0,
                     topic='Topic', language='eng', publisher='Publisher',
                     editor='Editor', pages=100, synopsis='Synopsis',
                     presentation='Presentation')
        book2 = Book(id_doc=2, author='Author', title='Title', price=10.0,
                     topic='Topic', language='eng', publisher='Publisher',
                     editor='Editor', pages=100, synopsis='Synopsis',
                     presentation='Presentation')
        self.assertEqual(self.book, book1)
        self.assertNotEqual(self.book, book2)

if __name__ == '__main__':
    unittest.main()
