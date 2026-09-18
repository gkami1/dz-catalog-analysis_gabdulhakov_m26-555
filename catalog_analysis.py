import math

movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155,
     "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
]


def average_rating(movies):
    """Возвращает среднюю оценку по каталогу, округлённую до одного знака."""
    total = 0
    for movie in movies:
        total += movie["rating"]
    return round(total / len(movies), 1)


def catalog_age_stats(movies, current_year=2026):
    """Возвращает (самый старый возраст, самый новый возраст, средний возраст)."""
    ages = [current_year - movie["year"] for movie in movies]
    oldest = max(ages)
    newest = min(ages)
    average = math.ceil(sum(ages) / len(ages))
    return (oldest, newest, average)


def duration_in_hours(minutes):
    """Переводит минуты в строку формата '2ч 35м'."""
    hours = minutes // 60
    leftover = minutes % 60
    return f"{hours}ч {leftover}м"


def rating_tier(rating):
    """Возвращает категорию оценки: шедевр / хорошо / средне / слабо."""
    if rating >= 7:
        tier = "шедевр" if rating >= 9 else "хорошо"
    elif rating >= 5:
        tier = "средне"
    else:
        tier = "слабо"
    return tier


def decade_label(year):
    """Возвращает метку эпохи по году выпуска фильма."""
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if year >= 2015:
            return "недавние"
        case _:
            return "старые"


def count_long_movies(movies, threshold=120):
    """Считает количество фильмов длиннее threshold минут."""
    count = 0
    for movie in movies:
        if movie["duration_min"] > threshold:
            count += 1
    return count


def print_non_comedy(movies):
    """Печатает названия фильмов, которые не относятся к жанру 'comedy'."""
    for movie in movies:
        if "comedy" in movie["genres"]:
            continue
        print(movie["title"])


def find_first_masterpiece(movies):
    """Находит первый фильм с рейтингом выше 9.0 или сообщает, что такого нет."""
    index = 0
    while index < len(movies):
        if movies[index]["rating"] > 9.0:
            print(movies[index]["title"])
            break
        index += 1
    else:
        print("Шедевров не найдено")


def normalize_title(title):
    """Приводит строку к Title Case вручную, без str.title()."""
    words = title.split()
    normalized = [word[0].upper() + word[1:] for word in words]
    return " ".join(normalized)


def make_slug(title):
    """Превращает название в слаг вида the-quiet-algorithm."""
    return title.lower().replace(" ", "-")


def format_report_line(movie):
    """Собирает единую строку с описанием фильма."""
    title = normalize_title(movie["title"])
    genres = ", ".join(sorted(movie["genres"]))
    duration = duration_in_hours(movie["duration_min"])
    return (
        f'"{title}" ({movie["year"]}) — '
        f'{movie["rating"]}/10, {duration}, жанры: {genres}'
    )


def titles_sorted_by_rating(movies):
    """Возвращает названия фильмов, отсортированные по убыванию рейтинга."""
    sorted_movies = sorted(movies, key=lambda movie: movie["rating"], reverse=True)
    return [movie["title"] for movie in sorted_movies]


def top_n_by_rating(movies, n=3):
    """Возвращает список из n кортежей (title, rating) — топ по рейтингу."""
    sorted_movies = sorted(movies, key=lambda movie: movie["rating"], reverse=True)
    return [(movie["title"], movie["rating"]) for movie in sorted_movies[:n]]


def count_by_genre(movies):
    """Возвращает словарь {жанр: количество фильмов}."""
    counts = {}
    for movie in movies:
        for genre in movie["genres"]:
            counts[genre] = counts.get(genre, 0) + 1
    return counts


def actor_filmography(movies):
    """Возвращает словарь {актер: [список названий фильмов]}."""
    filmography = {}
    for movie in movies:
        for actor in movie["actors"]:
            if actor not in filmography:
                filmography[actor] = []
            filmography[actor].append(movie["title"])
    return filmography


def above_average_ratings(movies):
    """Словарь {title: rating} только для фильмов с рейтингом выше среднего."""
    avg = average_rating(movies)
    return {
        movie["title"]: movie["rating"]
        for movie in movies
        if movie["rating"] > avg
    }


def all_genres(movies):
    """Возвращает множество всех уникальных жанров каталога."""
    genres = set()
    for movie in movies:
        genres |= movie["genres"]
    return genres


def common_actors(movie1, movie2):
    """Возвращает множество актёров, снимавшихся в обоих фильмах."""
    return set(movie1["actors"]) & set(movie2["actors"])


def genres_only_in_one(movies_a, movies_b):
    """Жанры, которые есть в movies_a, но отсутствуют в movies_b."""
    genres_a = set()
    for movie in movies_a:
        genres_a |= movie["genres"]

    genres_b = set()
    for movie in movies_b:
        genres_b |= movie["genres"]

    return genres_a - genres_b


def iter_high_rated(movies, min_rating=8.0):
    """Лениво отдаёт фильмы с рейтингом не ниже min_rating."""
    for movie in movies:
        if movie["rating"] >= min_rating:
            yield movie


def total_duration_above_7(movies):
    """Суммарная длительность фильмов с рейтингом выше 7 (в минутах)."""
    return sum(m["duration_min"] for m in movies if m["rating"] > 7)


def build_report(movies):
    """Печатает единый отчёт по каталогу."""
    avg_rating = average_rating(movies)
    _, _, avg_age = catalog_age_stats(movies)

    print("ОТЧЁТ ПО КАТАЛОГУ")
    print(f"Средний рейтинг: {avg_rating}")
    print(f"Средний возраст фильмов: {avg_age} лет")
    print()

    print("Топ-3 фильма:")
    top = sorted(movies, key=lambda movie: movie["rating"], reverse=True)[:3]
    for movie in top:
        print(f"  {format_report_line(movie)}")
    print()

    print("Фильмов по жанрам:")
    counts = count_by_genre(movies)
    sorted_counts = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    for genre, count in sorted_counts:
        print(f"  {genre} — {count}")
    print()

    genres_line = ", ".join(sorted(all_genres(movies)))
    print(f"Все жанры каталога: {genres_line}")


if __name__ == "__main__":
    build_report(movies)