import unittest
from logic.classes.ebook import Ebook

class TestEbook(unittest.TestCase):
    ebook = Ebook(id_doc=1, author='Author', title='Title', price=1.23,
                  topic='Topic', language='eng', pub_date='2022-01-01',
                  size=1.0, doi='doi', editor='Editor', pages=100, synopsis='Synopsis')

    def test_instance(self):
        self.assertIsInstance(self.ebook, Ebook, "Its instance!")

    def test_id(self):
        self.assertEqual(self.ebook.id_doc, 1)

    def test_author(self):
        self.assertEqual(self.ebook.author, "Author")

    def test_title(self):
        self.assertEqual(self.ebook.title, 'Title')

    def test_price(self):
        self.assertEqual(self.ebook.price, 1.23)

    def test_topic(self):
        self.assertEqual(self.ebook.topic, 'Topic')

    def test_language(self):
        self.assertEqual(self.ebook.language, 'eng')

    def test_pub_date(self):
        self.assertEqual(self.ebook.pub_date, '2022-01-01')

    def test_size(self):
        self.assertEqual(self.ebook.size, 1.0)

    def test_doi(self):
        self.assertEqual(self.ebook.doi, 'doi')

    def test_editor(self):
        self.assertEqual(self.ebook.editor, 'Editor')

    def test_pages(self):
        self.assertEqual(self.ebook.pages, 100)

    def test_synopsis(self):
        self.assertEqual(self.ebook.synopsis, 'Synopsis')

    def test_str(self):
        self.assertEqual(self.ebook.__str__(),
                         {"ID": 1,
                          "Author": "Author",
                          "Title": "Title",
                          "Price": 1.23,
                          "Topic": "Topic",
                          "Language": "eng",
                          "Editor": "Editor",
                          "Pages": 100,
                          "Synopsis": "Synopsis"})

    def test_eq(self):
        ebook2 = Ebook(id_doc=1, author='Author', title='Title', price=1.23,
                       topic='Topic', language='eng', pub_date='2022-01-01',
                       size=1.0, doi='doi', editor='Editor', pages=100, synopsis='Synopsis')
        self.assertEqual(self.ebook, ebook2)

if __name__ == '__main__':
    unittest.main()
