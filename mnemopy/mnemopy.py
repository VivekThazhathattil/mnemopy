import datetime
import random
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtMultimedia import QSound
import sys
from .resources import *
class Ui_main_window(object):
    def setupUi(self, main_window):

        self.running_applet = False
        self.counter = 0
        self.app_no = 0
        self.recall_mode = False

        self.watch_counter = 0
        self.is_watch_reset = True

        self.watch_timer = QtCore.QTimer()
        self.watch_timer.timeout.connect(self.run_watch)
        self.watch_timer.setInterval(100)

        main_window.setObjectName("main_window")
        main_window.resize(739, 446)
        main_window.setStyleSheet("background-color: rgb(18, 18, 18);")
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")
        self.stacked_windows = QtWidgets.QStackedWidget(self.centralwidget)
        self.stacked_windows.setGeometry(QtCore.QRect(0, -20, 731, 441))
        self.stacked_windows.setObjectName("stacked_windows")
        # ========================================================================================
        self.page_main_menu = QtWidgets.QWidget()
        self.page_main_menu.setObjectName("page_main_menu")
        self.app_descr = QtWidgets.QTextBrowser(self.page_main_menu)
        self.app_descr.setGeometry(QtCore.QRect(100, 130, 551, 81))
        self.app_descr.setStyleSheet('font: 20pt "Sans Serif";\n' "")
        self.app_descr.setObjectName("app_descr")
        self.button_fmw = QtWidgets.QPushButton(self.page_main_menu)
        self.button_fmw.setGeometry(QtCore.QRect(430, 240, 201, 23))
        self.button_fmw.setStyleSheet("color: rgb(255, 255, 255);")
        self.button_fmw.setObjectName("button_fmw")
        self.button_fmw.clicked.connect(self.open_window_15min_words)
        self.button_exit = QtWidgets.QPushButton(self.page_main_menu)
        self.button_exit.setGeometry(QtCore.QRect(340, 400, 80, 23))
        self.button_exit.setStyleSheet("color: rgb(255, 255, 255);")
        self.button_exit.setObjectName("button_exit")
        self.button_exit.clicked.connect(self.exit_the_app)
        self.speed_cards_button = QtWidgets.QPushButton(self.page_main_menu)
        self.speed_cards_button.setGeometry(QtCore.QRect(140, 240, 91, 23))
        self.speed_cards_button.setStyleSheet("color: rgb(255, 255, 255);")
        self.speed_cards_button.setObjectName("speed_cards_button")
        self.speed_cards_button.clicked.connect(self.open_window_speed_cards)
        self.app_title = QtWidgets.QLabel(self.page_main_menu)
        self.app_title.setGeometry(QtCore.QRect(200, 60, 331, 71))
        self.app_title.setStyleSheet(
            'font: 30pt "Sans Serif";\n' "color: rgb(255, 56, 56)"
        )
        self.app_title.setObjectName("app_title")
        self.button_fmn = QtWidgets.QPushButton(self.page_main_menu)
        self.button_fmn.setGeometry(QtCore.QRect(260, 240, 141, 23))
        self.button_fmn.setStyleSheet("color: rgb(255, 255, 255);")
        self.button_fmn.setObjectName("button_fmn")
        self.button_fmn.clicked.connect(self.open_window_5min_nums)
        self.button_sn = QtWidgets.QPushButton(self.page_main_menu)
        self.button_sn.setGeometry(QtCore.QRect(140, 290, 121, 23))
        self.button_sn.setStyleSheet("color: rgb(255, 255, 255);")
        self.button_sn.setObjectName("button_sn")
        self.button_sn.clicked.connect(self.open_window_sn)
        self.button_bn = QtWidgets.QPushButton(self.page_main_menu)
        self.button_bn.setGeometry(QtCore.QRect(280, 290, 121, 23))
        self.button_bn.setStyleSheet("color: rgb(255, 255, 255);")
        self.button_bn.setObjectName("button_bn")
        self.button_bn.clicked.connect(self.open_window_bn)
        self.heart_img = QtWidgets.QLabel(self.page_main_menu)
        self.heart_img.setGeometry(QtCore.QRect(560, 70, 41, 41))
        self.heart_img.setText("")
        self.heart_img.setPixmap(QtGui.QPixmap(":/dat/img/love.png"))
        self.heart_img.setScaledContents(True)
        self.heart_img.setObjectName("heart_img")
        self.stacked_windows.addWidget(self.page_main_menu)

        # _______________________ SPEED CARDS____________________________

        self.page_sc = QtWidgets.QWidget()
        self.page_sc.setObjectName("page_sc")
        self.time_delay_label = QtWidgets.QLabel(self.page_sc)
        self.time_delay_label.setGeometry(QtCore.QRect(30, 60, 121, 16))
        self.time_delay_label.setStyleSheet("color:rgb(255, 255, 255)")
        self.time_delay_label.setObjectName("time_delay_label")
        self.time_delay_label.setVisible(True)
        self.begin_sc = QtWidgets.QPushButton(self.page_sc)
        self.begin_sc.setGeometry(QtCore.QRect(30, 100, 80, 23))
        self.begin_sc.setStyleSheet("color: rgb(255, 255, 255);")
        self.begin_sc.setObjectName("begin_sc")
        self.begin_sc.clicked.connect(self.applet_sc)
        self.begin_sc.setVisible(True)
        self.pause_sc = QtWidgets.QPushButton(self.page_sc)
        self.pause_sc.setGeometry(QtCore.QRect(130, 100, 80, 23))
        self.pause_sc.setStyleSheet("color: rgb(255, 255, 255);")
        self.pause_sc.setObjectName("pause_sc")
        self.pause_sc.setVisible(False)
        self.pause_sc.clicked.connect(self.pause_action)
        self.hide_timer_sc = QtWidgets.QCheckBox(self.page_sc)
        self.hide_timer_sc.setGeometry(QtCore.QRect(230, 100, 82, 23))
        self.hide_timer_sc.setStyleSheet("color: rgb(255, 255, 255);")
        self.hide_timer_sc.setObjectName("hide_timer_sc")
        self.hide_timer_sc.clicked.connect(self.hide_timer)
        self.hide_timer_sc.setVisible(True)
        self.recall_sc = QtWidgets.QPushButton(self.page_sc)
        self.recall_sc.setGeometry(QtCore.QRect(330, 100, 80, 23))
        self.recall_sc.setStyleSheet("color: rgb(255, 255, 255);")
        self.recall_sc.setObjectName("recall_sc")
        self.recall_sc.setVisible(False)
        self.recall_sc.clicked.connect(self.recall_sc_fn)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.page_sc)
        self.doubleSpinBox.setGeometry(QtCore.QRect(160, 60, 61, 24))
        self.doubleSpinBox.setStyleSheet("background-color: rgb(102, 102, 102);")
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.doubleSpinBox.setMinimum(0)
        self.doubleSpinBox.setDecimals(2)
        self.doubleSpinBox.setVisible(True)
        self.next_sc = QtWidgets.QPushButton(self.page_sc)
        self.next_sc.setGeometry(QtCore.QRect(590, 280, 80, 23))
        self.next_sc.setStyleSheet("color: rgb(255, 255, 255);")
        self.next_sc.clicked.connect(self.manual_next)
        self.next_sc.setObjectName("next_sc")
        self.next_sc.setVisible(False)
        self.prev_sc = QtWidgets.QPushButton(self.page_sc)
        self.prev_sc.setGeometry(QtCore.QRect(590, 320, 80, 23))
        self.prev_sc.setStyleSheet("color: rgb(255, 255, 255);")
        self.prev_sc.setObjectName("prev_sc")
        self.prev_sc.clicked.connect(self.manual_prev)
        self.prev_sc.setVisible(False)
        self.button_quit = QtWidgets.QPushButton(self.page_sc)
        self.button_quit.setGeometry(QtCore.QRect(430, 100, 141, 23))
        self.button_quit.setStyleSheet("color: rgb(255, 255, 255);")
        self.button_quit.setObjectName("button_quit")
        self.button_quit.clicked.connect(self.return_to_main_menu)
        self.exit_sc = QtWidgets.QPushButton(self.page_sc)
        self.exit_sc.setGeometry(QtCore.QRect(590, 100, 80, 23))
        self.exit_sc.setStyleSheet("color: rgb(255, 255, 255);")
        self.exit_sc.setObjectName("exit_sc")
        self.exit_sc.clicked.connect(self.exit_the_app)
        self.card_image = QtWidgets.QLabel(self.page_sc)
        self.card_image.setGeometry(QtCore.QRect(270, 150, 181, 261))
        self.card_image.setText("")
        pixmap = QtGui.QPixmap(":/dat/sc/back.png")
        self.card_image.setPixmap(pixmap.scaled(150, 300, QtCore.Qt.KeepAspectRatio))
        self.lcdNumber = QtWidgets.QLCDNumber(self.page_sc)
        self.lcdNumber.setGeometry(QtCore.QRect(590, 160, 111, 31))
        self.lcdNumber.setObjectName("lcdNumber")
        self.checkBox = QtWidgets.QCheckBox(self.page_sc)
        self.checkBox.setGeometry(QtCore.QRect(590, 210, 85, 21))
        self.checkBox.setStyleSheet("color: rgb(255, 255, 255);")
        self.checkBox.setObjectName("checkBox")
        self.checkBox.stateChanged.connect(self.manual_mode)
        self.card_no_sc = QtWidgets.QLabel(self.page_sc)
        self.card_no_sc.setGeometry(QtCore.QRect(530, 300, 41, 20))
        self.card_no_sc.setStyleSheet("color:rgb(255, 255, 255)")
        self.card_no_sc.setObjectName("card_no_sc")
        self.stacked_windows.addWidget(self.page_sc)

        # ___________________5 MINUTE NUMBERS___________________________

        self.page_fmn = QtWidgets.QWidget()
        self.page_fmn.setObjectName("page_fmn")
        # quit button
        self.quit_fmn = QtWidgets.QPushButton(self.page_fmn)
        self.quit_fmn.setGeometry(QtCore.QRect(210, 50, 131, 23))
        self.quit_fmn.setStyleSheet("color: rgb(255, 255, 255);")
        self.quit_fmn.setObjectName("quit_fmn")
        self.quit_fmn.clicked.connect(self.return_to_main_menu)
        # begin button
        self.begin_fmn = QtWidgets.QPushButton(self.page_fmn)
        self.begin_fmn.setGeometry(QtCore.QRect(30, 50, 80, 23))
        self.begin_fmn.setStyleSheet("color: rgb(255, 255, 255);")
        self.begin_fmn.setObjectName("begin_fmn")
        self.begin_fmn.clicked.connect(self.applet_fmn)
        # exit button
        self.exit_fmn = QtWidgets.QPushButton(self.page_fmn)
        self.exit_fmn.setGeometry(QtCore.QRect(350, 50, 80, 23))
        self.exit_fmn.setStyleSheet("color: rgb(255, 255, 255);")
        self.exit_fmn.setObjectName("exit_fmn")
        self.exit_fmn.clicked.connect(self.exit_the_app)
        # prev button
        self.prev_fmn = QtWidgets.QPushButton(self.page_fmn)
        self.prev_fmn.setGeometry(QtCore.QRect(230, 380, 80, 23))
        self.prev_fmn.setStyleSheet("color: rgb(255, 255, 255);")
        self.prev_fmn.setVisible(False)
        self.prev_fmn.setObjectName("prev_fmn")
        self.prev_fmn.clicked.connect(self.click_prev)
        # next button
        self.next_fmn = QtWidgets.QPushButton(self.page_fmn)
        self.next_fmn.setGeometry(QtCore.QRect(380, 380, 80, 23))
        self.next_fmn.setStyleSheet("color: rgb(255, 255, 255);")
        self.next_fmn.setVisible(False)
        self.next_fmn.setObjectName("next_fmn")
        self.next_fmn.clicked.connect(self.click_next)
        # recall button
        self.recall_fmn = QtWidgets.QPushButton(self.page_fmn)
        self.recall_fmn.setGeometry(QtCore.QRect(120, 50, 80, 23))
        self.recall_fmn.setStyleSheet("color: rgb(255, 255, 255);")
        self.recall_fmn.setObjectName("recall_fmn")
        self.recall_fmn.setVisible(False)
        self.recall_fmn.clicked.connect(self.recall_fmn_fn)
        # lcd watch
        self.timer_fmn = QtWidgets.QLCDNumber(self.page_fmn)
        self.timer_fmn.setGeometry(QtCore.QRect(563, 32, 131, 41))
        self.timer_fmn.setObjectName("timer_fmn")
        # number display panel
        self.disp_panel_fmn = QtWidgets.QTextBrowser(self.page_fmn)
        self.disp_panel_fmn.setGeometry(QtCore.QRect(90, 100, 511, 251))
        self.disp_panel_fmn.setObjectName("disp_panel_fmn")
        self.disp_panel_fmn.setStyleSheet(
            'font: 13.5pt "Sans Serif";\n' "color: rgb(255, 255, 255);"
        )
        # page no label
        self.page_no_fmn = QtWidgets.QLabel(self.page_fmn)
        self.page_no_fmn.setGeometry(QtCore.QRect(327, 380, 34, 21))
        self.page_no_fmn.setObjectName("page_no_fmn")
        self.page_no_fmn.setStyleSheet("color: rgb(255, 255, 255);")
        # hide clock checkbox
        self.hide_timer_fmn = QtWidgets.QCheckBox(self.page_fmn)
        self.hide_timer_fmn.setGeometry(QtCore.QRect(620, 90, 85, 21))
        self.hide_timer_fmn.setStyleSheet("color: rgb(255, 255, 255);")
        self.hide_timer_fmn.setObjectName("hide_timer_fmn")
        self.hide_timer_fmn.stateChanged.connect(self.hide_timer)

        # show next digit in recall
        self.show_next_digit_fmn = QtWidgets.QPushButton(self.page_fmn)
        self.show_next_digit_fmn.setGeometry(QtCore.QRect(660, 160, 31, 31))
        self.show_next_digit_fmn.setStyleSheet("color: rgb(255, 255, 255);")
        self.show_next_digit_fmn.setObjectName("show_next_digit")
        self.show_next_digit_fmn.setVisible(False)
        self.show_next_digit_fmn.clicked.connect(self.show_next_digit_fmn_fn)

        self.stacked_windows.addWidget(self.page_fmn)

        # ___________________15 MINUTE RANDOM WORDS______________________

        self.page_fmw = QtWidgets.QWidget()
        self.page_fmw.setObjectName("page_fmw")
        self.begin_fmw = QtWidgets.QPushButton(self.page_fmw)
        self.begin_fmw.setGeometry(QtCore.QRect(30, 50, 80, 23))
        self.begin_fmw.setStyleSheet("color: rgb(255, 255, 255);")
        self.begin_fmw.setObjectName("begin_fmw")
        self.begin_fmw.setVisible(True)
        self.begin_fmw.clicked.connect(self.applet_fmw)
        self.recall_fmw = QtWidgets.QPushButton(self.page_fmw)
        self.recall_fmw.setGeometry(QtCore.QRect(130, 50, 80, 23))
        self.recall_fmw.setStyleSheet("color: rgb(255, 255, 255);")
        self.recall_fmw.setObjectName("recall_fmw")
        self.recall_fmw.setVisible(False)
        self.recall_fmw.clicked.connect(self.recall_fmw_fn)
        self.quit_fmw = QtWidgets.QPushButton(self.page_fmw)
        self.quit_fmw.setGeometry(QtCore.QRect(230, 50, 131, 23))
        self.quit_fmw.setStyleSheet("color: rgb(255, 255, 255);")
        self.quit_fmw.setObjectName("quit_fmw")
        self.quit_fmw.clicked.connect(self.return_to_main_menu)
        self.exit_fmw = QtWidgets.QPushButton(self.page_fmw)
        self.exit_fmw.setGeometry(QtCore.QRect(380, 50, 80, 23))
        self.exit_fmw.setStyleSheet("color: rgb(255, 255, 255);")
        self.exit_fmw.setObjectName("exit_fmw")
        self.exit_fmw.clicked.connect(self.exit_the_app)
        self.timer_fmw = QtWidgets.QLCDNumber(self.page_fmw)
        self.timer_fmw.setGeometry(QtCore.QRect(620, 40, 84, 33))
        self.timer_fmw.setObjectName("timer_fmw")
        self.hide_timer_fmw = QtWidgets.QCheckBox(self.page_fmw)
        self.hide_timer_fmw.setGeometry(QtCore.QRect(510, 50, 85, 21))
        self.hide_timer_fmw.setStyleSheet("color: rgb(255, 255, 255);")
        self.hide_timer_fmw.setObjectName("hide_timer_fmw")
        self.hide_timer_fmw.clicked.connect(self.hide_timer)
        self.hide_timer_fmw.setVisible(True)
        self.table_fmw = QtWidgets.QTableView(self.page_fmw)
        self.table_fmw.setGeometry(QtCore.QRect(110, 90, 566, 331))
        self.table_fmw.setStyleSheet(
            "color: rgb(255, 255, 255);\n" "gridline-color: rgb(255, 255, 255);"
        )
        self.table_fmw.setObjectName("table_fmw")
        self.table_fmw.setShowGrid(True)
        self.table_fmw.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.model = QtGui.QStandardItemModel()  # SELECTING THE MODEL
        self.table_fmw.setModel(self.model)  # SETTING THE MODEL
        self.stacked_windows.addWidget(self.page_fmw)

        # ________________ SPOKEN NUMBERS____________________________

        self.page_sn = QtWidgets.QWidget()
        self.page_sn.setObjectName("page_sn")
        self.begin_sn = QtWidgets.QPushButton(self.page_sn)
        self.begin_sn.setGeometry(QtCore.QRect(30, 40, 80, 23))
        self.begin_sn.setStyleSheet("color: rgb(255, 255, 255);")
        self.begin_sn.setObjectName("begin_sn")
        self.begin_sn.clicked.connect(self.applet_sn)
        self.recall_sn = QtWidgets.QPushButton(self.page_sn)
        self.recall_sn.setGeometry(QtCore.QRect(130, 40, 80, 23))
        self.recall_sn.setStyleSheet("color: rgb(255, 255, 255);")
        self.recall_sn.setObjectName("recall_sn")
        self.recall_sn.setVisible(False)
        self.recall_sn.clicked.connect(self.recall_sn_fn)
        self.quit_sn = QtWidgets.QPushButton(self.page_sn)
        self.quit_sn.setGeometry(QtCore.QRect(440, 400, 151, 23))
        self.quit_sn.setStyleSheet("color: rgb(255, 255, 255);")
        self.quit_sn.setObjectName("quit_sn")
        self.quit_sn.clicked.connect(self.return_to_main_menu)
        self.exit_sn = QtWidgets.QPushButton(self.page_sn)
        self.exit_sn.setGeometry(QtCore.QRect(620, 400, 80, 23))
        self.exit_sn.setStyleSheet("color: rgb(255, 255, 255);")
        self.exit_sn.setObjectName("exit_sn")
        self.exit_sn.clicked.connect(self.exit_the_app)
        self.timer_sn = QtWidgets.QLCDNumber(self.page_sn)
        self.timer_sn.setGeometry(QtCore.QRect(550, 30, 151, 31))
        self.timer_sn.setObjectName("timer_sn")
        self.hide_timer_sn = QtWidgets.QCheckBox(self.page_sn)
        self.hide_timer_sn.setGeometry(QtCore.QRect(610, 80, 85, 21))
        self.hide_timer_sn.setStyleSheet("color: rgb(255, 255, 255);")
        self.hide_timer_sn.setObjectName("hide_timer_sn")
        self.hide_timer_sn.stateChanged.connect(self.hide_timer)
        self.num_disp_sn = QtWidgets.QTextBrowser(self.page_sn)
        self.num_disp_sn.setGeometry(QtCore.QRect(30, 80, 181, 331))
        self.num_disp_sn.setObjectName("num_disp_sn")
        self.num_disp_sn.setVisible(False)
        self.num_disp_sn.setStyleSheet(
            'font: 13.5pt "Sans Serif";\n color: rgb(255, 255, 255);'
        )
        self.speaker_icon_sn = QtWidgets.QLabel(self.page_sn)
        self.speaker_icon_sn.setGeometry(QtCore.QRect(350, 120, 161, 141))
        self.speaker_icon_sn.setText("")
        self.speaker_icon_sn.setObjectName("speaker_icon_label")
        pixmap = QtGui.QPixmap(":/dat/img/speaker_icon.png")
        self.speaker_icon_sn.setPixmap(
            pixmap.scaled(150, 300, QtCore.Qt.KeepAspectRatio)
        )
        self.speaker_icon_sn.setVisible(False)
        self.stacked_windows.addWidget(self.page_sn)

        # ___________________BINARY NUMBERS _________________________

        self.page_bn = QtWidgets.QWidget()
        self.page_bn.setObjectName("page_bn")
        self.prev_bn = QtWidgets.QPushButton(self.page_bn)
        self.prev_bn.setGeometry(QtCore.QRect(237, 388, 80, 23))
        self.prev_bn.setStyleSheet("color: rgb(255, 255, 255);")
        self.prev_bn.setObjectName("prev_bn")
        self.prev_bn.setDisabled(True)
        self.prev_bn.setVisible(False)
        self.prev_bn.clicked.connect(self.click_prev_bn)
        self.quit_bn = QtWidgets.QPushButton(self.page_bn)
        self.quit_bn.setGeometry(QtCore.QRect(217, 58, 131, 23))
        self.quit_bn.setStyleSheet("color: rgb(255, 255, 255);")
        self.quit_bn.setObjectName("quit_bn")
        self.quit_bn.clicked.connect(self.return_to_main_menu)
        self.checkbox_bn = QtWidgets.QCheckBox(self.page_bn)
        self.checkbox_bn.setGeometry(QtCore.QRect(627, 98, 85, 21))
        self.checkbox_bn.setStyleSheet("color: rgb(255, 255, 255);")
        self.checkbox_bn.setObjectName("checkbox_bn")
        self.checkbox_bn.stateChanged.connect(self.hide_timer)
        self.begin_bn = QtWidgets.QPushButton(self.page_bn)
        self.begin_bn.setGeometry(QtCore.QRect(37, 58, 80, 23))
        self.begin_bn.setStyleSheet("color: rgb(255, 255, 255);")
        self.begin_bn.setObjectName("begin_bn")
        self.begin_bn.clicked.connect(self.applet_bn)
        self.page_no_bn = QtWidgets.QLabel(self.page_bn)
        self.page_no_bn.setGeometry(QtCore.QRect(337, 388, 34, 21))
        self.page_no_bn.setObjectName("page_no_bn")
        self.page_no_bn.setStyleSheet("color: rgb(255, 255, 255);")
        self.disp_panel_bn = QtWidgets.QTextBrowser(self.page_bn)
        self.disp_panel_bn.setGeometry(QtCore.QRect(97, 108, 511, 251))
        self.disp_panel_bn.setObjectName("disp_panel_bn")
        self.disp_panel_bn.setStyleSheet(
            'font: 13.5pt "Sans Serif";\n' "color: rgb(255, 255, 255);"
        )
        self.button_exit_bn = QtWidgets.QPushButton(self.page_bn)
        self.button_exit_bn.setGeometry(QtCore.QRect(357, 58, 80, 23))
        self.button_exit_bn.setStyleSheet("color: rgb(255, 255, 255);")
        self.button_exit_bn.setObjectName("button_exit_bn")
        self.button_exit_bn.clicked.connect(self.exit_the_app)
        self.recall_bn = QtWidgets.QPushButton(self.page_bn)
        self.recall_bn.setGeometry(QtCore.QRect(127, 58, 80, 23))
        self.recall_bn.setStyleSheet("color: rgb(255, 255, 255);")
        self.recall_bn.setObjectName("recall_bn")
        self.recall_bn.setVisible(False)
        self.recall_bn.clicked.connect(self.recall_bn_fn)
        self.next_bn = QtWidgets.QPushButton(self.page_bn)
        self.next_bn.setGeometry(QtCore.QRect(387, 388, 80, 23))
        self.next_bn.setStyleSheet("color: rgb(255, 255, 255);")
        self.next_bn.setObjectName("next_bn")
        self.next_bn.setDisabled(True)
        self.next_bn.setVisible(False)
        self.next_bn.clicked.connect(self.click_next_bn)
        self.timer_bn = QtWidgets.QLCDNumber(self.page_bn)
        self.timer_bn.setGeometry(QtCore.QRect(570, 40, 131, 41))
        self.timer_bn.setObjectName("timer_bn")
        self.show_next_digit_bn = QtWidgets.QPushButton(self.page_bn)
        self.show_next_digit_bn.setGeometry(QtCore.QRect(660, 160, 31, 31))
        self.show_next_digit_bn.setStyleSheet("color: rgb(255, 255, 255);")
        self.show_next_digit_bn.setObjectName("show_next_digit")
        self.show_next_digit_bn.setVisible(False)
        self.show_next_digit_bn.clicked.connect(self.show_next_digit_bn_fn)
        self.stacked_windows.addWidget(self.page_bn)

        # ========================================================================================

        main_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 739, 20))
        self.menubar.setObjectName("menubar")
        main_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(main_window)
        self.statusbar.setObjectName("statusbar")
        main_window.setStatusBar(self.statusbar)

        self.retranslateUi(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    # ========================================================================================

    def pause_action(self):
        if self.running_applet == True:
            print("Pausing the applet")
            if self.app_no == 1:
                self.pause_sc.setText(self._translate("main_window", "unpause"))
            self.running_applet = not self.running_applet
        else:
            print("Unpausing the applet")
            if self.app_no == 1:
                self.pause_sc.setText(self._translate("main_window", "pause"))
            self.running_applet = not self.running_applet
            self.start_watch()
            if self.app_no == 1:
                self.update_image()

    def exit_the_app(self):
        print("Exiting the application")
        exit()

    def open_window_speed_cards(self):
        print("speed_cards")
        self.stacked_windows.setCurrentIndex(1)

    def open_window_5min_nums(self):
        print("5min")
        self.stacked_windows.setCurrentIndex(2)

    def open_window_15min_words(self):
        print("15min")
        self.stacked_windows.setCurrentIndex(3)

    def open_window_sn(self):
        print("spoken numbers")
        self.stacked_windows.setCurrentIndex(4)

    def open_window_bn(self):
        print("spoken_numbers")
        self.stacked_windows.setCurrentIndex(5)

    def return_to_main_menu(self):
        self.watch_reset()
        self.recall_mode = False
        self.counter = 0
        if self.app_no == 1:
            pixmap = QtGui.QPixmap(":/dat/sc/back.png")
            self.card_image.setPixmap(
                pixmap.scaled(150, 300, QtCore.Qt.KeepAspectRatio)
            )
        if self.app_no == 2:
            self.disp_panel_fmn.setPlainText(self._translate("main_window", ""))
            self.page_no_fmn.setText(
                self._translate("main_window", "{}/50".format(self.counter + 1))
            )
            self.next_fmn.setDisabled(True)
            self.prev_fmn.setDisabled(True)
            self.begin_fmn.setText(self._translate("main_window", "begin"))
            self.show_next_digit_fmn.setVisible(False)
        if self.app_no == 3:
            self.table_fmw.setVisible(False)
            self.recall_fmw.setVisible(False)
            self.begin_fmw.setText(self._translate("main_window", "begin"))
        if self.app_no == 4:
            self.speaker_icon_sn.setVisible(False)
            self.num_disp_sn.setVisible(False)
            self.recall_sn.setVisible(False)
        if self.app_no == 5:
            self.disp_panel_bn.setPlainText(self._translate("main_window", ""))
            self.page_no_bn.setText(
                self._translate("main_window", "{}/50".format(self.counter + 1))
            )
            self.next_bn.setDisabled(True)
            self.prev_bn.setDisabled(True)
            self.begin_bn.setText(self._translate("main_window", "begin"))
            self.show_next_digit_bn.setVisible(False)

        self.app_no = 0
        self.running_applet = False
        print("returning to the main menu")
        self.stacked_windows.setCurrentIndex(0)

    def update_image(self):
        if self.counter < 52:
            print("counter = " + str(self.counter))
            pic_temp = str(self.images[self.counter])
            pixmap = QtGui.QPixmap(pic_temp)
            print(str(self.images[self.counter]))
            self.card_image.setPixmap(
                pixmap.scaled(150, 300, QtCore.Qt.KeepAspectRatio)
            )
            self.card_image.setObjectName("card_image")
            self.counter += 1
            self.card_no_sc.setText(
                self._translate("main_window", "{}/52".format(str(self.counter)))
            )
            if not self.checkBox.isChecked() and self.running_applet:
                QtCore.QTimer.singleShot(self.time_step * 1000, self.update_image)

    #        elif self.running_applet == False:
    #            self.counter += 1
    #            update_image(self)

    #                self.running_applet = False
    #                self.stop_watch()
    #                self.begin_sc.setText(self._translate("main_window","begin"))
    #                self.pause_sc.setVisible(False)
    #                self.counter = 0

    def applet_sc(self):
        self.app_no = 1
        self.time_step = self.doubleSpinBox.value()
        if (
            self.running_applet == False
        ):  # clicked when 'begin' visible, applet not running
            self.begin_sc.setText(self._translate("main_window", "stop"))
            self.pause_sc.setVisible(True)
            self.time_delay_label.setVisible(True)
            self.doubleSpinBox.setVisible(True)
            self.start_watch()
            self.recall_sc.setVisible(False)
            ranks = [str(n) for n in range(2, 11)] + list("JQKA")
            suits = ["S", "D", "C", "H"]
            Deck = [rank + suit for suit in suits for rank in ranks]

            Cards = random.sample(Deck, 52)
            self.images = []
            img_path = ":/dat/sc/"

            for i in range(52):
                img_name = Cards[i] + ".png"
                full_img_loc = img_path + img_name
                self.images = self.images + [full_img_loc]

            self.counter = 0
            self.running_applet = True
            self.update_image()
        else:  # clicked when 'stop' visible, applet running
            self.begin_sc.setText(self._translate("main_window", "begin"))
            self.pause_sc.setVisible(False)
            self.stop_watch()
            self.recall_sc.setVisible(True)
            self.running_applet = False

    def recall_sc_fn(self):
        print("speedcards recall")
        self.counter = 0
        pixmap = QtGui.QPixmap(":/dat/sc/back.png")
        self.card_image.setPixmap(pixmap.scaled(150, 300, QtCore.Qt.KeepAspectRatio))
        self.card_no_sc.setText(self._translate("main_window", "--/52"))
        self.recall_sc.setVisible(False)
        self.time_delay_label.setVisible(False)
        self.doubleSpinBox.setVisible(False)
        self.next_sc.setVisible(True)
        self.prev_sc.setVisible(True)
        self.begin_sc.setText(self._translate("main_window", "begin"))
        self.watch_reset()
        self.checkBox.setChecked(True)

    def showLCD(self):
        text = (str(datetime.timedelta(milliseconds=self.watch_counter)) + ".000")[:+9]
        if self.app_no == 1:
            self.lcdNumber.setDigitCount(11)
            if not self.is_watch_reset:  # if "is_watch_reset" is False
                self.lcdNumber.display(text)
            else:
                self.lcdNumber.display("0:00:00.000")
        if self.app_no == 2:
            self.timer_fmn.setDigitCount(11)
            if not self.is_watch_reset:  # if "is_watch_reset" is False
                self.timer_fmn.display(text)
            else:
                self.timer_fmn.display("0:00:00.000")
        if self.app_no == 3:
            self.timer_fmw.setDigitCount(11)
            if not self.is_watch_reset:  # if "is_watch_reset" is False
                self.timer_fmw.display(text)
            else:
                self.timer_fmw.display("0:00:00.000")
        if self.app_no == 4:
            self.timer_sn.setDigitCount(11)
            if not self.is_watch_reset:  # if "is_watch_reset" is False
                self.timer_sn.display(text)
            else:
                self.timer_sn.display("0:00:00.000")

        if self.app_no == 5:
            self.timer_bn.setDigitCount(11)
            if not self.is_watch_reset:  # if "is_watch_reset" is False
                self.timer_bn.display(text)
            else:
                self.timer_bn.display("0:00:00.000")

    def run_watch(self):
        self.watch_counter += 100
        self.showLCD()

    def start_watch(self):
        print("started timer")
        self.watch_timer.start()
        self.is_watch_reset = False

    def stop_watch(self):
        self.watch_timer.stop()
        self.watch_counter = 0

    def watch_reset(self):
        self.watch_timer.stop()
        self.watch_counter = 0
        self.is_watch_reset = True
        self.showLCD()

    def display_num_matrix(self):
        self.matr2str = "\n".join(
            "    ".join("%d" % x for x in y) for y in self.num_matrix[self.counter]
        )
        self.disp_panel_fmn.setPlainText(self._translate("main_window", self.matr2str))

    def show_next_digit_fmn_fn(self):
        self.x_count += 1
        if(self.x_count*self.y_count > 150):
            self.click_next()
        if(self.x_count == 16): # dont hardcode this!
            self.x_count = 1
            self.y_count += 1
            self.recall_str += "\n   "
        else:
            self.recall_str += "   "
        self.recall_str += str(self.num_matrix[self.counter][self.y_count-1][self.x_count-1])
        self.disp_panel_fmn.setPlainText(self._translate("main_window", self.recall_str))

    def click_next(self):
        if self.counter >= 49:
            self.next_fmn.setDisabled(True)
            self.prev_fmn.setDisabled(False)
        else:
            self.next_fmn.setDisabled(False)
            self.prev_fmn.setDisabled(False)
            self.counter += 1
            self.page_no_fmn.setText(
                self._translate("main_window", "{}/50".format(self.counter + 1))
            )
            if self.recall_mode:
                self.x_count = 0
                self.y_count = 1
                self.recall_str = ""
                self.disp_panel_fmn.setPlainText(self._translate("main_window", self.recall_str))
            else:
                self.display_num_matrix()

    def click_prev(self):
        if self.counter <= 0:
            self.prev_fmn.setDisabled(True)
            self.next_fmn.setDisabled(False)
        else:
            self.prev_fmn.setDisabled(False)
            self.next_fmn.setDisabled(False)
            self.counter -= 1
            self.page_no_fmn.setText(
                self._translate("main_window", "{}/50".format(self.counter + 1))
            )
            if self.recall_mode:
                self.x_count = 0
                self.y_count = 1
                self.recall_str = ""
                self.disp_panel_fmn.setPlainText(self._translate("main_window", self.recall_str))
            else:
                self.display_num_matrix()

    def recall_fmn_fn(self):
        self.watch_reset()
        self.counter = 0
        self.recall_mode = True
        self.recall_str = ""
        self.x_count = 0
        self.y_count = 1
        self.recall_fmn.setVisible(False)
        self.disp_panel_fmn.setVisible(True)
        self.disp_panel_fmn.setPlainText(self._translate("main_window", self.recall_str))
        self.show_next_digit_fmn.setVisible(True)
        self.next_fmn.setVisible(True)
        self.next_fmn.setDisabled(False)
        self.prev_fmn.setVisible(True)
        self.prev_fmn.setDisabled(False)
        self.page_no_fmn.setVisible(True)
        self.page_no_fmn.setText(
            self._translate("main_window", "{}/50".format(self.counter + 1))
        )


    def applet_fmn(self):
        self.app_no = 2
        if self.running_applet:
            print("clicked stop:applet_fmn")
            self.begin_fmn.setText(self._translate("main_window", "begin"))
            self.running_applet = False
            self.stop_watch()
            self.next_fmn.setVisible(False)
            self.prev_fmn.setVisible(False)
            self.disp_panel_fmn.setVisible(False)
            self.recall_fmn.setVisible(True)
            self.page_no_fmn.setVisible(False)
        else:
            print("clicked begin:applet_fmn")
            self.begin_fmn.setText(self._translate("main_window", "stop"))
            self.counter = 0
            self.running_applet = True
            self.next_fmn.setVisible(True)
            self.prev_fmn.setVisible(True)
            self.next_fmn.setDisabled(False)
            self.prev_fmn.setDisabled(False)
            self.disp_panel_fmn.setVisible(True)
            self.recall_fmn.setVisible(False)
            self.page_no_fmn.setVisible(True)
            self.num_matrix = np.random.randint(
                10, size=(50, 10, 15)
            )  # create a num matrix 15x10x10
            self.start_watch()
            self.page_no_fmn.setText(
                self._translate("main_window", "{}/50".format(self.counter + 1))
            )
            self.display_num_matrix()

    def manual_mode(self):
        self.next_sc.setVisible(self.checkBox.isChecked())
        self.prev_sc.setVisible(self.checkBox.isChecked())
        if self.checkBox.isChecked():
            self.time_step = 1704351
        else:
            self.time_step = self.doubleSpinBox.value()

    def manual_next(self):
        if self.counter < 52:
            self.update_image()

    def manual_prev(self):
        self.counter -= 2
        if self.counter < 0:
            self.counter = 0
        self.update_image()

    def display_num_matrix_bn(self):
        self.matr2str = "\n".join(
            "    ".join("%d" % x for x in y) for y in self.num_matrix_bn[self.counter]
        )
        self.disp_panel_bn.setPlainText(self._translate("main_window", self.matr2str))

    def show_next_digit_bn_fn(self):
        self.x_count += 1
        if(self.x_count*self.y_count > 150):
            self.click_next_bn()
        if(self.x_count == 16): # dont hardcode this!
            self.x_count = 1
            self.y_count += 1
            self.recall_str += "\n   "
        else:
            self.recall_str += "   "
        self.recall_str += str(self.num_matrix_bn[self.counter][self.y_count-1][self.x_count-1])
        self.disp_panel_bn.setPlainText(self._translate("main_window", self.recall_str))

    def click_next_bn(self):
        if self.counter >= 49:
            self.next_bn.setDisabled(True)
            self.prev_bn.setDisabled(False)
        else:
            self.next_bn.setDisabled(False)
            self.prev_bn.setDisabled(False)
            self.counter += 1
            self.page_no_bn.setText(
                self._translate("main_window", "{}/50".format(self.counter + 1))
            )
            if self.recall_mode:
                self.x_count = 0
                self.y_count = 1
                self.recall_str = ""
                self.disp_panel_bn.setPlainText(self._translate("main_window", self.recall_str))
            else:
                self.display_num_matrix_bn()

    def click_prev_bn(self):
        if self.counter <= 0:
            self.prev_bn.setDisabled(True)
            self.next_bn.setDisabled(False)
        else:
            self.prev_bn.setDisabled(False)
            self.next_bn.setDisabled(False)
            self.counter -= 1
            self.page_no_bn.setText(
                self._translate("main_window", "{}/50".format(self.counter + 1))
            )
            if self.recall_mode:
                self.x_count = 0
                self.y_count = 1
                self.recall_str = ""
                self.disp_panel_bn.setPlainText(self._translate("main_window", self.recall_str))
            else:
                self.display_num_matrix_bn()

    # fold_here
    def recall_bn_fn(self):
        self.watch_reset()
        self.counter = 0
        self.recall_mode = True
        self.recall_str = ""
        self.disp_panel_bn.setPlainText(self._translate("main_window", self.recall_str))
        self.x_count = 0
        self.y_count = 1
        self.recall_bn.setVisible(False)
        self.show_next_digit_bn.setVisible(True)
        self.disp_panel_bn.setVisible(True)
        self.next_bn.setVisible(True)
        self.prev_bn.setVisible(True)
        self.page_no_bn.setVisible(True)
        self.page_no_bn.setText(
            self._translate("main_window", "{}/50".format(self.counter + 1))
        )

    def applet_bn(self):
        self.app_no = 5
        print("clicked begin applet bn")
        if self.running_applet:
            self.begin_bn.setText(self._translate("main_window", "begin"))
            self.running_applet = False
            self.stop_watch()
            self.next_bn.setVisible(False)
            self.prev_bn.setVisible(False)
            self.disp_panel_bn.setVisible(False)
            self.recall_bn.setVisible(True)
            self.page_no_bn.setVisible(False)
        else:
            self.begin_bn.setText(self._translate("main_window", "stop"))
            self.counter = 0
            self.running_applet = True
            self.next_bn.setVisible(True)
            self.prev_bn.setVisible(True)
            self.next_bn.setDisabled(False)
            self.prev_bn.setDisabled(False)
            self.recall_bn.setVisible(False)
            self.disp_panel_bn.setVisible(True)
            self.page_no_bn.setVisible(True)
            self.num_matrix_bn = np.random.randint(
                2, size=(50, 10, 15)
            )  # create a num matrix 15x10x10
            self.start_watch()
            self.page_no_bn.setText(
                self._translate("main_window", "{}/50".format(self.counter + 1))
            )
            self.display_num_matrix_bn()

    def hide_timer(self):
        if self.app_no == 1:
            self.lcdNumber.setVisible(not self.hide_timer_sc.isChecked())
        if self.app_no == 2:
            self.timer_fmn.setVisible(not self.hide_timer_fmn.isChecked())
        if self.app_no == 3:
            self.timer_fmw.setVisible(not self.hide_timer_fmw.isChecked())
        if self.app_no == 4:
            self.timer_sn.setVisible(not self.hide_timer_sn.isChecked())
        if self.app_no == 5:
            self.timer_bn.setVisible(not self.checkbox_bn.isChecked())

    def update_sn(self):
        print("entered update_sn")
        if self.counter < 1000 and self.running_applet == True:
            print("counter = " + str(self.counter))
            print(":/dat/sn/" + str(self.num_list_sn[self.counter]) + ".wav")
            QSound.play(":/dat/sn/" + str(self.num_list_sn[self.counter]) + ".wav")
            self.counter += 1
            QtCore.QTimer.singleShot(1000, self.update_sn)

    def recall_sn_fn(self):
        self.watch_reset()
        self.recall_sn.setVisible(False)
        self.num_disp_sn.setVisible(True)
        ls2str = ""
        for i in range(self.counter):
            ls2str = ls2str + str(i + 1) + ") " + str(self.num_list_sn[i]) + "\n"
        self.num_disp_sn.setPlainText(self._translate("main_window", ls2str))

    def applet_sn(self):
        self.app_no = 4
        print("clicked begin applet sn")
        if not self.running_applet:  # when begin clicked while not running
            self.begin_sn.setText(self._translate("main_window", "stop"))
            self.counter = 0
            self.running_applet = True
            self.num_list_sn = np.random.randint(10, size=(1000))
            self.start_watch()
            self.recall_sn.setVisible(False)
            self.num_disp_sn.setVisible(False)
            self.speaker_icon_sn.setVisible(True)
            self.update_sn()
        else:  # when stop clicked while running
            self.begin_sn.setText(self._translate("main_window", "begin"))
            self.running_applet = False
            self.stop_watch()
            self.speaker_icon_sn.setVisible(False)
            self.num_disp_sn.setVisible(False)
            self.recall_sn.setVisible(True)

    def populate_fmw(self):
        values = []
        # Get the complete list from word bank
        # randomly select 1000 words from the word bank
        # add it to the table
        word_list_full = [line.strip() for line in open(":/dat/wordbank.txt")]
        word_list = random.choices(word_list_full, k=500)
        word_matrix = [[word_list[5 * j + i] for i in range(5)] for j in range(100)]

        for value in word_matrix:
            row = []
            for item in value:
                cell = QtGui.QStandardItem(str(item))
                row.append(cell)
            self.model.appendRow(row)

    def applet_fmw(self):
        self.app_no = 3
        if not self.running_applet:
            print("clicked begin:applet_fmw")
            self.running_applet = True
            self.table_fmw.setVisible(True)
            self.begin_fmw.setVisible(True)
            self.begin_fmw.setText(self._translate("main_window", "stop"))
            self.recall_fmw.setVisible(False)
            self.counter = 0
            for idx in range(100):
                self.model.removeRow(99 - idx)
            self.start_watch()
            self.populate_fmw()
        else:
            print("clicked stop:applet_fmw")
            self.running_applet = False
            self.table_fmw.setVisible(False)
            self.begin_fmw.setVisible(True)
            self.begin_fmw.setText(self._translate("main_window", "restart"))
            self.recall_fmw.setVisible(True)
            self.stop_watch()

    def recall_fmw_fn(self, signal):
        def double_click_event():
            print("haha")

        #            row = signal.row()
        #            column = signal.column()
        #            print("row = ", row)
        #            self.table_fmw.showRow(row)
        self.watch_reset()
        print("recall_fmw")
        self.begin_fmw.setVisible(True)
        self.begin_fmw.setText("restart")
        self.table_fmw.setVisible(True)
        self.recall_fmw.setVisible(False)
        #        for i in range(5):
        #            self.table_fmw.hideColumn(i)
        self.table_fmw.setShowGrid(True)
        self.table_fmw.doubleClicked.connect(double_click_event)

    # ========================================================================================

    def retranslateUi(self, main_window):
        self._translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(self._translate("main_window", "MainWindow"))
        self.app_descr.setHtml(
            self._translate(
                "main_window",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'Sans Serif'; font-size:20pt; font-weight:400; font-style:normal;\">\n"
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:12pt; color:#ffffff;">This app is aimed at users who wish to hone their memorizing skills for events like XMT and WMC. Choose from the following list to begin your training session:</span></p></body></html>',
            )
        )
        self.button_fmw.setText(
            self._translate("main_window", "15-minute random list of words")
        )
        self.button_exit.setText(self._translate("main_window", "Exit"))
        self.speed_cards_button.setText(self._translate("main_window", "Speed Cards"))
        self.app_title.setText(self._translate("main_window", "MnemoPy Arena"))
        self.button_fmn.setText(self._translate("main_window", "5-minute numbers"))
        self.time_delay_label.setText(
            self._translate("main_window", "Enter time delay :")
        )
        self.begin_sc.setText(self._translate("main_window", "begin"))
        self.pause_sc.setText(self._translate("main_window", "pause"))
        self.hide_timer_sc.setText(self._translate("main_window", "hide timer"))
        self.hide_timer_fmw.setText(self._translate("main_window", "hide timer"))
        self.recall_sc.setText(self._translate("main_window", "recall"))
        self.button_quit.setText(self._translate("main_window", "quit to main menu"))
        self.exit_sc.setToolTip(
            self._translate(
                "main_window",
                "<html><head/><body><p>exit the program</p></body></html>",
            )
        )
        self.exit_sc.setWhatsThis(
            self._translate(
                "main_window",
                "<html><head/><body><p>exit the program</p></body></html>",
            )
        )
        self.exit_sc.setText(self._translate("main_window", "exit"))
        self.quit_fmn.setText(self._translate("main_window", "quit to main menu"))
        self.begin_fmn.setText(self._translate("main_window", "begin"))
        self.exit_fmn.setText(self._translate("main_window", "exit"))
        self.prev_fmn.setText(self._translate("main_window", "prev"))
        self.disp_panel_fmn.setPlainText(self._translate("main_window", ""))
        self.next_fmn.setText(self._translate("main_window", "next"))
        self.checkBox.setText(self._translate("main_window", "manual"))
        self.recall_fmn.setText(self._translate("main_window", "recall"))
        self.hide_timer_fmn.setText(self._translate("main_window", "hide clock"))
        self.next_sc.setText(self._translate("main_window", "next"))
        self.prev_sc.setText(self._translate("main_window", "prev"))
        self.button_sn.setText(self._translate("main_window", "Spoken numbers"))
        self.button_bn.setText(self._translate("main_window", "Binary numbers"))
        self.begin_fmw.setText(self._translate("main_window", "begin"))
        self.recall_fmw.setText(self._translate("main_window", "recall"))
        self.quit_fmw.setText(self._translate("main_window", "quit to main menu"))
        self.exit_fmw.setText(self._translate("main_window", "exit"))
        self.begin_sn.setText(self._translate("main_window", "begin"))
        self.recall_sn.setText(self._translate("main_window", "recall"))
        self.quit_sn.setText(self._translate("main_window", "quit to main menu"))
        self.exit_sn.setText(self._translate("main_window", "exit"))
        self.hide_timer_sn.setText(self._translate("main_window", "hide timer"))
        self.prev_bn.setText(self._translate("main_window", "prev"))
        self.quit_bn.setText(self._translate("main_window", "quit to main menu"))
        self.checkbox_bn.setText(self._translate("main_window", "hide clock"))
        self.begin_bn.setText(self._translate("main_window", "begin"))
        self.button_exit_bn.setText(self._translate("main_window", "exit"))
        self.recall_bn.setText(self._translate("main_window", "recall"))
        self.next_bn.setText(self._translate("main_window", "next"))
        self.card_no_sc.setText(self._translate("main_window", "--/52"))
        self.show_next_digit_fmn.setText(self._translate("main_window", ">"))
        self.show_next_digit_bn.setText(self._translate("main_window", ">"))

