import pyautogui
import time
import os
from clicker_zero_city.search_coordinate import search_coordinate_ad


class AdClicker:

    def __init__(self):
        self.KITCHEN_ROOM = False
        self.LAB_ROOM = False
        self.BANK_ROOM = False
        self.ZAL_ROOM = False
        self.FORGE_ROOM = False
        self.JOINERY_ROOM = False

        self.one_click_rk = True
        # Время просмотра рекламы. Хочу сделать регулируемое
        self.waiting_for_end = 40

        self.click_repetitions = 1

        self.video_rooms = 'png/marketing/marketing1.PNG'
        self.video_tablet = 'png/marketing/marketing2.PNG'
        self.prize = 'png/marketing/prize.PNG'

        # self.dining = "..//png/study_rooms/dining_room"
        self.dining = "png/study_rooms/dining_room"
        self.lab = "png/study_rooms/lab_room"
        self.bank = "png/study_rooms/bank_room"
        self.zal = "png/study_rooms/zal_room"
        self.joinery = "png/study_rooms/joinery_room"
        self.forge = "png/study_rooms/forge_room"

    def path_png(self, path: list):
        """
        Выбор по координате комнату
        Если координата нашлась. наводит курсор мышки на нее и 1 раз кликает

        """
        if path:
            center = pyautogui.center(path[0])
            pyautogui.moveTo(center)
            if self.one_click_rk:
                pyautogui.click(center)
                self.one_click_rk = False
            else:
                self.click_repetitions += 1

    def preview_room(self):
        """Предварительный просмотр рекламы"""
        get_vidio = pyautogui.locateOnScreen(self.video_rooms, confidence=0.8)
        if get_vidio:
            pyautogui.click(get_vidio)
            time.sleep(self.waiting_for_end)

    def preview_tablet(self):
        """Предварительный просмотр рекламы"""
        get_vidio = pyautogui.locateOnScreen(self.video_tablet, confidence=0.8)
        if get_vidio:
            pyautogui.click(get_vidio)
            time.sleep(self.waiting_for_end)

    def definition_prize(self):
        """На планшете после просмотра рекламы нажать забрать приз"""
        click = pyautogui.locateOnScreen(self.prize, confidence=0.8)
        if click:
            pyautogui.click(click)

    def path_normal(self, path):
        """Модюль преобразующий в правильный путь для координат"""
        _pn = os.path.normpath(os.path.join(path))
        path_dining_room = [_pn + "\\" + file for file in os.listdir(_pn)]
        path = list(filter(None, map(search_coordinate_ad, path_dining_room)))
        return path

    def kitchen_rooms(self):
        """
        Ищет координаты картинок для получение рекламы

        """
        path = self.path_normal(self.dining)
        time.sleep(1)
        if self.preview_room():
            self.click_repetitions += 1
        elif self.click_repetitions > 3:
            self.KITCHEN_ROOM = False
            self.one_click_rk = True
            self.click_repetitions = 1
        elif self.KITCHEN_ROOM:
            self.path_png(path)

        # print(f'Кухня найденый координат {len(path)}', self.click_repetitions)

        # time.sleep(5)

    def laboratory_room(self):
        path = self.path_normal(self.lab)
        time.sleep(1)
        if self.preview_room():
            self.click_repetitions += 1
        elif self.click_repetitions > 3:
            self.LAB_ROOM = False
            self.one_click_rk = True
            self.click_repetitions = 1
        elif self.LAB_ROOM:
            self.path_png(path)

        # print(f'Лаборатория найденый координат {len(path)}', self.click_repetitions)

    def joinery_room(self):
        """
        Ищет координаты картинок для получение рекламы
        Комната улучшения добычи дерева
        """
        path = self.path_normal(self.joinery)
        time.sleep(1)
        if self.preview_room():
            self.click_repetitions += 1

        elif self.click_repetitions > 3:
            self.JOINERY_ROOM = False
            self.one_click_rk = True
            self.click_repetitions = 1
        elif self.JOINERY_ROOM:

            self.path_png(path)
        # print(f'Лесопилка найденый координат {len(path)}', self.click_repetitions)

    def bank_room(self):
        """
        Ищет координаты картинок для получение рекламы
        Комната улучшения добычи денег
        """
        path = self.path_normal(self.bank)
        time.sleep(1)
        if self.preview_room():
            self.click_repetitions += 1
        elif self.click_repetitions > 3:
            self.BANK_ROOM = False
            self.one_click_rk = True
            self.click_repetitions = 1
        elif self.BANK_ROOM:
            self.path_png(path)

        # print(f'Банк', path, self.click_repetitions)

    def zal_room(self):
        """
        Ищет координаты картинок для получение рекламы
        Комната по повышению силы
        """
        path = self.path_normal(self.zal)
        time.sleep(1)
        if self.preview_room():
            self.click_repetitions += 1

        elif self.click_repetitions > 3:
            self.ZAL_ROOM = False
            self.one_click_rk = True
            self.click_repetitions = 1
        elif self.ZAL_ROOM:
            self.path_png(path)
        # print(f'Спортзал', path, self.click_repetitions)
        # time.sleep(5)

    def forge_room(self):
        """
        Ищет координаты картинок для получение рекламы
        Комната улучшению добычи металла
        """
        path = self.path_normal(self.forge)
        time.sleep(1)
        if self.preview_room():
            self.click_repetitions += 1
        elif self.click_repetitions > 3:
            self.FORGE_ROOM = False
            self.one_click_rk = True
            self.click_repetitions = 1
        elif self.FORGE_ROOM:
            self.path_png(path)
        # print(f'Кузница найденый координат {len(path)}', self.click_repetitions)

        # time.sleep(5)

# def watch_ads():
#     """Ручной запуск
#     только если не работает виндоус окно
#     """
#     keyboard.add_hotkey('ALT + Z', advertising_rooms)
#     keyboard.add_hotkey('ALT + X', advertising_tablet)
#     preview = AdClicker()
#     preview.KITCHEN_ROOM = True
#     preview.ZAL_ROOM = False
#     preview.BANK_ROOM = False
#     preview.LAB_ROOM = False
#     preview.FORGE_ROOM = False
#     preview.JOINERY_ROOM = False
#     while True:
#         print('1')
#         if choosing_action["rooms"]:
#             if preview.KITCHEN_ROOM:
#                 preview.kitchen_rooms()
#             elif preview.LAB_ROOM:
#                 preview.laboratory_room()
#             elif preview.JOINERY_ROOM:
#                 preview.joinery_room()
#             elif preview.ZAL_ROOM:
#                 preview.zal_room()
#             elif preview.BANK_ROOM:
#                 preview.bank_room()
#             elif preview.FORGE_ROOM:
#                 preview.forge_room()
#
#         if choosing_action['tablet']:
#             preview.preview_tablet()
#             preview.definition_prize()
