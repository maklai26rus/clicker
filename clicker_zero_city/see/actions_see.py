import time

from clicker_zero_city.see.run_video import AdClicker
from clicker_zero_city.see.see import Ui_Za_City
from clicker_zero_city.wind_menu.info_window import Ui_info

from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import qApp
import sys


class Inspector(QThread):
    """
    Проверящий класс. на нажите клавиши старт и отмены стоп

    Потоковый класс

    """

    def __init__(self, mainwindow):
        super().__init__()
        QThread.__init__(self)
        # Активная или не активная комната
        self.action = True

        # Определят на запуск цикла.
        self.program_operation_switch = False
        self.mainwindow = mainwindow
        self.choosing_action = {"rooms": False, 'tablet': False, 'resourcer': False}

    def shutdown_click(self):
        for k in self.choosing_action.keys():
            self.choosing_action[k] = False

    def run(self):
        self.watch_ads()

    def watch_ads(self):
        """
        Выполняется обработка просмотра рекламы в комнатах
        """
        while self.program_operation_switch:
            time.sleep(0.5)
            if self.choosing_action["rooms"]:

                if self.mainwindow.preview.KITCHEN_ROOM:
                    self.mainwindow.preview.kitchen_rooms()
                    self.mainwindow.btn_changes_color_startup(self.mainwindow.preview.KITCHEN_ROOM,
                                                              self.mainwindow.btn_kitchen_test)
                elif self.mainwindow.preview.LAB_ROOM:
                    self.mainwindow.preview.laboratory_room()
                    self.mainwindow.btn_changes_color_startup(self.mainwindow.preview.LAB_ROOM,
                                                              self.mainwindow.btn_lab_test)
                elif self.mainwindow.preview.SAWMILL_ROOM:
                    self.mainwindow.preview.joinery_room()
                    self.mainwindow.btn_changes_color_startup(self.mainwindow.preview.SAWMILL_ROOM,
                                                              self.mainwindow.btn_sawmill_test)
                elif self.mainwindow.preview.ZAL_ROOM:
                    self.mainwindow.preview.zal_room()
                    self.mainwindow.btn_changes_color_startup(self.mainwindow.preview.ZAL_ROOM,
                                                              self.mainwindow.btn_zal_test)
                elif self.mainwindow.preview.BANK_ROOM:
                    self.mainwindow.preview.bank_room()
                    self.mainwindow.btn_changes_color_startup(self.mainwindow.preview.BANK_ROOM,
                                                              self.mainwindow.btn_bank_test)
                elif self.mainwindow.preview.FORGE_ROOM:
                    self.mainwindow.preview.forge_room()
                    self.mainwindow.btn_changes_color_startup(self.mainwindow.preview.FORGE_ROOM,
                                                              self.mainwindow.btn_forge_test)

            elif self.choosing_action['tablet']:
                self.mainwindow.preview.tablet_search()
                self.mainwindow.preview.cheking_tablet()
                self.mainwindow.preview.preview_tablet()
                self.mainwindow.preview.definition_prize()

            elif self.choosing_action['resourcer']:
                if self.mainwindow.preview.res_food and self.choosing_action['resourcer']:
                    self.mainwindow.preview.get_metal_res(path=self.mainwindow.preview.path_food,
                                                          counter=self.mainwindow.preview.res_food_counter,
                                                          resource="food")

                if self.mainwindow.preview.res_vial and self.choosing_action['resourcer']:
                    self.mainwindow.preview.get_metal_res(path=self.mainwindow.preview.path_vial,
                                                          counter=self.mainwindow.preview.res_vial_counter,
                                                          resource="vial")

                if self.mainwindow.preview.res_wood and self.choosing_action['resourcer']:
                    self.mainwindow.preview.get_metal_res(path=self.mainwindow.preview.path_wood,
                                                          counter=self.mainwindow.preview.res_wood_counter,
                                                          resource="wood")

                if self.mainwindow.preview.res_baks and self.choosing_action['resourcer']:
                    self.mainwindow.preview.get_metal_res(path=self.mainwindow.preview.path_baks,
                                                          counter=self.mainwindow.preview.res_baks_counter,
                                                          resource="baks")

                if self.mainwindow.preview.res_metal and self.choosing_action['resourcer']:
                    self.mainwindow.preview.get_metal_res(path=self.mainwindow.preview.path_metal,
                                                          counter=self.mainwindow.preview.res_metal_counter,
                                                          resource="metal")

    def is_checked_rooms(self):
        """
        self.mainwindow.set_enabled(self.action) определяет возможность выбора комнат
        Дальше передает выбраные комнаты для просмотра рекламмы

        """

        self.mainwindow.set_enabled(self.action)
        self.mainwindow.preview.KITCHEN_ROOM = self.mainwindow.kitchen_room.isChecked()
        self.mainwindow.preview.LAB_ROOM = self.mainwindow.lab_room.isChecked()
        self.mainwindow.preview.BANK_ROOM = self.mainwindow.bank_room.isChecked()
        self.mainwindow.preview.ZAL_ROOM = self.mainwindow.zal_room.isChecked()
        self.mainwindow.preview.SAWMILL_ROOM = self.mainwindow.sawmill_room.isChecked()
        self.mainwindow.preview.FORGE_ROOM = self.mainwindow.forge_room.isChecked()

    def is_checked_resources(self):
        self.mainwindow.set_enabled_resourcer(self.action)
        self.mainwindow.preview.res_food = self.mainwindow.check_foot.isChecked()
        self.mainwindow.preview.res_metal = self.mainwindow.check_forge.isChecked()
        self.mainwindow.preview.res_baks = self.mainwindow.check_baks.isChecked()
        self.mainwindow.preview.res_wood = self.mainwindow.check_wood.isChecked()
        self.mainwindow.preview.res_vial = self.mainwindow.check_reagent.isChecked()


class ActionsSee(Ui_Za_City):
    """
    Запуск простмора рекламы в комнатах/планшете


    Подключается к формам. Вся логика форм прописана в этом классе

    """

    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.window = QtWidgets.QMainWindow()
        self.ui_info = Ui_info()

        self.preview = AdClicker()
        self.program_operation_switch = False

        self.inspector = Inspector(mainwindow=self)

        self.setupUi(self.main_window)
        # MainWindow.setFixedSize(298, 384) при обновлении платформы не забуддь в ручную. поставить setFixedSize
        self.bnt_watch_ads_room()

        self.action.triggered.connect(self.open_window)

        self.btn_tablet_start()

        self.btn_running_stop()

        self.btn_resources()

        self.test_kitchen_room()
        self.test_lab_room()
        self.test_zal_room()
        self.test_bank_room()
        self.test_joinery_room()
        self.test_forge_room()

        self.version_number.setText('0.071022')
        self.actionExit.triggered.connect(qApp.quit)

    def open_window(self):
        """Открывает окно инфо """
        self.ui_info.setupUi(self.window)
        self.window.show()

    def btn_resources(self):
        """
        Кнопка нажатия сбор ресурсво
        """
        self.btn_start_resources.clicked.connect(self.resourcer)

    def resourcer(self):
        """Начала сбора. после нажатия  """
        self.inspector.action = False
        self.inspector.program_operation_switch = True
        self.inspector.choosing_action['resourcer'] = True
        self.inspector.choosing_action['rooms'] = False
        self.inspector.choosing_action['tablet'] = False

        self.inspector.is_checked_resources()
        self.inspector.start()

    def bnt_watch_ads_room(self):
        """Нажатие кнопки для просмотра рекламы в комнатах"""
        self.btn_start_rooms.clicked.connect(self.viewing_ads)

    def viewing_ads_stop(self):
        """Ручная остановка просмотра рекламы"""
        self.inspector.action = True
        self.inspector.program_operation_switch = False
        self.inspector.choosing_action['rooms'] = False
        self.inspector.choosing_action['tablet'] = False
        self.inspector.choosing_action['resourcer'] = False
        self.inspector.is_checked_rooms()
        self.inspector.is_checked_resources()

    def viewing_ads(self):
        """
        Просмотр обявлений (рекламы)
        """
        self.preview.one_click_rk = True
        self.inspector.action = False
        self.inspector.program_operation_switch = True
        self.inspector.choosing_action['tablet'] = False
        self.inspector.choosing_action['rooms'] = True
        self.inspector.choosing_action['resourcer'] = False
        self.inspector.is_checked_rooms()

        self.inspector.start()

    def btn_running_stop(self):
        """Кнопка для остановки просмотра рекламы с планшета"""
        self.btn_stop_program.clicked.connect(self.viewing_ads_stop)

    def btn_tablet_start(self):
        """Кнопка для запуск просмотра рекламы с планшета """
        self.btn_start_tablet.clicked.connect(self.btn_ts)

    def btn_ts(self):
        """Действие выполнения кнопка btn_start_tablet"""
        self.inspector.choosing_action['tablet'] = True
        self.inspector.choosing_action['rooms'] = False
        self.inspector.choosing_action['resourcer'] = False
        self.inspector.program_operation_switch = True

        self.inspector.start()

    def set_enabled(self, action):
        """Переключатель блокирует выбор комнат после нажатие СТАРТ
            Разблакирет после нажатие СТОП
        """
        self.kitchen_room.setEnabled(action)
        self.btn_kitchen_test.setEnabled(action)
        self.lab_room.setEnabled(action)
        self.btn_lab_test.setEnabled(action)
        self.bank_room.setEnabled(action)
        self.btn_bank_test.setEnabled(action)
        self.zal_room.setEnabled(action)
        self.btn_zal_test.setEnabled(action)
        self.sawmill_room.setEnabled(action)
        self.btn_sawmill_test.setEnabled(action)
        self.forge_room.setEnabled(action)
        self.btn_forge_test.setEnabled(action)

    def set_enabled_resourcer(self, action):
        """
        Блокировка чекбокса просмотр рекламы для получение ресурсов
        """
        self.check_wood.setEnabled(action)
        self.check_foot.setEnabled(action)
        self.check_forge.setEnabled(action)
        self.check_baks.setEnabled(action)
        self.check_reagent.setEnabled(action)

    def test_kitchen_room(self):
        """Запуск кнопки на проверка если комната """
        self.btn_kitchen_test.clicked.connect(self.test_kitchen)

    def test_lab_room(self):
        """Запуск кнопки на проверка если комната """
        self.btn_lab_test.clicked.connect(self.test_lab)

    def test_zal_room(self):
        """Запуск кнопки на проверка если комната """
        self.btn_zal_test.clicked.connect(self.test_zal)

    def test_bank_room(self):
        """Запуск кнопки на проверка если комната """
        self.btn_bank_test.clicked.connect(self.test_bank)

    def test_forge_room(self):
        """Запуск кнопки на проверка если комната """
        self.btn_forge_test.clicked.connect(self.test_forge)

    def test_joinery_room(self):
        """Запуск кнопки на проверка если комната """
        self.btn_sawmill_test.clicked.connect(self.test_sawmill)

    def test_kitchen(self):
        """Тест на проверку если комната"""
        path = self.preview.path_normal(self.preview.path_room_kitchen)
        self.preview.one_click_rk = True
        self.go_to_room(path, btn=self.btn_kitchen_test)

    def test_lab(self):
        """Тест на проверку если комната"""
        path = self.preview.path_normal(self.preview.path_room_lab)
        self.preview.one_click_rk = True
        self.go_to_room(path, btn=self.btn_lab_test)

    def btn_changes_color_startup(self, room, btn):
        """
        Если комната активна кнопка становится желтого цвета, иначе зеленного
        """

        if room:
            btn.setStyleSheet(f"background-color : yellow;")
        else:
            btn.setStyleSheet("background-color : green;")

    def go_to_room(self, path, btn):
        """
        Определяет есть ли координата
        Если есть то переходит на нее и окрашивает кнопку в зеленый цвет
        Если же нет то в красный без перехода
        """
        if path:
            self.preview.get_room_list(path)
            btn.setStyleSheet("background-color : green;")
        else:
            btn.setStyleSheet("background-color : red;")

    def test_bank(self):
        """Тест на проверку если комната"""
        path = self.preview.path_normal(self.preview.path_room_bank)
        self.preview.one_click_rk = True
        self.go_to_room(path, btn=self.btn_bank_test)

    def test_zal(self):
        """Тест на проверку если комната"""
        path = self.preview.path_normal(self.preview.path_room_zal)
        self.preview.one_click_rk = True
        self.go_to_room(path, btn=self.btn_zal_test)

    def test_sawmill(self):
        """Тест на проверку если комната"""
        path = self.preview.path_normal(self.preview.path_room_sawmill)
        self.preview.one_click_rk = True
        self.go_to_room(path, btn=self.btn_sawmill_test)

    def test_forge(self):
        """Тест на проверку если комната"""
        path = self.preview.path_normal(self.preview.path_room_forge)
        self.preview.one_click_rk = True
        self.go_to_room(path, btn=self.btn_forge_test)


def main_actions_see():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ActionsSee(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
