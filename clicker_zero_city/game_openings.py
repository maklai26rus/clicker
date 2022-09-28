import pyautogui
import time
from search_coordinate import search_coordinate
import os

# Запуск игры через лайнчера
launcher = 'png/start_game/Zerolauncher.PNG'
game = 'png/start_game/games.PNG'

# Возможные рекламные тригеры
advertising = "png/advertising"
cross = "png/X/X.PNG"
path_advertising = [advertising + "/" + file for file in os.listdir(advertising)]
path = [path_advertising, ]


def time_game(func):
    def other_func():
        time.sleep(10)
        func()
        return func

    return other_func


def eternal_search(func):
    """
    Зацикленая функция для поиска координат
    """
    def search():
        while True:
            sh = func()
            if sh:
                center = pyautogui.center(sh)
                pyautogui.doubleClick(center)
                break
            else:
                print('Не могу найти корданату. Проверте если она на месте?')

    return search


def open_game():
    """Запуск скрипта"""
    finding_shortcut()
    run_game()
    choose_closing_ads()


@eternal_search
def finding_shortcut():
    """Поиск ярлыка на рабочем столе"""
    click = pyautogui.locateOnScreen(launcher, confidence=0.8)
    return click


@time_game
@eternal_search
def run_game():
    """
    Запуск игры
    :return:
    """
    click = pyautogui.locateOnScreen(game, confidence=0.8)
    return click


# @time_game
def choose_closing_ads():
    """Закрытия рекламы
    Поиск рекламы. Берет из папки все рекламные привязки и ищет их координат

    Если находит закрывает и перезапускает сам себя для повторной проверки на рекламу.
    Если рекламы нет. то нечего неделает

    """
    time.sleep(10)
    advertising_click = list(filter(None, map(search_coordinate, path)))
    advertising_click_x = pyautogui.locateOnScreen(cross, confidence=0.65)
    try:
        if advertising_click_x:
            print('Закрытия рекламы Х')
            center = pyautogui.center(advertising_click_x)
            pyautogui.click(advertising_click_x)
            time.sleep(10)
            choose_closing_ads()

        if advertising_click[0]:
            print('Закрытия рекламы')
            ac = pyautogui.center(advertising_click[0])
            pyautogui.click(ac)
            pyautogui.press('esc')
            time.sleep(10)
            choose_closing_ads()
    except IndexError:
        pass

# choose_closing_ads()