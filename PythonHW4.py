def caesar_cipher(text, shift):
    alphabets = {
        'ru_upper': (1040, 1071, 32),  # А-Я
        'ru_lower': (1072, 1103, 32),  # а-я
        'en_upper': (65, 90, 26),      # A-Z
        'en_lower': (97, 122, 26)      # a-z
    }
    
    result = ""
    for char in text:
        if char.isspace():
            result += char
            continue
            
        char_code = ord(char)
        
        for start, end, mod in alphabets.values():
            if start <= char_code <= end:
                new_code = start + ((char_code - start + shift) % mod)
                result += chr(new_code)
                break
        else:
            result += char
            
    return result

try:
    text = input("Введите текст: ")
    shift = int(input("Введите сдвиг: "))
    
    encrypted_text = caesar_cipher(text, shift)
    print(f"Результат: {encrypted_text}")
    
except ValueError:
    print("Ошибка: Сдвиг должен быть числом!")



