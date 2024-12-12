import logging
from abc import ABC, abstractmethod
from typing import List, Optional

from models.book import Book
from repositories.json_storage import JsonStorage


logger = logging.getLogger("LibraryLogger")


class BaseRepository(ABC):
    """
    Абстрактный базовый класс для всех репозиториев.
    """

    @abstractmethod
    def add(self, item) -> None:
        """
        Добавить элемент в репозиторий.
        """
        pass

    @abstractmethod
    def delete(self, item_id: str) -> None:
        """
        Удалить элемент из репозитория по ID.
        """
        pass

    @abstractmethod
    def get_by_id(self, item_id: str) -> Optional[object]:
        """
        Получить элемент по ID.
        """
        pass

    @abstractmethod
    def get_all(self) -> List[object]:
        """
        Получить все элементы из репозитория.
        """
        pass

    @abstractmethod
    def update_status(self, item_id: str, status: str) -> None:
        """
        Обновить статус элемента.
        """
        pass


class BookRepository(BaseRepository):
    def __init__(self, storage: JsonStorage):
        self.storage = storage

    def get_all(self) -> List[Book]:
        data = self.storage.read()
        return [Book(**book) for book in data]

    def get_by_id(self, book_id: str) -> Book:
        books = self.get_all()
        for book in books:
            if book.id == book_id:
                return book
        return None

    def add(self, title: str, author: str, year: int) -> Book:
        books = self.get_all()
        book = Book.create(title, author, year)
        books.append(book)
        self.storage.write([book.__dict__ for book in books])
        return book

    def delete(self, book_id: str) -> str:
        books = self.get_all()
        if book_remove_to_id := self.get_by_id(book_id):
            books.remove(book_remove_to_id)
            self.storage.write([book.__dict__  for book in books])
            return book_remove_to_id.id
        else:
            return None

    def update_status(self, book_id: str, status: str) -> Book:
        books = self.get_all()
        if book := self.get_by_id(book_id):
            for item in books:
                if item.id == book.id:
                    item.status = status
                    # book.status = status
                    self.storage.write([book.__dict__ for book in books])
            return book
        else:
            return None

    def search(self, query: str) -> List[Book]:
        books = self.get_all()
        if result := [book for book in books if query.lower() in book.title.lower() or query.lower() in book.author.lower() or query.lower() in str(book.year)]:
            return result
        else:
            return None







