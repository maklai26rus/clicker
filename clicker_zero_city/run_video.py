import keyboard
import pyautogui
import time
import os

from command_clicker import *
from search_coordinate import search_coordinate_ad

video_rooms = 'png/marketing/marketing1.PNG'
video_tablet = 'png/marketing/marketing2.PNG'
prize = 'png/marketing/prize.PNG'

# rooms = "png/study_rooms"
dining = "png/study_rooms/dining_room"
lab = "png/study_rooms/lab_room"
bank = "png/study_rooms/bank_room"
zal = "png/study_rooms/zal_room"
joinery = "png/study_rooms/joinery"

path_dining_room = [dining + "/" + file for file in os.listdir(dining)]
path_lab_room = [lab + "/" + file for file in os.listdir(lab)]
path_bank_room = [bank + "/" + file for file in os.listdir(bank)]
path_zal_room = [zal + "/" + file for file in os.listdir(zal)]
path_joinery_room = [joinery + "/" + file for file in os.listdir(joinery)]


class AdClicker:
    KITCHEN_ROOM = True
    LAB_ROOM = True
    BANK_ROOM = False
    ZAL_ROOM = True
    JOINERY_ROOM = True

    def __init__(self):
        self.one_click_rk = True

        self.room_kitchen = None
        self.click_repetitions_rk = 1

        self.room_lab = None
        self.click_repetitions_rl = 1

        self.room_joinery = None
        self.click_repetitions_rj = 1

        self.room_bank = None
        self.click_repetitions_rb = 1

        self.room_zal = None
        self.click_repetitions_rz = 1

    def kitchen_rooms(self):
        self.room_kitchen = list(filter(None, map(search_coordinate_ad, path_dining_room)))
        time.sleep(1)
        if self.click_repetitions_rk > 3:
            AdClicker.KITCHEN_ROOM = False
            self.one_click_rk = True
        elif self.room_kitchen:
            print('Кухня', self.room_kitchen[0])
            center = pyautogui.center(self.room_kitchen[0])
            pyautogui.moveTo(center)
            if self.one_click_rk:
                pyautogui.click(center)
                self.one_click_rk = False

            self.click_repetitions_rk += 1
            time.sleep(5)
            self.preview_room()
        else:
            self.one_click_rk = True

    def preview_room(self):
        """Предварительный просмотр рекламы"""
        get_vidio = pyautogui.locateOnScreen(video_rooms, confidence=0.8)
        if get_vidio:
            pyautogui.click(get_vidio)
            time.sleep(40)

    def preview_tablet(self):
        """Предварительный просмотр рекламы"""
        get_vidio = pyautogui.locateOnScreen(video_tablet, confidence=0.8)
        if get_vidio:
            pyautogui.click(get_vidio)
            time.sleep(40)

    def definition_prize(self):
        """На планшете после просмотра рекламы нажать забрать приз"""
        click = pyautogui.locateOnScreen(prize, confidence=0.8)
        if click:
            pyautogui.click(click)

    def laboratory_room(self):
        self.room_lab = list(filter(None, map(search_coordinate_ad, path_lab_room)))
        time.sleep(1)
        if self.click_repetitions_rl > 3:
            AdClicker.LAB_ROOM = False
            self.one_click_rk = True
        elif self.room_lab:
            print('Лаб')
            center = pyautogui.center(self.room_lab[0])
            pyautogui.moveTo(center)
            if self.one_click_rk:
                pyautogui.click(center)
                self.one_click_rk = False

            self.click_repetitions_rl += 1
            time.sleep(5)
            self.preview_room()
        else:
            self.one_click_rk = True

    def joinery_room(self):
        self.room_joinery = list(filter(None, map(search_coordinate_ad, path_joinery_room)))
        time.sleep(1)
        if self.click_repetitions_rj > 3:
            AdClicker.JOINERY_ROOM = False
            self.one_click_rk = True
        elif self.room_joinery:
            print('Лесопилка')
            center = pyautogui.center(self.room_joinery[0])
            pyautogui.moveTo(center)
            if self.one_click_rk:
                pyautogui.click(center)
                self.one_click_rk = False

            self.click_repetitions_rj += 1
            time.sleep(5)
            self.preview_room()
        else:
            self.one_click_rk = True

    def bank_room(self):
        self.room_bank = list(filter(None, map(search_coordinate_ad, path_bank_room)))
        time.sleep(1)
        if self.click_repetitions_rb > 3:
            AdClicker.BANK_ROOM = False
            self.one_click_rk = True
        elif self.room_bank:
            print('BANK')
            center = pyautogui.center(self.room_bank[0])
            pyautogui.moveTo(center)
            if self.one_click_rk:
                pyautogui.click(center)
                self.one_click_rk = False

            self.click_repetitions_rb += 1
            time.sleep(5)
            self.preview_room()
        else:
            self.one_click_rk = True

    def zal_room(self):
        self.room_zal = list(filter(None, map(search_coordinate_ad, path_zal_room)))
        time.sleep(1)
        if self.click_repetitions_rb > 3:
            AdClicker.ZAL_ROOM = False
            self.one_click_rk = True
        elif self.room_zal:
            print('ZAL')
            center = pyautogui.center(self.room_zal[0])
            pyautogui.moveTo(center)
            if self.one_click_rk:
                pyautogui.click(center)
                self.one_click_rk = False

            self.click_repetitions_rb += 1
            time.sleep(5)
            self.preview_room()
        else:
            self.one_click_rk = True


keyboard.add_hotkey('ALT + Z', advertising_rooms)
keyboard.add_hotkey('ALT + X', advertising_tablet)


def main():
    preview = AdClicker()
    while True:
        if choosing_action["rooms"]:
            if preview.KITCHEN_ROOM:
                preview.kitchen_rooms()
            elif preview.LAB_ROOM:
                preview.laboratory_room()
            elif preview.JOINERY_ROOM:
                preview.joinery_room()
            elif preview.ZAL_ROOM:
                preview.zal_room()
            elif preview.BANK_ROOM:
                preview.bank_room()

        if choosing_action['tablet']:
            preview.preview_tablet()
            preview.definition_prize()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Закрытия программы')
