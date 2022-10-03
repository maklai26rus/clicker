import time

from run_video import AdClicker
from see import Ui_MainWindow
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import QThread
import sys


class ProgresBar(QThread):

    def __init__(self, mainwindow):
        super().__init__()
        QThread.__init__(self)
        self.action = True
        self.program_operation_switch = False
        self.mainwindow = mainwindow

    def run(self):
        self.watch_ads()

    def watch_ads(self):
        while self.program_operation_switch:
            time.sleep(0.5)
            if self.mainwindow.preview.KITCHEN_ROOM:
                self.mainwindow.preview.kitchen_rooms()
            elif self.mainwindow.preview.LAB_ROOM:
                self.mainwindow.preview.laboratory_room()
            elif self.mainwindow.preview.JOINERY_ROOM:
                self.mainwindow.preview.joinery_room()
            elif self.mainwindow.preview.ZAL_ROOM:
                self.mainwindow.preview.zal_room()
            elif self.mainwindow.preview.BANK_ROOM:
                self.mainwindow.preview.bank_room()
            elif self.mainwindow.preview.FORGE_ROOM:
                self.mainwindow.preview.forge_room()

    def is_checked(self):
        self.mainwindow._set_enabled(self.action)
        self.mainwindow.preview.KITCHEN_ROOM = self.mainwindow.kitchen_room.isChecked()
        self.mainwindow.preview.LAB_ROOM = self.mainwindow.lab_room.isChecked()
        self.mainwindow.preview.BANK_ROOM = self.mainwindow.bank_room.isChecked()
        self.mainwindow.preview.ZAL_ROOM = self.mainwindow.zal_room.isChecked()
        self.mainwindow.preview.JOINERY_ROOM = self.mainwindow.sawmill_room.isChecked()
        self.mainwindow.preview.FORGE_ROOM = self.mainwindow.forge_room.isChecked()


class ActionsSee(Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.preview = AdClicker()
        self.program_operation_switch = False

        self.bar = ProgresBar(mainwindow=self)

    def watch_ads_room(self):
        """Нажатие кнопки для просмотра рекламы в комнатах"""
        self.start_rooms.clicked.connect(self.when_viewing_ads)

    def when_viewing_ads_stop(self):
        self.bar.action = True
        self.bar.program_operation_switch = False
        self.bar.is_checked()

    def when_viewing_ads(self):
        """
        Начала просмотре рекламы
        """
        self.bar.action = False
        self.bar.program_operation_switch = True
        self.bar.start()
        self.bar.is_checked()

    def stop_ads_room(self):
        self.stop_rooms.clicked.connect(self.when_viewing_ads_stop)

    def _set_enabled(self, action):
        self.kitchen_room.setEnabled(action)
        self.lab_room.setEnabled(action)
        self.bank_room.setEnabled(action)
        self.zal_room.setEnabled(action)
        self.sawmill_room.setEnabled(action)
        self.forge_room.setEnabled(action)


def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = ActionsSee()
    ui.setupUi(MainWindow)
    ui.watch_ads_room()
    ui.stop_ads_room()

    MainWindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
