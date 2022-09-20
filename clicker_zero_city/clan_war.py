import pyautogui
import time
from search_coordinate import search_coordinate
import os

# Поиск комнаты Альянса
path_alliance_rooms = "png/alliance_room"
path_alliance = [path_alliance_rooms + "/" + file for file in os.listdir(path_alliance_rooms)]
path_room_al = [path_alliance, ]

# Проверка АВ
av = "png/av/av.PNG"
next_av = "png/av/next.PNG"


def time_game(func):
    def other_func():
        time.sleep(5)
        func()
        return func

    return other_func


def clan_war():
    """Запуск скрипта"""
    ak_search()
    if run_ab():
        ab_next()


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
