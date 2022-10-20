import pyautogui
import time
import os
from clicker_zero_city.search_coordinate import search_coordinate_ad


class AdClicker:
    """
    Класс отвечающий за просмотр рекламы

    """

    def __init__(self):

        self.checking_room_kitchen = False
        self.counter_room_kitchen = 1

        self.checking_room_lab = False
        self.counter_room_lab = 1

        self.checking_room_bank = False
        self.counter_room_bank = 1

        self.checking_room_zal = False
        self.counter_room_zal = 1

        self.checking_room_forge = False
        self.counter_room_forge = 1

        self.checking_room_sawmill = False
        self.counter_room_sawmill = 1

        self.previous_room = ''

        self.res_food = False
        self.counter_res_food = 2
        self.res_metal = False
        self.counter_res_metal = 2
        self.res_baks = False
        self.counter_res_baks = 2
        self.res_wood = False
        self.counter_res_wood = 2
        self.res_vial = False
        self.counter_res_vial = 2

        self.ads_in_arena = False
        self.counter_ads_in_arena = 2
        self.ads_in_tunnel = False
        self.counter_ads_in_tunnel = 4
        self.ads_in_bunker = False
        self.counter_ads_in_bunker = 2
        self.ads_in_terminal = False
        self.counter_ads_in_terminal = 2

        # Разовое нажатие на выбранную комнату
        self.one_click_rk = True
        # Время просмотра рекламы. Хочу сделать регулируемое
        self.waiting_for_end = 40
        # click_repetitions клик сколько раз нажали на рекаламу
        self.click_repetitions = 1
        # Максимальное кол-во просмотра рекламы
        self.max_see = 3

        self.path_video_rooms = 'png/marketing/marketing1.PNG'
        self.path_video_tablet = 'png/marketing/marketing2.PNG'
        self.path_prize = 'png/marketing/prize.PNG'

        self.path_room_kitchen = "png/study_rooms/dining_room"
        self.path_room_lab = "png/study_rooms/lab_room"
        self.path_room_bank = "png/study_rooms/bank_room"
        self.path_room_zal = "png/study_rooms/zal_room"
        self.path_room_sawmill = "png/study_rooms/sawmill_room"
        self.path_room_forge = "png/study_rooms/forge_room"

        self.path_tablet = "png/marketing/tablet.PNG"
        self.path_movie = "png/marketing/movie.PNG"
        self.path_add_res = "png/marketing/add_res.PNG"
        self.path_step1 = "png/marketing/step1.PNG"
        self.path_step2 = "png/marketing/step2.PNG"

        self.path_food = "png/marketing/food.PNG"
        self.path_baks = "png/marketing/baks.PNG"
        self.path_metal = "png/marketing/metal.PNG"
        self.path_vial = "png/marketing/vial.PNG"
        self.path_wood = "png/marketing/wood.PNG"

        self.path_arena = "png/marketing/arena.PNG"
        self.path_terminal = "png/marketing/terminal.PNG"
        self.path_bunker = "png/marketing/bunker.PNG"
        self.path_tunnel = "png/marketing/tunel.PNG"
        # self.path_add_res = "png/marketing/add_res.PNG"

    def getting_resources_location(self, path, counter, resource):
        """
        Смотрим рекламу для получение ресурсов
        введения счечика просмотра рекламы
        path = путь к картинке получения ресурса
        counter = счечик. сколько раз просмотреть рекламу
        resource= что за выбраный ресурс

        """
        _pn = os.path.normpath(os.path.join(path))
        get_pn = pyautogui.locateOnScreen(_pn, confidence=0.7)
        if get_pn and counter > 0:
            pyautogui.click(get_pn)
            time.sleep(1)

            get_pvt = pyautogui.locateOnScreen(self.path_video_tablet, confidence=0.8)
            if get_pvt:
                pyautogui.click(get_pvt)
                if resource == 'arena':
                    self.counter_res_metal -= 1
                elif resource == 'terminal':
                    self.counter_res_food -= 1
                elif resource == 'bunker':
                    self.counter_res_wood -= 1
                elif resource == 'tunnel':
                    self.counter_res_baks -= 1

        time.sleep(3)

    def getting_resources(self, path, counter, resource):
        """
        Смотрим рекламу для получение ресурсов
        введения счечика просмотра рекламы
        path = путь к картинке получения ресурса
        counter = счечик. сколько раз просмотреть рекламу
        resource= что за выбраный ресурс

        """
        _pn = os.path.normpath(os.path.join(path))
        get_pn = pyautogui.locateOnScreen(_pn, confidence=0.7)
        if get_pn and counter > 0:
            pyautogui.click(get_pn)
            time.sleep(1)

            get_par = pyautogui.locateOnScreen(self.path_add_res, confidence=0.8)
            if get_par:
                pyautogui.click(get_par)
                if resource == 'metal':
                    self.counter_res_metal -= 1
                elif resource == 'food':
                    self.counter_res_food -= 1
                elif resource == 'wood':
                    self.counter_res_wood -= 1
                elif resource == 'baks':
                    self.counter_res_baks -= 1
                elif resource == 'vial':
                    self.counter_res_vial -= 1

        time.sleep(3)

    def get_room_list(self, path: list):
        """
        Выбор по координате комнату
        Если координата нашлась. наводит курсор мышки на нее и 1 раз кликает

        """
        if path:
            center = pyautogui.center(path[0])
            # pyautogui.moveTo(center)
            if self.one_click_rk:
                pyautogui.click(center)
                # self.one_click_rk = False
            # else:
            #     self.click_repetitions += 1

    def preview_room(self):
        """Предварительный просмотр рекламы"""
        get_vidio = pyautogui.locateOnScreen(self.path_video_rooms, confidence=0.8)
        if get_vidio:
            pyautogui.click(get_vidio)
            # time.sleep(self.waiting_for_end)

    def preview_tablet(self):
        """Предварительный просмотр рекламы"""
        get_vidio = pyautogui.locateOnScreen(self.path_video_tablet, confidence=0.8)
        if get_vidio:
            pyautogui.click(get_vidio)
            # time.sleep(self.waiting_for_end)

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

    def tablet_search(self):
        get_tablet = pyautogui.locateOnScreen(self.path_tablet, confidence=0.9)
        if get_tablet:
            pyautogui.click(get_tablet)
            time.sleep(1)
            get_movie2 = pyautogui.locateOnScreen(self.path_step2, confidence=0.8)
            pyautogui.click(get_movie2)

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

    def test_rooms(self, counter, path_room, resource):
        """
        Ищет координаты картинок для получение рекламы
        room комната для просмотра рекламы
        counter кол-во раз смотреть рекламу
        path_room путь к деректории
        """
        time.sleep(2)
        get_pn = self.path_normal(path_room)
        if get_pn and counter > 0:
            if self.previous_room != resource:
                self.get_room_list(get_pn)
                self.previous_room = resource

            time.sleep(4)
            get_pvr = pyautogui.locateOnScreen(self.path_video_rooms, confidence=0.8)
            if get_pvr:
                pyautogui.click(get_pvr)
                """Кастыль. Иногда при нажатии рекламы, реклама не проигрывает
                Теперь при просмотре добавится просмотр в комнате лишний. 
                """
                if resource == 'kitchen':
                    self.counter_room_kitchen += 1
                elif resource == 'sawmill':
                    self.counter_room_sawmill += 1
                elif resource == 'lab':
                    self.counter_room_lab += 1
                elif resource == 'bank':
                    self.counter_room_bank += 1
                elif resource == 'zal':
                    self.counter_room_zal += 1
                elif resource == 'forge':
                    self.counter_room_forge += 1

            if resource == 'kitchen':
                self.counter_room_kitchen -= 1
            elif resource == 'sawmill':
                self.counter_room_sawmill -= 1
            elif resource == 'lab':
                self.counter_room_lab -= 1
            elif resource == 'bank':
                self.counter_room_bank -= 1
            elif resource == 'zal':
                self.counter_room_zal -= 1
            elif resource == 'forge':
                self.counter_room_forge -= 1

        time.sleep(3)
    # def test_rooms(self, counter, path_room, resource):
    #     """
    #     Ищет координаты картинок для получение рекламы
    #     room комната для просмотра рекламы
    #     counter кол-во раз смотреть рекламу
    #     path_room путь к деректории
    #     """
    #     get_pvr = pyautogui.locateOnScreen(self.path_video_rooms, confidence=0.8)
    #
    #     if get_pvr and counter > 0:
    #
    #         pyautogui.click(get_pvr)
    #
    #         if resource == 'kitchen':
    #             self.counter_room_kitchen -= 1
    #         elif resource == 'sawmill':
    #             self.counter_room_sawmill -= 1
    #         elif resource == 'lab':
    #             self.counter_room_lab -= 1
    #         elif resource == 'bank':
    #             self.counter_room_bank -= 1
    #         elif resource == 'zal':
    #             self.counter_room_zal -= 1
    #         elif resource == 'forge':
    #             self.counter_room_forge -= 1
    #         # time.sleep(3)
    #     else:
    #         if self.previous_room != resource:
    #             get_pn = self.path_normal(path_room)
    #
    #             self.get_room_list(get_pn)
    #             self.previous_room = resource
    #             time.sleep(5)

    # def kitchen_rooms(self):
    #     """
    #     Ищет координаты картинок для получение рекламы
    #
    #     """
    #     if self.preview_room():
    #         self.click_repetitions += 1
    #     elif self.click_repetitions > self.max_see:
    #         self.KITCHEN_ROOM = False
    #         self.one_click_rk = True
    #         self.click_repetitions = 1
    #     elif self.KITCHEN_ROOM:
    #         path = self.path_normal(self.path_room_kitchen)
    #         time.sleep(1)
    #         self.get_room_list(path)
    #
    #     # print(f'Кухня найденый координат {len(path)}', self.click_repetitions)
    #
    #     # time.sleep(5)
    #
    # def laboratory_room(self):
    #     """
    #     Ищет координаты картинок для получение рекламы
    #     Комната улучшения знаний в лаборатории
    #     """
    #     if self.preview_room():
    #         self.click_repetitions += 1
    #     elif self.click_repetitions > self.max_see:
    #         self.LAB_ROOM = False
    #         self.one_click_rk = True
    #         self.click_repetitions = 1
    #     elif self.LAB_ROOM:
    #         path = self.path_normal(self.path_room_lab)
    #         time.sleep(1)
    #         self.get_room_list(path)
    #
    #     # print(f'Лаборатория найденый координат {len(path)}', self.click_repetitions)
    #
    # def joinery_room(self):
    #     """
    #     Ищет координаты картинок для получение рекламы
    #     Комната улучшения добычи дерева
    #     """
    #     if self.preview_room():
    #         self.click_repetitions += 1
    #     elif self.click_repetitions > self.max_see:
    #         self.SAWMILL_ROOM = False
    #         self.one_click_rk = True
    #         self.click_repetitions = 1
    #     elif self.SAWMILL_ROOM:
    #         path = self.path_normal(self.path_room_sawmill)
    #         time.sleep(1)
    #         self.get_room_list(path)
    #     # print(f'Лесопилка найденый координат {len(path)}', self.click_repetitions)
    #
    # def bank_room(self):
    #     """
    #     Ищет координаты картинок для получение рекламы
    #     Комната улучшения добычи денег
    #     """
    #     if self.preview_room():
    #         self.click_repetitions += 1
    #     elif self.click_repetitions > self.max_see:
    #         self.BANK_ROOM = False
    #         self.one_click_rk = True
    #         self.click_repetitions = 1
    #     elif self.BANK_ROOM:
    #         path = self.path_normal(self.path_room_bank)
    #         time.sleep(1)
    #         self.get_room_list(path)
    #
    #     # print(f'Банк', path, self.click_repetitions)
    #
    # def zal_room(self):
    #     """
    #     Ищет координаты картинок для получение рекламы
    #     Комната по повышению силы
    #     """
    #     if self.preview_room():
    #         self.click_repetitions += 1
    #     elif self.click_repetitions > self.max_see:
    #         self.ZAL_ROOM = False
    #         self.one_click_rk = True
    #         self.click_repetitions = 1
    #     elif self.ZAL_ROOM:
    #         path = self.path_normal(self.path_room_zal)
    #         time.sleep(1)
    #         self.get_room_list(path)
    #     # print(f'Спортзал', path, self.click_repetitions)
    #     # time.sleep(5)
    #
    # def forge_room(self):
    #     """
    #     Ищет координаты картинок для получение рекламы
    #     Комната улучшению добычи металла
    #     """
    #     if self.preview_room():
    #         self.click_repetitions += 1
    #     elif self.click_repetitions > self.max_see:
    #         self.FORGE_ROOM = False
    #         self.one_click_rk = True
    #         self.click_repetitions = 1
    #     elif self.FORGE_ROOM:
    #         path = self.path_normal(self.path_room_forge)
    #         time.sleep(1)
    #         self.get_room_list(path)
    #     # print(f'Кузница найденый координат {len(path)}', self.click_repetitions)
    #
    #     # time.sleep(5)

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
#                 preview.sawmill_room()
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
