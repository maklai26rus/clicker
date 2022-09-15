import pyautogui
import time

global_map = "png/global_maps.PNG"
kater = "png/kater.PNG"
orang = "png/orang.PNG"
battle = 'png/battle.PNG'
battle_next = 'png/battle_next.PNG'


def time_game(func):
    def other_func():
        time.sleep(5)
        func()
        return func

    return other_func


def start_var_orangeria():
    """Запуск скрипта"""
    global_maps()


@time_game
def global_maps():
    """
    Переходим на глобальную карту для поиска  оранжереи
    :return:
    """
    click = pyautogui.locateOnScreen(global_map, confidence=0.5)
    pyautogui.click(click)
    time.sleep(1)

    if greenhouse_search():
        pass
    else:
        boat_search()
        greenhouse_search()

    run_battle()


def boat_search():
    """
    Ищем на карте катер и привязываемся кнему что бы перетащить мышкку
    :return:
    """
    click = pyautogui.locateOnScreen(kater, confidence=0.4)
    if click:
        pyautogui.click(click)
        pyautogui.dragTo(100, 0, 1, button='left')


def greenhouse_search():
    """
    Определяем на карте оранжерею
    :return:
    """
    click = pyautogui.locateOnScreen(orang, confidence=0.5)
    if click:
        pyautogui.click(click)
        time.sleep(10)


def run_battle():
    """
    Начинаем бой в оранжереи
    :return:
    """
    click = list(pyautogui.locateAllOnScreen(battle, confidence=0.93))
    for b in click:
        center = pyautogui.center(b)
        pyautogui.click(center)
        time.sleep(0.2)
        start_battle_orangeria()
        time.sleep(5)


def start_battle_orangeria():
    click = pyautogui.locateOnScreen(battle_next, confidence=0.6)
    if click:
        pyautogui.click(click)
        time.sleep(20)
        pyautogui.press('esc')
    else:
        pyautogui.press('esc')

