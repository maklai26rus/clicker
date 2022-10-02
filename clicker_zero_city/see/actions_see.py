from run_video import AdClicker
from see import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class ActionsSee(Ui_MainWindow):

    def __init__(self):
        self.preview = AdClicker()

    def watch_ads_room(self):
        """Нажатие кнопки для просмотра рекламы в комнатах"""
        self.start_rooms.clicked.connect(self.when_viewing_ads)

    def when_viewing_ads(self):
        """
        Начала просмотре рекламы
        """
        action = False

        self.set_enabled(action)

        self.preview.KITCHEN_ROOM = self.kitchen_room.isChecked()

        self.preview.LAB_ROOM = self.lab_room.isChecked()

        self.preview.BANK_ROOM = self.bank_room.isChecked()

        self.preview.ZAL_ROOM = self.zal_room.isChecked()

        self.preview.JOINERY_ROOM = self.sawmill_room.isChecked()
        self.watch_ads()

    def when_viewing_ads_stop(self):
        action = True
        self.set_enabled(action)

    def stop_ads_room(self):
        self.stop_rooms.clicked.connect(self.when_viewing_ads_stop)

    def set_enabled(self, action):
        self.kitchen_room.setEnabled(action)
        self.lab_room.setEnabled(action)
        self.bank_room.setEnabled(action)
        self.zal_room.setEnabled(action)
        self.sawmill_room.setEnabled(action)
        self.forge_room.setEnabled(action)
        print(self.forge_room.text())

    def watch_ads(self):
        if self.preview.KITCHEN_ROOM:
            self.preview.kitchen_rooms()
        elif self.preview.LAB_ROOM:
            self.preview.laboratory_room()
        elif self.preview.JOINERY_ROOM:
            self.preview.joinery_room()
        elif self.preview.ZAL_ROOM:
            self.preview.zal_room()
        elif self.preview.BANK_ROOM:
            self.preview.bank_room()
        elif self.preview.FORGE_ROOM:
            self.preview.forge_room()
        else:
            self.watch_ads()


def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = ActionsSee()
    ui.setupUi(MainWindow)
    ui.watch_ads_room()
    ui.stop_ads_room()
    # ui.watch_ads()

    MainWindow.show()
    sys.exit(app.exec_())

    # if choosing_action['tablet']:
    #     preview.preview_tablet()
    #     preview.definition_prize()


if __name__ == "__main__":
    main()
    # watch_ads()
