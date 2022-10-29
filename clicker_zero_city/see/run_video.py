import pyautogui
import time
import os


class AdClicker:
    """
    Класс отвечающий за просмотр рекламы

    """

    def __init__(self):
        self.crutch = 0.9

        self.checking_room_kitchen = False
        self.counter_room_kitchen = 2

        self.checking_room_lab = False
        self.counter_room_lab = 2

        self.checking_room_bank = False
        self.counter_room_bank = 2

        self.checking_room_zal = False
        self.counter_room_zal = 2

        self.checking_room_forge = False
        self.counter_room_forge = 2

        self.checking_room_sawmill = False
        self.counter_room_sawmill = 2

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

        self.path_shop = 'png/marketing/shop'
        self.path_global_map = 'png/marketing/global_map'
        # self.path_video_rooms = 'png/marketing/marketing1.PNG'
        self.path_video_type1 = 'png/marketing/type_realm_icon_1'
        self.path_video_type2 = 'png/marketing/type_realm_icon_2'
        self.path_prize = 'png/marketing/prize'

        self.path_room_kitchen = "png/study_rooms/dining_room"
        self.path_room_lab = "png/study_rooms/lab_room"
        self.path_room_bank = "png/study_rooms/bank_room"
        self.path_room_zal = "png/study_rooms/zal_room"
        self.path_room_sawmill = "png/study_rooms/sawmill_room"
        self.path_room_forge = "png/study_rooms/forge_room"

        self.path_tablet = "png/marketing/tablet"
        self.path_movie = "png/marketing/movie"
        self.path_add_res = "png/marketing/add_res"
        self.path_step1 = "png/marketing/step1"
        self.path_step2 = "png/marketing/step2"

        self.path_food = "png/marketing/food"
        self.path_baks = "png/marketing/baks"
        self.path_metal = "png/marketing/metal"
        self.path_vial = "png/marketing/vial"
        self.path_wood = "png/marketing/wood"

        self.path_arena = "png/marketing/arena"
        self.path_terminal = "png/marketing/terminal"
        self.path_bunker = "png/marketing/bunker"
        self.path_tunnel = "png/marketing/tunel"

    def click_global_map(self):
        get_pngm = self.path_normal(self.path_global_map)
        if get_pngm:
            pyautogui.click(get_pngm[0])

    def getting_resources_location(self, path, counter, resource):
        """
        Смотрим рекламу для получение ресурсов
        введения счечика просмотра рекламы
        path = путь к картинке получения ресурса
        counter = счечик. сколько раз просмотреть рекламу
        resource= что за выбраный ресурс

        """
        get_pn = self.path_normal(path)
        if get_pn and counter > 0:
            pyautogui.click(get_pn[0])
            time.sleep(2)

            get_pvt = self.path_normal(self.path_video_type2)
            if get_pvt:
                pyautogui.click(get_pvt[0])
                if resource == 'arena':
                    self.counter_ads_in_arena -= 1
                elif resource == 'terminal':
                    self.counter_ads_in_terminal -= 1
                elif resource == 'bunker':
                    self.counter_ads_in_bunker -= 1
                elif resource == 'tunnel':
                    self.counter_ads_in_tunnel -= 1
        time.sleep(3)

    def exit_location(self):
        get_pns = self.path_normal(self.path_shop)
        if get_pns:
            pyautogui.press('esc')

    def getting_resources(self, path, counter, resource):
        """
        Смотрим рекламу для получение ресурсов
        введения счечика просмотра рекламы
        path = путь к картинке получения ресурса
        counter = счечик. сколько раз просмотреть рекламу
        resource= что за выбраный ресурс

        """
        get_pn = self.path_normal(path)
        if get_pn and counter > 0:
            pyautogui.click(get_pn[0])
            time.sleep(1)

            # get_par = pyautogui.locateOnScreen(self.path_add_res, confidence=0.8)
            get_par = self.path_normal(self.path_add_res)
            if get_par:
                pyautogui.click(get_par[0])
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
            pyautogui.click(center)

    def preview_tablet(self):
        """Предварительный просмотр рекламы"""
        get_vidio = self.path_normal(self.path_video_type2)
        if get_vidio:
            pyautogui.click(get_vidio[0])
            time.sleep(6)

    def definition_prize(self):
        """На планшете после просмотра рекламы нажать забрать приз"""
        click = self.path_normal(self.path_prize)
        if click:
            pyautogui.click(click[0])

    def search_coordinate_ad(self, path_rooms_png):
        """Принимает путь к картинке и ещет координату.
            Если в момент запуска была найдена точка то воозращает координату ее для дальнейшего действия

        return: Возращает найденую координату
        """
        return pyautogui.locateOnScreen(path_rooms_png, confidence=0.7)

    def path_normal(self, path) -> list:
        """Модюль преобразующий в правильный путь для координат"""
        _pn = os.path.normpath(os.path.join(path))
        path_dining_room = [_pn + "\\" + file for file in os.listdir(_pn)]
        path = list(filter(None, map(self.search_coordinate_ad, path_dining_room)))
        return path

    def tablet_search(self):
        """
        Поиск иконки планшет на экране.
        Переходит в него для просмотра рекламы

        """
        get_tablet = self.path_normal(self.path_tablet)
        if get_tablet:
            pyautogui.click(get_tablet[0])
            time.sleep(2)
            get_movie2 = self.path_normal(self.path_step2)
            if get_movie2:
                pyautogui.click(get_movie2[0])

    def cheking_tablet(self):
        """Проверка на рекламу в планшете. если непоявилась кнопка рекламы,  смотреть ее.
        Иначе делает клик по вверхней иконке и назад
         ....
        """
        get_movie = self.path_normal(self.path_movie)
        get_vidio = self.path_normal(self.path_video_type2)
        if get_movie and get_vidio:
            return True
        elif get_movie:
            get_movie1 = self.path_normal(self.path_step1)
            if get_movie1:
                pyautogui.click(get_movie1[0])
            time.sleep(1)
            get_movie2 = self.path_normal(self.path_step2)
            if get_movie2:
                pyautogui.click(get_movie2[0])
            time.sleep(1)

    def ads_rooms(self, counter, path_room, resource):
        """
        Ищет координаты картинок для получение рекламы
        room комната для просмотра рекламы
        counter кол-во раз смотреть рекламу
        path_room путь к деректории с png файлами
        """
        time.sleep(2)
        get_pn = self.path_normal(path_room)
        if get_pn and counter > 0:
            if self.previous_room != resource:
                self.get_room_list(get_pn)
                self.previous_room = resource

            time.sleep(6)  # Пауза после нахождения комнаты. для определения есть ли значек рекламы
            get_pvr = self.path_normal(self.path_video_type1)
            if get_pvr:
                pyautogui.click(get_pvr[0])
                time.sleep(4)  # Пауза на рекламу 4 секунды
                # Кастыль. Иногда при нажатии рекламы, реклама не проигрывает
                # Теперь при просмотре добавится просмотр в комнате лишний.
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
