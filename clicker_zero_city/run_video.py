import keyboard
import pyautogui
import time
import os

from command_clicker import *
from search_coordinate import search_coordinate

video_rooms = 'png/reklama.PNG'
video_tablet = 'png/reklama2.PNG'
prize = 'png/prize.PNG'

rooms = "png/study_rooms"
dining = "png/study_rooms/dining_room"
lab = "png/study_rooms/lab_room"
bank = "png/study_rooms/bank_room"
zal = "png/study_rooms/zal_room"
joinery = "png/study_rooms/joinery"

path_rooms = [rooms + "/" + file for file in os.listdir(rooms)]

path_dining_room = [dining + "/" + file for file in os.listdir(dining)]
path_lab_room = [lab + "/" + file for file in os.listdir(lab)]
path_bank_room = [bank + "/" + file for file in os.listdir(bank)]
path_zal_room = [zal + "/" + file for file in os.listdir(zal)]
path_joinery_room = [joinery + "/" + file for file in os.listdir(joinery)]

path = [path_joinery_room, path_dining_room, path_lab_room, path_bank_room, path_zal_room, ]

keyboard.add_hotkey('ALT + Z', advertising_rooms)
keyboard.add_hotkey('ALT + X', advertising_tablet)


def definition_advertising_rooms():
    """Выбор рекламы в комнат """
    get_vidio = pyautogui.locateOnScreen(video_rooms, confidence=0.8)
    if get_vidio:
        return get_vidio


def definition_advertising_tablet():
    """Выбор рекламы в планшета"""
    get_vidio = pyautogui.locateOnScreen(video_tablet, confidence=0.8)
    if get_vidio:
        return get_vidio


def definition_prize():
    """На планшете после просмотра рекламы нажать забрать приз"""
    click = pyautogui.locateOnScreen(prize, confidence=0.8)
    return click


def choose_rooms():
    """выбрать комнату для просмотра рекламы"""
    try:
        room = list(map(search_coordinate, path))
        return room[0]
    except IndexError:
        return None


def main():
    one_time_click = True
    while True:
        if choosing_action["rooms"]:
            room = choose_rooms()
            if room:
                if one_time_click:
                    pyautogui.click(room)
                time.sleep(5)
                click_rooms = definition_advertising_rooms()
                if click_rooms:
                    pyautogui.click(click_rooms)
                    time.sleep(35)
                    one_time_click = False
                else:
                    del path[0]
                    one_time_click = True

        if choosing_action['tablet']:
            click_tablet = definition_advertising_tablet()

            if click_tablet:
                time.sleep(1)
                pyautogui.click(click_tablet)
                time.sleep(35)

            click_prize = definition_prize()
            if click_prize:
                time.sleep(1)
                pyautogui.click(click_prize)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Закрытия программы')
