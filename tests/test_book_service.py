import unittest
from unittest.mock import MagicMock
from services.book_service import BookService
from repositories.book_repository import BookRepository
from models.book import Book


class TestBookService(unittest.TestCase):

    def setUp(self):
        # Мокаем репозиторий
        self.mock_repo = MagicMock(spec=BookRepository)
        self.service = BookService(self.mock_repo)

    def test_add_book(self):
        book = self.service.add(title="Book 1", author="Author 1", year=2000)
        self.mock_repo.add.assert_called_once_with(book)

    def test_delete_book(self):
        book = Book(id="1", title="Book 1", author="Author 1", year=2000, status="в наличии")
        self.mock_repo.get_by_id.return_value = book
        self.service.delete_book(book.id)
        self.mock_repo.delete.assert_called_once_with(book.id)

    def test_change_status(self):
        book = Book(id="1", title="Book 1", author="Author 1", year=2000, status="в наличии")
        self.mock_repo.get_by_id.return_value = book
        self.service.update_status(book.id, "выдана")
        self.mock_repo.update_status.assert_called_once_with(book.id, "выдана")


if __name__ == "__main__":
    unittest.main()
