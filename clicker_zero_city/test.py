DATABASE = {"Сергей": "Омск",
            "Соня": "Москва",
            "Миша": "Москва",
            "Дима": "Челябинск",
            "Коля": "Ставрополь"}


def process_anfisa(query):
    if query == 'Сколько у меня друзей?':
        count = len(DATABASE)
        return 'У тебя ' + str(count) + ' друзей.'
    # # Здесь проверьте, что переменная query равна строке 'Кто все мои друзья?'
    elif query == 'Кто все мои друзья?':
        friends_string = ''
        # Чтобы получить перечень друзей -
        # переберите словарь DATABASE в цикле
        for fs in DATABASE:
            friends_string += fs + "," + ' '
            # Добавляйте к переменной friends_string имя друга и пробел
        # Верните строку, составленную из 'Твои друзья: ' и friends_string
        return friends_string
    else:
        return '<неизвестный запрос>'


# Не изменяйте следующий код
print('Привет, я Анфиса!')
print(process_anfisa('Сколько у меня друзей?'))
print(process_anfisa('Кто все мои друзья?'))
