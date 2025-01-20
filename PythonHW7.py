from pathlib import Path
from PIL import Image
import os
from typing import List
from tqdm import tqdm

# Константы
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'JPG', 'JPEG'}
DEFAULT_QUALITY = 40
DEFAULT_FORMAT = 'WEBP'
AVAILABLE_FORMATS = {'WEBP'}

def get_images_paths(source_path: str) -> List[str]:
    """
    Рекурсивно получает пути ко всем изображениям в указанной директории или файле.
    
    Аргументы:
        source_path (str): Путь к директории или файлу
        
    Возвращает:
        List[str]: Список путей к изображениям
    """
    image_paths = []
    source = Path(source_path)
    
    if not source.exists():
        raise FileNotFoundError(f"Путь {source_path} не существует")
    
    if source.is_file():
        if source.suffix[1:] in ALLOWED_EXTENSIONS:
            image_paths.append(str(source))
    else:
        for root, _, files in os.walk(source_path):
            for file in files:
                if file.split('.')[-1] in ALLOWED_EXTENSIONS:
                    image_paths.append(os.path.join(root, file))
    
    return image_paths

def compress_image(image_path: str, output_format: str = DEFAULT_FORMAT, quality: int = DEFAULT_QUALITY) -> str:
    """
    Сжимает изображение в формат WEBP с указанным качеством.
    
    Аргументы:
        image_path (str): Путь к исходному изображению
        output_format (str): Целевой формат (WEBP)
        quality (int): Качество сжатия (1-100)
        
    Возвращает:
        str: Путь к сжатому изображению
    """
    try:
        source_image = Image.open(image_path)
        output_path = str(Path(image_path).with_suffix('.webp'))
        
        source_image.save(output_path, format="WEBP", quality=quality)
        
        # Подсчёт степени сжатия
        original_size = os.path.getsize(image_path)
        compressed_size = os.path.getsize(output_path)
        compression_ratio = (1 - compressed_size / original_size) * 100
        
        print(f"Сжато изображение: {image_path}")
        print(f"Степень сжатия: {compression_ratio:.2f}%")
        
        return output_path
    
    except Exception as e:
        print(f"Ошибка при сжатии {image_path}: {str(e)}")
        return ""

def main() -> None:
    """
    Основная функция для управления процессом сжатия изображений.
    """
    try:
        # Получение данных от пользователя
        source_path = input("Введите путь к файлу или директории: ")
        quality = int(input(f"Введите качество сжатия (1-100) [по умолчанию={DEFAULT_QUALITY}]: ") or DEFAULT_QUALITY)
        
        # Проверка введенных данных
        if not 1 <= quality <= 100:
            raise ValueError("Качество должно быть от 1 до 100")
            
        # Получение путей к изображениям
        image_paths = get_images_paths(source_path)
        if not image_paths:
            print("Изображения не найдены")
            return
            
        # Обработка изображений с индикатором прогресса
        print("\nОбработка изображений...")
        for image_path in tqdm(image_paths):
            compress_image(image_path, DEFAULT_FORMAT, quality)
            
        print("\nСжатие успешно завершено!")
        
    except Exception as e:
        print(f"Ошибка: {str(e)}")

if __name__ == "__main__":
    main()
