from abc import ABC, abstractmethod
from typing import Any

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
