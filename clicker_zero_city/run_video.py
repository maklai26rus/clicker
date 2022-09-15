import keyboard
import pyautogui
import time
import os

from search_coordinate import search_coordinate

isClicking = False
video = 'png/reklama.PNG'
video2 = 'png/reklama2.PNG'
prize = 'png/prize.PNG'
rooms = "png/study_rooms"
dining = "png/study_rooms/dining_room"
lab = "png/study_rooms/lab_room"
bank = "png/study_rooms/bank_room"
zal = "png/study_rooms/zal_room"

path_rooms = [rooms + "/" + file for file in os.listdir(rooms)]

path_dining_room = [dining + "/" + file for file in os.listdir(dining)]
path_lab_room = [lab + "/" + file for file in os.listdir(lab)]
path_bank_room = [bank + "/" + file for file in os.listdir(bank)]
path_zal_room = [zal + "/" + file for file in os.listdir(zal)]

path = [path_dining_room, path_lab_room, path_bank_room, path_zal_room]


def definition_advertising():
    """Выбор рекламы с комнат или с планшета"""
    get_vidio = pyautogui.locateOnScreen(video, confidence=0.8)
    if get_vidio:
        return get_vidio
    else:
        get_vidio = pyautogui.locateOnScreen(video2, confidence=0.8)
        return get_vidio


def definition_prize():
    """На планшете после просмотра рекламы нажать забрать приз"""
    click = pyautogui.locateOnScreen(prize, confidence=0.8)
    return click


def set_clicker():
    global isClicking
    if isClicking:
        isClicking = False
        print("Кликер отключен")
    else:
        isClicking = True
        print("Start clicer")


keyboard.add_hotkey('ALT + Z', set_clicker)


def choose_rooms():
    """выбрать комнату для просмотра рекламы"""

    for p in path:
        click = search_coordinate(p)

        if click:
            pyautogui.center(click)
            time.sleep(0.01)
            pyautogui.click(click)
            time.sleep(10)

            get_vidio = pyautogui.locateOnScreen(video, confidence=0.8)
            print('поиск рекламного значка = ', get_vidio)
            if get_vidio:
                print(f"Смотрю рекламу {p}")
                break
            else:
                print(f'Реклама просмотрине по {p}')
                path.remove(p)
                break


def main():
    while True:
        if isClicking:
            choose_rooms()
            click = definition_advertising()
            if click:
                pyautogui.click(click)
                time.sleep(35)

            click2 = definition_prize()
            if click2:
                pyautogui.click(click2)

            time.sleep(3)


if __name__ == '__main__':
    main()
