import small_dict

search_query = input("Введите название фильма или его часть: ").lower()


found_movies = []


for movie_title, year in small_dict.items():
    if search_query in movie_title.lower():
        found_movies.append(movie_title)


if found_movies:
    print("Найденные фильмы:")
    for movie in found_movies:
        print(movie)
else:
    print("Фильмы не найдены.")


future_movies = []


for movie_title, year in small_dict.items():

    if isinstance(year, int) and year > 2024:
        future_movies.append((movie_title, year))


if future_movies:
    print("Фильмы, вышедшие после 2024 года:")
    for movie, release_year in future_movies:
        print(f"{movie} ({release_year})")
else:
    print("Фильмы после 2024 года не найдены.")


print("1. Простая печать названий фильмов:")
for movie in small_dict:
    print(movie)


movie_titles = list(small_dict.keys())
print("\n2. Список названий фильмов:")
print(movie_titles)


future_movies_dict = {
    movie: year 
    for movie, year in small_dict.items() 
    if isinstance(year, int) and year > 2024
}
print("\n3. Словарь фильмов после 2024 года:")
print(future_movies_dict)


movie_list_dicts = [
    {movie: year} 
    for movie, year in small_dict.items() 
    if isinstance(year, int) and year > 2024
]
print("\n4. Список словарей фильмов после 2024 года:")
print(movie_list_dicts)