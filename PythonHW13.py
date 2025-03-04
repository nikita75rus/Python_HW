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
    def compress_image(self, input_path: str, output_path: str) -> None:
        """
        Сжать одно изображение в формат HEIF
        
        Аргументы:
            input_path (str): Путь к исходному изображению
            output_path (str): Путь для сохранения HEIF изображения
        """
        with Image.open(input_path) as img:
            img.save(output_path, "HEIF", quality=self.__quality)
        print(f"Сжато: {input_path} -> {output_path}")

    def process_directory(self, directory: str) -> None:
        """
        Обработать все поддерживаемые изображения в директории и поддиректориях
        
        Аргументы:
            directory (str): Путь к обрабатываемой директории
        """
        for root, _, files in os.walk(directory):
            for file in files:
                if file.lower().endswith(self.supported_formats):
                    input_path = os.path.join(root, file)
                    output_path = os.path.splitext(input_path)[0] + '.heic'
                    self.compress_image(input_path, output_path)
def main(input_path: str) -> None:
    """
    Основная функция программы для обработки входного пути и запуска сжатия
    
    Аргументы:
        input_path (str): Путь к файлу или директории для обработки
    """
    compressor = ImageCompressor(quality=50)
    input_path = input_path.strip('"')

    if os.path.exists(input_path):
        if os.path.isfile(input_path):
            print(f"Обрабатываем файл: {input_path}")
            output_path = os.path.splitext(input_path)[0] + '.heic'
            compressor.compress_image(input_path, output_path)
        elif os.path.isdir(input_path):
            print(f"Обрабатываем директорию: {input_path}")
            compressor.process_directory(input_path)
    else:
        print("Указанный путь не существует")

if __name__ == "__main__":
    user_input: str = input("Введите путь к файлу или директории: ")
    main(user_input)
