import pyautogui
import time
from search_coordinate import search_coordinate
import os

# Запуск игры через лайнчера
launcher = 'png/start_game/MGLauncher.PNG'
zero = 'png/start_game/Zero.PNG'
game = 'png/start_game/games.PNG'

# Поиск комнаты Альянса
path_alliance_rooms = "png/alliance_room"
path_alliance = [path_alliance_rooms + "/" + file for file in os.listdir(path_alliance_rooms)]
path_room_al = [path_alliance, ]

# Проверка АВ
av = "png/av/av.PNG"
next_av = "png/av/next.PNG"

# Возможные рекламные тригеры
advertising = "png/advertising"
path_advertising = [advertising + "/" + file for file in os.listdir(advertising)]
path = [path_advertising, ]


def time_game(func):
    def other_func():
        time.sleep(5)
        func()
        return func

    return other_func


def start_var_av():
    """Запуск скрипта"""
    finding_shortcut()
    game_selection()
    run_game()
    choose_closing_ads()
    ak_search()
    if run_ab():
        ab_next()


def finding_shortcut():
    """Поиск ярлыка на рабочем столе"""
    click = pyautogui.locateOnScreen(launcher, confidence=0.8)
    pyautogui.doubleClick(click)


@time_game
def game_selection():
    """Выбор игры"""
    click = pyautogui.locateOnScreen(zero)
    pyautogui.click(click)


@time_game
def run_game():
    """
    Запуск игры
    :return:
    """
    click = pyautogui.locateOnScreen(game)
    pyautogui.click(click)


@time_game
def choose_closing_ads():
    """Закрытия рекламы
    Поиск рекламы. Берет из папки все рекламные привязки и ищет их координат

    Если находит закрывает и перезапускает сам себя для повторной проверки на рекламу.
    Если рекламы нет. то нечего неделает

    """
    time.sleep(10)
    advertising_click = list(filter(None, map(search_coordinate, path)))

    try:
        if advertising_click[0]:
            print('Закрытия рекламы')
            ac = pyautogui.center(advertising_click[0])
            pyautogui.click(ac)
            pyautogui.press('esc')
            time.sleep(10)
            choose_closing_ads()
    except IndexError:
        pass


@time_game
def ak_search():
    """
    Поиск Альянтосовской комнаты
    выбор ее на главную
    :return:
    """
    alliance_click = list(filter(None, map(search_coordinate, path_room_al)))
    if alliance_click[0]:
        center_click = pyautogui.center(alliance_click[0])
        pyautogui.click(center_click)


@time_game
def run_ab():
    """
    Выбор АВ
    :return:
    """
    click = pyautogui.locateOnScreen(av, confidence=0.8)
    if click:
        pyautogui.click(click)


@time_game
def ab_next():
    """
    Выбор АВ
    :return:
    """
    click = pyautogui.locateOnScreen(next_av, confidence=0.7)
    if click:
        print('Начала войны')
        pyautogui.click(click)
        time.sleep(0.01)
        pyautogui.press('esc')
    else:
        print("Война уже начата")
        pyautogui.press('esc')
