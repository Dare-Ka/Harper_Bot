movie_types_dict = {
    'movie': 'Кинофильм',
    'tv-series': 'TV-сериал',
    'cartoon': 'Мультфильм',
    'animated-series': 'Аниме-сериал',
    'anime': 'Аниме'
}

random_movie_error = 'Извини, не получилось подобрать фильм😔\nПопробуем еще?'

movie_error = 'Не удалось найти фильм😔'

movie_description = ('<u><b>Название:</b></u> {name}\n'
                     '<u><b>Страна:</b></u> {countries}\n'
                     '<u><b>Жанры:</b></u> {genres}\n'
                     '<u><b>Тип:</b></u> {type}\n\n'
                     '<u><b>Описание:</b></u> {description}\n\n'
                     '<u><b>В ролях:</b></u> {persons}\n\n'
                     '<u><b>Продолжительность:</b></u> {length}(мин)\n'
                     '<u><b>Год выхода:</b></u> {year}\n'
                     '<u><b>Рейтинг на Кинопоиске:</b></u> {rating}'
                     )
