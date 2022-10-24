# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\see.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Za_City(object):
    def setupUi(self, Za_City):
        Za_City.setObjectName("Za_City")
        Za_City.resize(367, 500)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\1.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Za_City.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Za_City)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 347, 441))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_rooms = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_rooms.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_rooms.setFont(font)
        self.label_rooms.setStyleSheet("")
        self.label_rooms.setTextFormat(QtCore.Qt.PlainText)
        self.label_rooms.setScaledContents(False)
        self.label_rooms.setTextInteractionFlags(QtCore.Qt.TextEditable)
        self.label_rooms.setObjectName("label_rooms")
        self.verticalLayout_3.addWidget(self.label_rooms)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.kitchen_room = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.kitchen_room.setMouseTracking(True)
        self.kitchen_room.setTabletTracking(False)
        self.kitchen_room.setObjectName("kitchen_room")
        self.gridLayout_3.addWidget(self.kitchen_room, 2, 0, 1, 1)
        self.sawmill_room = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.sawmill_room.setObjectName("sawmill_room")
        self.gridLayout_3.addWidget(self.sawmill_room, 3, 0, 1, 1)
        self.btn_kitchen_test = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.btn_kitchen_test.setStyleSheet("")
        self.btn_kitchen_test.setObjectName("btn_kitchen_test")
        self.gridLayout_3.addWidget(self.btn_kitchen_test, 2, 1, 1, 1)
        self.bank_room = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.bank_room.setObjectName("bank_room")
        self.gridLayout_3.addWidget(self.bank_room, 4, 0, 1, 1)
        self.lab_room = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.lab_room.setObjectName("lab_room")
        self.gridLayout_3.addWidget(self.lab_room, 5, 0, 1, 1)
        self.btn_sawmill_test = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.btn_sawmill_test.setObjectName("btn_sawmill_test")
        self.gridLayout_3.addWidget(self.btn_sawmill_test, 3, 1, 1, 1)
        self.forge_room = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.forge_room.setObjectName("forge_room")
        self.gridLayout_3.addWidget(self.forge_room, 6, 0, 1, 1)
        self.zal_room = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.zal_room.setObjectName("zal_room")
        self.gridLayout_3.addWidget(self.zal_room, 7, 0, 1, 1)
        self.btn_lab_test = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.btn_lab_test.setObjectName("btn_lab_test")
        self.gridLayout_3.addWidget(self.btn_lab_test, 5, 1, 1, 1)
        self.btn_bank_test = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.btn_bank_test.setObjectName("btn_bank_test")
        self.gridLayout_3.addWidget(self.btn_bank_test, 4, 1, 1, 1)
        self.btn_zal_test = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.btn_zal_test.setObjectName("btn_zal_test")
        self.gridLayout_3.addWidget(self.btn_zal_test, 7, 1, 1, 1)
        self.btn_forge_test = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.btn_forge_test.setObjectName("btn_forge_test")
        self.gridLayout_3.addWidget(self.btn_forge_test, 6, 1, 1, 1)
        self.btn_start_rooms = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.btn_start_rooms.setStyleSheet("")
        self.btn_start_rooms.setObjectName("btn_start_rooms")
        self.gridLayout_3.addWidget(self.btn_start_rooms, 8, 1, 1, 1)
        self.all_rooms = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.all_rooms.setObjectName("all_rooms")
        self.gridLayout_3.addWidget(self.all_rooms, 8, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_3)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_tablet = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_tablet.setFont(font)
        self.label_tablet.setStyleSheet("")
        self.label_tablet.setObjectName("label_tablet")
        self.gridLayout_2.addWidget(self.label_tablet, 0, 0, 1, 1)
        self.btn_start_tablet = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.btn_start_tablet.setObjectName("btn_start_tablet")
        self.gridLayout_2.addWidget(self.btn_start_tablet, 0, 1, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout_2)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_resources = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_resources.setFont(font)
        self.label_resources.setStyleSheet("")
        self.label_resources.setTextInteractionFlags(QtCore.Qt.TextEditable)
        self.label_resources.setObjectName("label_resources")
        self.verticalLayout_6.addWidget(self.label_resources)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.check_foot = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.check_foot.setObjectName("check_foot")
        self.gridLayout.addWidget(self.check_foot, 2, 1, 1, 1)
        self.check_wood = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.check_wood.setObjectName("check_wood")
        self.gridLayout.addWidget(self.check_wood, 3, 0, 1, 1)
        self.check_reagent = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.check_reagent.setObjectName("check_reagent")
        self.gridLayout.addWidget(self.check_reagent, 2, 0, 1, 1)
        self.check_baks = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.check_baks.setObjectName("check_baks")
        self.gridLayout.addWidget(self.check_baks, 1, 1, 1, 1)
        self.btn_start_resources = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.btn_start_resources.setObjectName("btn_start_resources")
        self.gridLayout.addWidget(self.btn_start_resources, 3, 1, 1, 1)
        self.check_forge = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.check_forge.setObjectName("check_forge")
        self.gridLayout.addWidget(self.check_forge, 1, 0, 1, 1)
        self.verticalLayout_6.addLayout(self.gridLayout)
        self.btn_stop_program = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.btn_stop_program.setObjectName("btn_stop_program")
        self.verticalLayout_6.addWidget(self.btn_stop_program)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.version = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.version.setStyleSheet("")
        self.version.setObjectName("version")
        self.horizontalLayout_5.addWidget(self.version)
        self.version_number = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.version_number.setObjectName("version_number")
        self.horizontalLayout_5.addWidget(self.version_number)
        self.verticalLayout_6.addLayout(self.horizontalLayout_5)
        self.verticalLayout_5.addLayout(self.verticalLayout_6)
        self.verticalLayout_3.addLayout(self.verticalLayout_5)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        Za_City.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Za_City)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 367, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        Za_City.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Za_City)
        self.statusbar.setObjectName("statusbar")
        Za_City.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(Za_City)
        self.action.setObjectName("action")
        self.actionExit = QtWidgets.QAction(Za_City)
        self.actionExit.setObjectName("actionExit")
        self.action_Alt_Z = QtWidgets.QAction(Za_City)
        self.action_Alt_Z.setEnabled(False)
        self.action_Alt_Z.setObjectName("action_Alt_Z")
        self.menu.addAction(self.action)
        self.menu.addSeparator()
        self.menu.addAction(self.actionExit)
        self.menu_2.addAction(self.action_Alt_Z)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(Za_City)
        QtCore.QMetaObject.connectSlotsByName(Za_City)

    def retranslateUi(self, Za_City):
        _translate = QtCore.QCoreApplication.translate
        Za_City.setWindowTitle(_translate("Za_City", "Za_City"))
        self.label_rooms.setToolTip(_translate("Za_City", "<html><head/><body><p><br/></p></body></html>"))
        self.label_rooms.setWhatsThis(_translate("Za_City", "<html><head/><body><p align=\"center\">Просмотреть Рекламу в комнатах</p></body></html>"))
        self.label_rooms.setText(_translate("Za_City", "Просмотреть Рекламу в комнатах"))
        self.kitchen_room.setText(_translate("Za_City", "Кухня"))
        self.sawmill_room.setText(_translate("Za_City", "Лесопилка"))
        self.btn_kitchen_test.setText(_translate("Za_City", "тест кухня"))
        self.bank_room.setText(_translate("Za_City", "Банк"))
        self.lab_room.setText(_translate("Za_City", "Лаборатория"))
        self.btn_sawmill_test.setText(_translate("Za_City", "тест лесопилка"))
        self.forge_room.setText(_translate("Za_City", "Кузница"))
        self.zal_room.setText(_translate("Za_City", "Спорт зал"))
        self.btn_lab_test.setText(_translate("Za_City", "тест лаборатория"))
        self.btn_bank_test.setText(_translate("Za_City", "тест банк"))
        self.btn_zal_test.setText(_translate("Za_City", "тест спорт зал"))
        self.btn_forge_test.setText(_translate("Za_City", "тест кузница"))
        self.btn_start_rooms.setText(_translate("Za_City", "Старт"))
        self.all_rooms.setText(_translate("Za_City", " Все комнаты"))
        self.label_tablet.setText(_translate("Za_City", "<html><head/><body><p>П/Р Планшете</p></body></html>"))
        self.btn_start_tablet.setText(_translate("Za_City", "Старт"))
        self.label_resources.setText(_translate("Za_City", "<html><head/><body><p>П/р Получение ресурсов</p></body></html>"))
        self.check_foot.setText(_translate("Za_City", "Еда"))
        self.check_wood.setText(_translate("Za_City", "Древесина"))
        self.check_reagent.setText(_translate("Za_City", "Реагенты"))
        self.check_baks.setText(_translate("Za_City", "Деньги"))
        self.btn_start_resources.setToolTip(_translate("Za_City", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.btn_start_resources.setWhatsThis(_translate("Za_City", "<html><head/><body><p align=\"justify\"><br/></p></body></html>"))
        self.btn_start_resources.setText(_translate("Za_City", "Старт"))
        self.check_forge.setText(_translate("Za_City", "Железо"))
        self.btn_stop_program.setText(_translate("Za_City", "Остановить Выполнение"))
        self.version.setText(_translate("Za_City", "<html><head/><body><p align=\"right\">Версия:</p></body></html>"))
        self.version_number.setText(_translate("Za_City", "0"))
        self.menu.setTitle(_translate("Za_City", "Меню"))
        self.menu_2.setTitle(_translate("Za_City", "Команды"))
        self.action.setText(_translate("Za_City", "О кликере"))
        self.actionExit.setText(_translate("Za_City", "Exit"))
        self.action_Alt_Z.setText(_translate("Za_City", "Стоп Alt+Z"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Za_City = QtWidgets.QMainWindow()
    ui = Ui_Za_City()
    ui.setupUi(Za_City)
    Za_City.show()
    sys.exit(app.exec_())
