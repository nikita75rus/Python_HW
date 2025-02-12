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
# Добавляем сортировку и форматированный вывод
отсортировано_по_году = dict(sorted(full_dict.items(), 
    key=lambda x: 9999 if x[1]["year"] in ('TBA', None) else int(x[1]["year"])))

отсортировано_по_году_названию = dict(sorted(full_dict.items(), 
    key=lambda x: (9999 if x[1]["year"] in ('TBA', None) else int(x[1]["year"]), x[1]["title"] or "")))

фильтр_сортировка = sorted(
    filter(lambda x: isinstance(x[1]["year"], int) and x[1]["year"] > 2015, full_dict.items()),
    key=lambda x: x[1]["title"]
)

# Добавление форматированного вывода результатов
