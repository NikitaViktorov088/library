import json
import os
from typing import List, Optional

from book import Book


class Library:
    def __init__(self, filename: str="data.json"):
        self.filename = filename
        self.books: List[Book] = self.load_data()

    def load_data(self) -> List[Book]:
        """Загрузка книг из JSON файла"""
        if not os.path.exists(self.filename) or os.stat(self.filename).st_size == 0:
            return []

        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                data = json.load(file)
                return [Book.from_dict(book) for book in data]
        except json.JSONDecodeError:
            print("Ошибка при чтении данных из файла. Возможно, файл поврежден.")
            return []
        except Exception as e:
            print(f"Произошла ошибка при загрузке данных: {e}")
            return []

    def save(self) -> None:
        """Сохранение"""
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump([book.to_dict() for book in self.books], file, indent=4, ensure_ascii=False)

    def add(self, title: str, author: str, year: int) -> Book:
        """Добавление книги"""
        new_book = Book(title, author, year)
        self.books.append(new_book)
        self.save()
        return new_book

    def delete(self, book_id: str) -> Optional[Book]:
        """"Удаление книги по uuid"""
        if book_deleted := next((book for book in self.books if book.id == book_id), None):
            self.books.remove(book_deleted)
            self.save()
            return book_deleted
        return None

    def search(
            self,
            title: Optional[str] = None,
            author: Optional[str] = None,
            year: Optional[int] = None) -> List[Book]:
        """"Поиск книг по названию, автору, году"""
        result = self.books
        if title:
            result = [book for book in result if title.lower() in book.title.lower()]
        if author:
            result = [book for book in result if author.lower() in book.author.lower()]
        if year:
            result = [book for book in result if book.year == book.year]
        return result

    def change_status(self, book_id: str, status: str) -> Optional[Book]:
        """Изменение статуса"""
        book = next((book for book in self.books if book.id == book_id))
        if book:
            if status in ("В наличии", "Выдана"):
                book.status = status
                self.save()
                return book
        return None

    def list(self) -> List[Book]:
        """Весь список книг"""
        return self.books

