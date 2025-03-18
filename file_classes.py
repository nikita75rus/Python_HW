from abc import ABC, abstractmethod
from typing import Any
import json
from typing import Dict
class Абстрактный_Файл(ABC):
    """Абстрактный базовый класс для операций с файлами."""
    
    @abstractmethod
    def читать(self) -> Any:
        """Чтение данных из файла."""
        pass
    
    @abstractmethod
    def записать(self, данные: Any) -> None:
        """Запись данных в файл."""
        pass
    
    @abstractmethod
    def добавить(self, данные: Any) -> None:
        """Добавление данных в файл."""
        pass


class ФайлJson(Абстрактный_Файл):
    """Класс для работы с JSON файлами."""
    
    def __init__(self, путь_к_файлу: str):
        self.путь_к_файлу = путь_к_файлу
    
    def читать(self) -> Dict:
        with open(self.путь_к_файлу, 'r', encoding='utf-8') as файл:
            return json.load(файл)
    
    def записать(self, данные: Dict) -> None:
        with open(self.путь_к_файлу, 'w', encoding='utf-8') as файл:
            json.dump(данные, файл, indent=4, ensure_ascii=False)
    
    def добавить(self, данные: Dict) -> None:
        try:
            текущие_данные = self.читать()
            текущие_данные.update(данные)
            self.записать(текущие_данные)
        except FileNotFoundError:
            self.записать(данные)
