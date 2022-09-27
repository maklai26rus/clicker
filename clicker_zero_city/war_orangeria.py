import pyautogui
import time

import easyocr

from clicker_zero_city.exit_ZC import exit_mgl, exit_zc

# Переход на глобальную карту и поиск лодки
global_map = "png/greenery/global_maps.PNG"
looking_boat = "png/greenery/boat.PNG"
# Поиск оранжереи
greenery = "png/greenery/greenery_text.PNG"

# Обновление карты
update = 'png/greenery/update.PNG'

# При начале боя может выскачить 3 разных варианта
battle_next1 = 'png/greenery/battle_next1.PNG'
battle_next2 = 'png/greenery/battle_next2.PNG'
battle_next3 = "png/greenery/battle_next3.PNG"

# Ловят ненужный трегер
stop = "png/greenery/stop.PNG"
fist = 'png/greenery/fist.PNG'

# Первая строчка всегда сила
my_strength_txt = 'my_strength.txt'
crutch = 0.8
try:
    reader = easyocr.Reader(['ru'])
except UserWarning:
    print("ошибка модуля")


def eternal_search(func):
    """
    Зацикленая функция для поиска координат
    """

    def search():
        while True:
            sh = func()
            if sh:
                center = pyautogui.center(sh)
                pyautogui.click(center)
                time.sleep(0.1)
                break
            else:
                print(f'Не могу найти корданату. Проверте если она на месте? {func.__name__}')

    return search


def read_streng():
    """
    Читае их файла рекомендуему максимальную силу противника
    Возращает
    return : значение значение максимальной силы противника
    """
    with open(my_strength_txt, 'r', encoding='utf-8') as ms:
        for line in ms:
            my_strength = int("".join(line))
    return my_strength


def time_game(func):
    def other_func():
        time.sleep(3)
        func()
        return func

    return other_func


def start_war_orangeria():
    """Запуск скрипта"""
    # Вызов глобальной карты для поиска оранжереи
    global_maps()

    # Поиск привязке на карте катера
    boat_search()

    # запуск Оранжереи
    greenhouse_search()

    # Обновляет бойцов, всегда при запуске
    update_map()

    # Вибирает бойцов подходящих под уровень
    get_enemy()


@time_game
@eternal_search
def global_maps():
    """
    Переходим на глобальную карту для поиска  оранжереи
    :return:
    """
    click = pyautogui.locateOnScreen(global_map, confidence=0.5)
    return click
    # if click:
    #     pyautogui.click(click)
    # time.sleep(1)


@time_game
def boat_search():
    """
    Ищем на карте катер и привязываемся к нему что бы перетащить мышкку
    :return:
    """
    global crutch
    click = pyautogui.locateOnScreen(looking_boat, confidence=crutch)
    if click:
        pyautogui.click(click)
        pyautogui.dragTo(click.left // 3, click.top, 1, button='left')
    else:
        crutch -= 0.1
        boat_search()


@time_game
def update_map():
    """
    Обновляет карту бойцов
    """
    click = pyautogui.locateOnScreen(update, confidence=0.9)

    if click:
        pyautogui.click(click)


@time_game
def greenhouse_search():
    """
    Определяем на карте оранжерею
    :return:
    """
    click = pyautogui.locateOnScreen(greenery, confidence=0.8, grayscale=True)
    pyautogui.click(click.left + 50, click.top - 60)


@time_game
def get_enemy():
    """
    Определение пративника по его силе.
    в my_strength = read_streng() указана максимальная сила для нападения
    """
    number_temp = 1
    my_strength = read_streng()

    battle_click = list(pyautogui.locateAllOnScreen(battle_next1, confidence=0.9, grayscale=True))

    for enemy in battle_click:

        path_temp = f'png/temp/{number_temp}.png'
        pyautogui.screenshot(path_temp, region=(enemy.left - 350, enemy.top, enemy.width + 50, enemy.height + 10))
        time.sleep(0.1)

        enemy_strength = reader.readtext(path_temp, detail=0)
        try:
            es_int = int(enemy_strength[1].replace(' ', ''))
        except (IndexError, ValueError):
            es_int = my_strength * 2
        # print(f"Первая проверка. моя сила {my_strength} противника {es_int} ")
        if my_strength >= es_int:
            print(f"Вторая проверка. моя сила {my_strength} противника {es_int} ")
            center = pyautogui.center(enemy)
            pyautogui.click(center)
            time.sleep(2)

            # Дополнительная проверка на открытия окна
            click_fist = pyautogui.locateOnScreen(fist, confidence=0.7)
            if click_fist:
                time.sleep(0.2)

                start_battle_orangeria()

                time.sleep(5)

        number_temp += 1


def start_battle_orangeria():
    """Нажимает кнопку боя  и ждет окончания боя

    Если бой неначался, то проверяет на добавление элементов (энергия или химия)

    """
    click = pyautogui.locateOnScreen(battle_next2, confidence=0.7)
    if click:
        pyautogui.click(click)
        time.sleep(4)

        stop_battle()

        time.sleep(20)
        pyautogui.press('esc')

    else:
        pyautogui.press('esc')


def stop_battle():
    """
    Если энергия закончилась
    кликер закрывает окно
    Вслучае выскакивание добавление ресурсов нажимает бой
    """
    battle_stop = pyautogui.locateOnScreen(stop, confidence=0.6)
    click2 = pyautogui.locateOnScreen(battle_next3, confidence=0.8)
    if battle_stop:
        pyautogui.press('esc')
    elif click2:
        pyautogui.click(click2)

# get_enemy()
