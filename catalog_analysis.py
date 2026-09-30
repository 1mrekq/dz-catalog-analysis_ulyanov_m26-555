movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155, "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
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
    return round(sum(movie['rating'] for movie in movies) / len(movies), 1)
    

def catalog_age_stats(movies, current_year=2026):
    min_age = current_year - min(movie['year'] for movie in movies)
    max_age = current_year - max(movie['year'] for movie in movies)
    average = math.ceil(sum(current_year - movie['year'] for movie in movies) / len(movies))
    return (max_age, min_age, average)

MINUTES_IN_HOUR = 60

def duration_in_hours(minutes):
    return f'{minutes // MINUTES_IN_HOUR}ч {minutes % MINUTES_IN_HOUR}м'

def rating_tier(rating):
    if rating >= 9:
        return 'шедевр'
    elif rating > 7:
        return 'хорошо'
    else:
        return 'средне' if rating > 5 else 'слабо'

def decade_label(year):
    match year:
        case _ if year > 2020:
            return 'новые'
        case _ if year >= 2015:
            return 'недавние'
        case _:
            return 'старые'

for movie in movies:
    if 'comedy' in movie['genres']:
        continue
    print(f'{movie['title']}')

i = 0
while i < len(movies):
    if movies[i]['rating'] > 9:
        print(f'Шедевр: {movies[i]['title']}')
        break
    i+=1
else:
    print('Шедевров не найдено')

def main():
    print("Hello from dz-catalog-analysis-ulyanov-m26-555!")


if __name__ == "__main__":
    main()
