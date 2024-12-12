import logging
from services.book_service import BookService
from repositories.book_repository import BookRepository
from repositories.json_storage import JsonStorage
from models.book import Book


logger = logging.getLogger("LibraryLogger")


class Menu:
    def __init__(self):
        storage = JsonStorage("books.json")
        book_repository = BookRepository(storage)
        self.book_service = BookService(book_repository)

    def show(self):
        try:
             while True:
                 print("\nМеню: "
                       "1. Показать все книги  "
                       "2. Добавить книгу  "
                       "3. Удалить книгу  "
                       "4. Поиск книги  "
                       "5. Изменить статус книги  "
                       "0. Выход")
                 choice = input("Выберите действие: ")

                 match choice:
                     case "1":
                         self.show_books()
                     case "2":
                         self.add_book()
                     case "3":
                         self.delete_book()
                     case "4":
                         self.search_book()
                     case "5":
                         self.change_status()
                     case "0":
                         print("Выход...")
                         logger.info("Пользователь вышел из программы.")
                         break
                     case _:
                         print("Неверный выбор! Попробуйте снова.")
                         logger.warning("Пользователь выбрал неверный пункт меню.")
        except KeyboardInterrupt as e:
            """Выход из программы Ctrl+C"""

    def show_books(self):
        if books := self.book_service.get_all_books():
            for book in books:
                print(
                    f"ID: {book.id},"
                    f"Title: {book.title},"
                    f"Author: {book.author},"
                    f"Year: {book.year},"
                    f"Status: {book.status}"
                )
        else:
            print("Нет книг в библиотеке.")
            logger.info("Нет книг в библиотеке.")

    def add_book(self) -> Book|None:
        title = input("Введите название книги: ")
        author = input("Введите автора книги: ")
        year = int(input("Введите год издания книги: "))
        self.book_service.add(title, author, year)

    def delete_book(self):
        book_id = input("Введите ID книги для удаления: ")
        self.book_service.delete_book(book_id)

    def search_book(self):
        query = input("Введите запрос для поиска книги (по названию или автору): ")
        if books := self.book_service.search_book(query):
            for book in books:
                print(
                    f"ID: {book.id},"
                    f"Title: {book.title},"
                    f"Author: {book.author},"
                    f"Year: {book.year},"
                    f"Status: {book.status}"
                )
        else:
            print("Книги не найдены.")
            logger.info(f"По запросу '{query}' не было найдено книг.")

    def change_status(self):
        book_id = input("Введите ID книги для изменения статуса: ")
        new_status = input("Введите новый статус (в наличии/выдана): ").lower()
        if new_status not in ["в наличии", "выдана"]:
            print("Неверный статус!")
            logger.warning(f"Пользователь ввел неверный статус: '{new_status}'")
        else:
            self.book_service.update_status(book_id, new_status)
            logger.info(f"Пользователь изменил статус книги с ID {book_id} на {new_status}.")