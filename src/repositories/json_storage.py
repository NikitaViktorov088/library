import json
import logging
from typing import List


logger = logging.getLogger("LibraryLogger")


class JsonStorage:
    def __init__(self, filename: str):
        self.filename = filename

    def read(self) -> List[dict]:
        try:
            with open(self.filename, 'r') as file:
                logger.info(f"Чтение файла {self.filename} успешно!")
                return json.load(file)
        except FileNotFoundError:
            logger.warning(f"Файл {self.filename} не найден!")
            return []

    def write(self, data: List[dict]) -> None:
        try:
            with open(self.filename, 'w', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
                logger.info(f"Данные успешно записаны в {self.filename}")
        except Exception as e:
            logger.error(f"Ошибка при записи в файл {self.filename}: {e}")
            raise
