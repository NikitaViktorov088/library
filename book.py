import uuid
from typing import List, Dict, Optional


class Book:
    def __init__(self, title: str, author: str, year: int) -> None:
        self.id = str(uuid.uuid4())
        self.title = title
        self.author = author
        self.year = year
        self.status = "В наличии"

    def to_dict(self) -> Dict:
        """Преобразование объект книга в словарь"""
        return dict(id=self.id, title=self.title, author=self.author, year=self.year, status=self.status)

    @classmethod
    def from_dict(cls, data: Dict):
        """Создание объекта книга из словаря"""
        book = cls(data["title"], data["author"], data["year"])
        book.id = data["id"]
        book.status = data["status"]
        return book
