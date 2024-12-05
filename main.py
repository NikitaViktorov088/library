from library import Library


def show_menu():
    """Список действий"""
    print("\nБиблиотека")
    print("1. Добавить книгу")
    print("2. Удалить книгу")
    print("3. Поиск книги")
    print("4. Список всех книг")
    print("5. Изменить статус книги")
    print("6. Выход")

def handle_choice(library: Library, choice: str):
    """Обработка команд"""
    if choice == "1":
        title = input("Введите название книги: ")
        author = input("Введите автора книги: ")
        year = int(input("Введите год издания книги: "))
        library.add(title, author, year)
        print("Книга добавлена!")

    elif choice == "2":
        book_id = input("Введите ID книги для удаления: ")
        book = library.delete(book_id)
        if book:
            print(f"Книга '{book.title}' удалена.")
        else:
            print("Такой id книги не найден, вероятнее он уже удален!")

    elif choice == "3":
        title = input("Введите название для поиска (или оставьте пустым): ")
        author = input("Введите автора для поиска (или оставьте пустым): ")
        year = input("Введите год для поиска (или оставьте пустым): ")
        year = int(year) if year else None
        books = library.search(title, author, year)
        for book in books:
            print(
                f"ID: {book.id}, Название: {book.title}, Автор: {book.author}, Год: {book.year}, Статус: {book.status}")

    elif choice == "4":
        books = library.list()
        for book in books:
            print(
                f"ID: {book.id}, Название: {book.title}, Автор: {book.author}, Год: {book.year}, Статус: {book.status}")

    elif choice == "5":
        book_id = input("Введите ID книги для изменения статуса: ")
        new_status = input("Введите новый статус ('В наличии' или 'Выдана'): ")
        book = library.change_status(book_id, new_status)
        if book:
            print(f"Статус книги '{book.title}' изменен на '{book.status}'.")
        else:
            print("Такой id книги не найден!")

    elif choice == "6":
        print("Выход из программы...")
        return False

    else:
        print("Неверный выбор! Попробуйте снова.")
    return True

def main():
    library = Library()
    is_running = True

    while is_running:
        show_menu()
        choice = input("Ваш выбор: ")
        is_running = handle_choice(library, choice)


if __name__ == "__main__":
    main()
