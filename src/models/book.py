import uuid
from dataclasses import dataclass
import re


def validate_title_or_author(value: str) -> bool:
    """Валидация для title и author (только буквы и цифры)."""
    return bool(re.match(r'^[a-zA-Z0-9а-яА-Я ]+$', value))

@dataclass
class Book:
    id: str
    title: str
    author: str
    year: int
    status: str

    def __post_init__(self):
        if not validate_title_or_author(self.title):
            raise ValueError(f"Invalid title: {self.title}")
        if not validate_title_or_author(self.author):
            raise ValueError(f"Invalid author: {self.author}")
        if not (0 < self.year <= 2024):
            raise ValueError(f"Invalid year: {self.year}")
        if self.status not in ["в наличии", "выдана"]:
            raise ValueError(f"Invalid status: {self.status}")

    @staticmethod
    def create(title: str, author: str, year: int, status: str='в наличии') -> 'Book':
        """Создание книги."""
        return Book(
            id=uuid.uuid4().hex,
            title=title,
            author=author,
            year=year,
            status=status,
        )

