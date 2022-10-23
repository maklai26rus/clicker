import os
import pyautogui

from war_botany.search_coordinate import search_coordinate
import time


class ManageingBot:

    def __init__(self):
        self.text_error = 'error.txt'

        self.path_alliance_rooms = "..//png/alliance_room"
        self.path_alliance = [self.path_alliance_rooms + "/" + file for file in os.listdir(self.path_alliance_rooms)]
        self.path_room_al = [self.path_alliance, ]

        # Проверка АВ
        self.av = "..//png/av/av.PNG"
        self.next_av = "..//png/av/next.PNG"

    def ak_search(self):
        """
        Поиск Альянтосовской комнаты
        выбор ее на главную
        :return:
        """
        alliance_click = list(filter(None, map(search_coordinate, self.path_room_al)))
        try:
            if alliance_click[0]:
                center_click = pyautogui.center(alliance_click[0])
                pyautogui.click(center_click)
        except IndexError:
            with open(f'{self.text_error}', 'a', encoding='utf-8') as er:
                er.write(f"\n {IndexError} ошибка поиска алянтовской комнаты, {time.strftime('%d/%m/%Y %H:%M:%S')}")

    def run_ab(self):
        """
        Выбор АВ
        :return:
        """
        click = pyautogui.locateOnScreen(self.av, confidence=0.8)
        if click:
            pyautogui.click(click)

    def ab_next(self):
        """
        Выбор АВ
        :return:
        """
        click = pyautogui.locateOnScreen(self.next_av, confidence=0.7)
        if click:
            # print('Начала войны')
            pyautogui.click(click)
            time.sleep(0.01)
            pyautogui.press('esc')
        else:
            # print("Война уже начата")
            pyautogui.press('esc')


def main():
    mb = ManageingBot()
    mb.ak_search()


if __name__ == '__main__':
    main()
