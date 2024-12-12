from typing import List
from repositories.book_repository import BookRepository
from models.book import Book
import logging

logger = logging.getLogger("LibraryLogger")


class BookService:
    def __init__(self, repository: BookRepository):
        self.repository = repository

    def get_all_books(self) -> List[Book]:
        if result := self.repository.get_all():
            logger.info("Успешное получение всех книг")
            return result
        else:
            logger.error("Ошибка получения всех книг")
            return []

    def add(self, title: str, author: str, year: int) -> Book:
        if result := self.repository.add(title, author, year):
            print(f"Книга {title} добавлена id {result.id}!")
            logger.info(f"Книга {title} добавлена id {result.id}!")
            return result
        else:
            logger.error(f"Ошибка добавления книги {title}")
            raise

    def delete_book(self, book_id: int) -> str:
        if result := self.repository.delete(book_id):
            print(f"Пользователь удалил книгу с ID {book_id}.")
            logger.info(f"Успешное удаление книги с id {book_id}")
            return result
        else:
            logger.error("Ошибка удаления книги")
            raise

    def search_book(self, query: str) -> List[Book]:
        if result := self.repository.search(query):
            logger.info("Успешное получение книг по запросу")
            return result
        else:
            logger.error("Ошибка поиска книг")
            raise

    def update_status(self, book_id: int, status: str) -> str:
        if result := self.repository.update_status(book_id, status):
            logger.info("Успешное обновление статуса книги")
            return result
        else:
            logger.error("Ошибка обновления статуса книги")
            raise
