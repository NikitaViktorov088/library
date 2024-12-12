import unittest
from unittest.mock import MagicMock
from repositories.book_repository import BookRepository
from models.book import Book
from repositories.json_storage import JsonStorage


class TestBookRepository(unittest.TestCase):
    def setUp(self):
        self.mock_storage = MagicMock(spec=JsonStorage)
        self.repo = BookRepository(self.mock_storage)

    def test_add_book(self):
        self.mock_storage.read.return_value = []
        book = self.repo.add(title="Book 1", author="Author 1", year=2000)
        self.mock_storage.write.assert_called_once()
        self.assertEqual(self.mock_storage.write.call_args[0][0], [book.__dict__])

    def test_delete_book(self):
        book = Book(id="1", title="Book 1", author="Author 1", year=2000, status="в наличии")
        self.mock_storage.read.return_value = [book.__dict__]
        self.repo.delete(book.id)
        self.mock_storage.write.assert_called_once()
        self.assertEqual(self.mock_storage.write.call_args[0][0], [])

    def test_get_by_id_book_found(self):
        book = Book(id="1", title="Book 1", author="Author 1", year=2000, status="в наличии")
        self.mock_storage.read.return_value = [book.__dict__]
        found_book = self.repo.get_by_id(book.id)
        self.assertEqual(found_book.id, book.id)

    def test_get_by_id_book_not_found(self):
        self.mock_storage.read.return_value = []
        found_book = self.repo.get_by_id("nonexistent-id")
        self.assertIsNone(found_book)


if __name__ == "__main__":
    unittest.main()
