# Система управления библиотекой

Это консольное приложение для управления библиотекой, которое позволяет добавлять, удалять, искать книги, а также изменять их статус (в наличии/выдана). Программа использует файл в формате JSON для хранения данных о книгах.

## Оглавление

1. [Описание проекта](#описание-проекта)
2. [Требования](#требования)
3. [Установка](#установка)
4. [Использование](#использование)
5. [Структура проекта](#структура-проекта)
6. [Тестирование](#тестирование)

---

## Описание проекта

Программа представляет собой консольное приложение для управления книгами в библиотеке. Пользователь может:

- **Добавлять книги** с указанием названия, автора и года издания.
- **Удалять книги** по уникальному идентификатору.
- **Искать книги** по названию, автору или году издания.
- **Просматривать список всех книг** с указанием их статуса.
- **Изменять статус книги** (например, с "в наличии" на "выдана").

Все данные о книгах хранятся в файле `data.json`, который автоматически обновляется при изменении информации о книгах.

## Требования

Для корректной работы приложения необходимо:

- Python версии 3.x
- Стандартные библиотеки Python: `json`, `os`, `uuid`, `unittest`, и другие (все библиотеки уже включены в стандартную поставку Python).

---


