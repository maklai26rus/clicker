import pyautogui
import time
from search_coordinate import search_coordinate
import os

# Запуск игры через лайнчера
launcher = 'png/start_game/Zerolauncher.PNG'
game = 'png/start_game/games.PNG'

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


def open_game():
    """Запуск скрипта"""
    finding_shortcut()
    run_game()
    choose_closing_ads()


def finding_shortcut():
    """Поиск ярлыка на рабочем столе"""
    click = pyautogui.locateOnScreen(launcher, confidence=0.8)
    pyautogui.doubleClick(click)


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

