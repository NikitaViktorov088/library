import unittest
from library import Library
from book import Book
from main import show_menu
from unittest.mock import patch
from io import StringIO


class TestLibrary(unittest.TestCase):
    def setUp(self):
        """Создаем библиотеку"""
        self.library = Library(filename="test_library.json")
        self.book_1 = Book(title="test_book_1", author="test_author_1", year=2020)
        self.book_2 = Book(title="test_book_2", author="test_author_2", year=2021)
        self.library.books = [self.book_1, self.book_2]
        self.library.save()

    def test_add(self):
        """Тест добавления новой книги"""
        new_book = self.library.add(title="test_book_3", author="test_author_3", year=2023)
        self.assertEqual(len(self.library.books), 3)
        self.assertEqual(new_book.title, "test_book_3")
        self.assertEqual(new_book.author, "test_author_3")
        self.assertEqual(new_book.year, 2023)
        self.assertEqual(new_book.status, "В наличии")

    def test_delete(self):
        """"Тест удаления книги"""
        book_to_delete = self.book_1
        book_deleted = self.library.delete(book_to_delete.id)
        self.assertEqual(len(self.library.books), 1)
        self.assertEqual(book_deleted.id, book_to_delete.id)

        # Проверяем, что ошибка не возникает, если книга не найдена.
        book_deleted = self.library.delete(book_to_delete.id)
        self.assertEqual(book_deleted, None)

    def test_search(self):
        """Тест поиска книг"""
        result = self.library.search(title="test_book_1")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].title, "test_book_1")

        result = self.library.search(author="test_author_1")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].author, "test_author_1")

        result = self.library.search(year=2020)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].year, 2020)

    def test_change_status(self):
        """"Тест изменения статуса"""
        book_to_change = self.book_1
        updated_book = self.library.change_status(book_to_change.id, "Выдана")
        self.assertEqual(updated_book.status, "Выдана")

        # Проверяем в обратную сторону, так как есть кейс по возврату книги обратно.
        updated_book = self.library.change_status(book_to_change.id, "В наличии")
        self.assertEqual(updated_book.status, "В наличии")

        # Проверяем на неправильный статус.
        updated_book = self.library.change_status(book_to_change.id, "Неправильный статус")
        self.assertIsNone(updated_book)

    def test_list(self):
        """Тест списка книг"""
        books = self.library.list()
        self.assertEqual(len(books), 2)

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_menu(self, mock_stdout):
        """Тест меню"""
        show_menu()
        output = mock_stdout.getvalue().strip().split('\n')
        self.assertEqual(output[0], "Библиотека")
        self.assertIn("1. Добавить книгу", output)
        self.assertIn("2. Удалить книгу", output)
        self.assertIn("3. Поиск книги", output)
        self.assertIn("4. Список всех книг", output)
        self.assertIn("5. Изменить статус книги", output)
        self.assertIn("6. Выход", output)


if __name__ == '__main__':
    unittest.main()
