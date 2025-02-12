from typing import Dict, List, Set, Optional, Any
from pprint import pprint
from marvel import full_dict

# Обработка пользовательского ввода с помощью map
пользовательский_ввод = input("Введите числа через пробел: ")
числа: List[Optional[int]] = list(map(lambda x: int(x) if x.isdigit() else None, пользовательский_ввод.split()))

# Преобразование словаря в список словарей
список_фильмов: List[Dict[str, Any]] = [{"id": k, **v} for k, v in full_dict.items()]

