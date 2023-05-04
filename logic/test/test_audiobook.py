import unittest
from logic.classes.audio_book import AudioBook

class TestAudioBook(unittest.TestCase):
    audio_book = AudioBook(id_doc=1, author='Author', title='Title', price=9.99,
                           topic='Topic', language='eng', pub_date='2022-01-01',
                           size=200.0, doi='doi', hours=1, minutes=30, seconds=0,
                           synopsis='A very good audio book.')

    def test_instance(self):
        self.assertIsInstance(self.audio_book, AudioBook, "It's an instance of AudioBook!")

    def test_id(self):
        self.assertEqual(self.audio_book.id_doc, 1)

    def test_author(self):
        self.assertEqual(self.audio_book.author, "Author")

    def test_title(self):
        self.assertEqual(self.audio_book.title, 'Title')

    def test_price(self):
        self.assertEqual(self.audio_book.price, 9.99)

    def test_topic(self):
        self.assertEqual(self.audio_book.topic, 'Topic')

    def test_language(self):
        self.assertEqual(self.audio_book.language, 'eng')

    def test_pub_date(self):
        self.assertEqual(self.audio_book.pub_date, '2022-01-01')

    def test_size(self):
        self.assertEqual(self.audio_book.size, 200.0)

    def test_doi(self):
        self.assertEqual(self.audio_book.doi, 'doi')

    def test_duration(self):
        self.assertEqual(self.audio_book.hours, 1)
        self.assertEqual(self.audio_book.minutes, 30)
        self.assertEqual(self.audio_book.seconds, 0)

    def test_synopsis(self):
        self.assertEqual(self.audio_book.synopsis, 'A very good audio book.')

    def test__str__(self):
        self.assertEqual(self.admin.__str__(), '{"Admin ID": 1, "Admin name": "Name", "Admin last name": "Surname", '
                                           '"Admin phone": "123456789", "Admin mail": "test@test.com"}')

        

if __name__ == '__main__':
    unittest.main()
