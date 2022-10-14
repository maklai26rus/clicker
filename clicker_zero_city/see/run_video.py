import pyautogui
import time
import os
from clicker_zero_city.search_coordinate import search_coordinate_ad


class AdClicker:
    """
    Класс отвечающий за просмотр рекламы

    """

    def __init__(self):
        self.KITCHEN_ROOM = False
        self.LAB_ROOM = False
        self.BANK_ROOM = False
        self.ZAL_ROOM = False
        self.FORGE_ROOM = False
        self.JOINERY_ROOM = False

        self.res_food = False
        self.res_food_counter = 1
        self.res_metal = False
        self.res_metal_counter = 1
        self.res_baks = False
        self.res_baks_counter = 1
        self.res_wood = False
        self.res_wood_counter = 1
        self.res_vial = False
        self.res_vial_counter = 1

        # Разовое нажатие на выбранную комнату
        self.one_click_rk = True
        # Время просмотра рекламы. Хочу сделать регулируемое
        self.waiting_for_end = 40

        self.click_repetitions = 1

        self.path_video_rooms = 'png/marketing/marketing1.PNG'
        self.path_video_tablet = 'png/marketing/marketing2.PNG'
        self.path_prize = 'png/marketing/prize.PNG'

        self.path_room_kitchen = "png/study_rooms/dining_room"
        self.path_room_lab = "png/study_rooms/lab_room"
        self.path_room_bank = "png/study_rooms/bank_room"
        self.path_room_zal = "png/study_rooms/zal_room"
        self.path_room_joinery = "png/study_rooms/joinery_room"
        self.path_room_forge = "png/study_rooms/forge_room"
        self.path_movie = "png/marketing/movie.PNG"
        self.path_add_res = "png/marketing/add_res.PNG"
        self.path_step1 = "png/marketing/step1.PNG"
        self.path_step2 = "png/marketing/step2.PNG"

        self.path_food = "png/marketing/food.PNG"
        self.path_baks = "png/marketing/baks.PNG"
        self.path_metal = "png/marketing/metal.PNG"
        self.path_vial = "png/marketing/vial.PNG"
        self.path_wood = "png/marketing/wood.PNG"

    def get_metal_res(self, path, counter=1):
        """
        Смотрим рекламу для получение ресурсов

        """
        _pn = os.path.normpath(os.path.join(path))
        get_res = pyautogui.locateOnScreen(_pn, confidence=0.8)
        if get_res and counter <= 2:
            print(counter)
            pyautogui.click(get_res)
            time.sleep(2)
            self.preview_res()
            counter += 1
        time.sleep(3)

    def preview_res(self):
        """Предварительный просмотр рекламы"""
        get_vidio = pyautogui.locateOnScreen(self.path_add_res, confidence=0.8)
        if get_vidio:
            pyautogui.click(get_vidio)

    def get_room_list(self, path: list):
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
        get_vidio = pyautogui.locateOnScreen(self.path_video_rooms, confidence=0.8)
        if get_vidio:
            pyautogui.click(get_vidio)
            time.sleep(self.waiting_for_end)

    def preview_tablet(self):
        """Предварительный просмотр рекламы"""
        get_vidio = pyautogui.locateOnScreen(self.path_video_tablet, confidence=0.8)
        if get_vidio:
            pyautogui.click(get_vidio)
            time.sleep(self.waiting_for_end)

    def definition_prize(self):
        """На планшете после просмотра рекламы нажать забрать приз"""
        click = pyautogui.locateOnScreen(self.path_prize, confidence=0.8)
        if click:
            pyautogui.click(click)

    def path_normal(self, path) -> list:
        """Модюль преобразующий в правильный путь для координат"""
        _pn = os.path.normpath(os.path.join(path))
        path_dining_room = [_pn + "\\" + file for file in os.listdir(_pn)]
        path = list(filter(None, map(search_coordinate_ad, path_dining_room)))
        return path

    def cheking_tablet(self):
        """Проверка на рекламу в планшете. если непоявилась снопка крекламы но есть возможостить смотреть ее.
        то делает клик по вверхней иконке и назад
         ....
        """
        get_movie = pyautogui.locateOnScreen(self.path_movie, confidence=0.8)
        get_vidio = pyautogui.locateOnScreen(self.path_video_tablet, confidence=0.8)
        if get_movie and get_vidio:
            return True
        elif get_movie:
            get_movie1 = pyautogui.locateOnScreen(self.path_step1, confidence=0.8)
            pyautogui.click(get_movie1)
            time.sleep(1)
            get_movie2 = pyautogui.locateOnScreen(self.path_step2, confidence=0.8)
            pyautogui.click(get_movie2)
            time.sleep(1)

    def kitchen_rooms(self):
        """
        Ищет координаты картинок для получение рекламы

        """
        if self.preview_room():
            self.click_repetitions += 1
        elif self.click_repetitions > 3:
            self.KITCHEN_ROOM = False
            self.one_click_rk = True
            self.click_repetitions = 1
        elif self.KITCHEN_ROOM:
            path = self.path_normal(self.path_room_kitchen)
            time.sleep(1)
            self.get_room_list(path)

        # print(f'Кухня найденый координат {len(path)}', self.click_repetitions)

        # time.sleep(5)

    def laboratory_room(self):
        """
        Ищет координаты картинок для получение рекламы
        Комната улучшения знаний в лаборатории
        """
        if self.preview_room():
            self.click_repetitions += 1
        elif self.click_repetitions > 3:
            self.LAB_ROOM = False
            self.one_click_rk = True
            self.click_repetitions = 1
        elif self.LAB_ROOM:
            path = self.path_normal(self.path_room_lab)
            time.sleep(1)
            self.get_room_list(path)

        # print(f'Лаборатория найденый координат {len(path)}', self.click_repetitions)

    def joinery_room(self):
        """
        Ищет координаты картинок для получение рекламы
        Комната улучшения добычи дерева
        """
        if self.preview_room():
            self.click_repetitions += 1
        elif self.click_repetitions > 3:
            self.JOINERY_ROOM = False
            self.one_click_rk = True
            self.click_repetitions = 1
        elif self.JOINERY_ROOM:
            path = self.path_normal(self.path_room_joinery)
            time.sleep(1)
            self.get_room_list(path)
        # print(f'Лесопилка найденый координат {len(path)}', self.click_repetitions)

    def bank_room(self):
        """
        Ищет координаты картинок для получение рекламы
        Комната улучшения добычи денег
        """
        if self.preview_room():
            self.click_repetitions += 1
        elif self.click_repetitions > 3:
            self.BANK_ROOM = False
            self.one_click_rk = True
            self.click_repetitions = 1
        elif self.BANK_ROOM:
            path = self.path_normal(self.path_room_bank)
            time.sleep(1)
            self.get_room_list(path)

        # print(f'Банк', path, self.click_repetitions)

    def zal_room(self):
        """
        Ищет координаты картинок для получение рекламы
        Комната по повышению силы
        """
        if self.preview_room():
            self.click_repetitions += 1
        elif self.click_repetitions > 3:
            self.ZAL_ROOM = False
            self.one_click_rk = True
            self.click_repetitions = 1
        elif self.ZAL_ROOM:
            path = self.path_normal(self.path_room_zal)
            time.sleep(1)
            self.get_room_list(path)
        # print(f'Спортзал', path, self.click_repetitions)
        # time.sleep(5)

    def forge_room(self):
        """
        Ищет координаты картинок для получение рекламы
        Комната улучшению добычи металла
        """
        if self.preview_room():
            self.click_repetitions += 1
        elif self.click_repetitions > 3:
            self.FORGE_ROOM = False
            self.one_click_rk = True
            self.click_repetitions = 1
        elif self.FORGE_ROOM:
            path = self.path_normal(self.path_room_forge)
            time.sleep(1)
            self.get_room_list(path)
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
