from typing import Dict, List, Set, Optional, Any
from pprint import pprint
from marvel import full_dict

# Обработка пользовательского ввода с помощью map
пользовательский_ввод = input("Введите числа через пробел: ")
числа: List[Optional[int]] = list(map(lambda x: int(x) if x.isdigit() else None, пользовательский_ввод.split()))

# Преобразование словаря в список словарей
список_фильмов: List[Dict[str, Any]] = [{"id": k, **v} for k, v in full_dict.items()]
# Добавляем функции фильтрации и работы с множествами
отфильтрованные_фильмы: List[Dict[str, Any]] = list(filter(lambda x: x["id"] in числа, список_фильмов))
режиссеры: Set[str] = {фильм["director"] for фильм in список_фильмов}
фильмы_год_строка: Dict[str, Dict[str, Any]] = {k: {**v, "year": str(v["year"])} for k, v in full_dict.items()}
фильмы_на_ч: List[Dict[str, Any]] = list(filter(lambda x: x["title"] and x["title"].startswith("Ч"), список_фильмов))