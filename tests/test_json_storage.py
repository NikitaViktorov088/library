import unittest
from unittest.mock import patch, mock_open
from repositories.json_storage import JsonStorage


class TestJsonStorage(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open,
           read_data='[{"id": "1", "title": "Book 1", "author": "Author 1", "year": 2000, "status": "в наличии"}]')
    def test_read(self, mock_file):
        storage = JsonStorage("books.json")
        result = storage.read()
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["title"], "Book 1")

    @patch("builtins.open", new_callable=mock_open)
    def test_write(self, mock_file):
        storage = JsonStorage("books.json")
        data = [{"id": "1", "title": "Book 1", "author": "Author 1", "year": 2000, "status": "в наличии"}]
        storage.write(data)
        mock_file.assert_called_once_with("books.json", "w", encoding="utf-8")


if __name__ == "__main__":
    unittest.main()
