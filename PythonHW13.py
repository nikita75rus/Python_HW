"""
Модуль сжатия изображений в формат HEIF с использованием принципов ООП
"""

import os
from typing import Tuple
from PIL import Image
from pillow_heif import register_heif_opener

class ImageCompressor:
    """Класс для обработки операций сжатия изображений"""
    
    supported_formats: Tuple[str, ...] = ('.jpg', '.jpeg', '.png')

    def __init__(self, quality: int = 50) -> None:
        self.__quality = quality
        register_heif_opener()

    @property
    def quality(self) -> int:
        return self.__quality

    @quality.setter 
    def quality(self, quality: int) -> None:
        if not 1 <= quality <= 100:
            raise ValueError("Качество должно быть между 1 и 100")
        self.__quality = quality
