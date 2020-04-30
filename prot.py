import datetime
import random
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtMultimedia import QSound
import sys


class Ui_main_window(object):
    def setupUi(self, main_window):
        
        self.running_applet = False
        self.counter = 0
        self.app_no = 0

        self.watch_counter = 0
        self.is_watch_reset = True

        self.watch_timer = QtCore.QTimer()
        self.watch_timer.timeout.connect(self.run_watch)
        self.watch_timer.setInterval(1)

        main_window.setObjectName("main_window")
        main_window.resize(739, 446)
        main_window.setStyleSheet("background-color: rgb(18, 18, 18);")
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")
        self.stacked_windows = QtWidgets.QStackedWidget(self.centralwidget)
        self.stacked_windows.setGeometry(QtCore.QRect(0, -20, 731, 441))
        self.stacked_windows.setObjectName("stacked_windows")
#========================================================================================
        self.page_main_menu = QtWidgets.QWidget()
        self.page_main_menu.setObjectName("page_main_menu")
        self.app_descr = QtWidgets.QTextBrowser(self.page_main_menu)
        self.app_descr.setGeometry(QtCore.QRect(100, 130, 551, 81))
        self.app_descr.setStyleSheet("font: 20pt \"Sans Serif\";\n"
"")
        self.app_descr.setObjectName("app_descr")
        self.button_15min_words = QtWidgets.QPushButton(self.page_main_menu)
        self.button_15min_words.setGeometry(QtCore.QRect(430, 240, 201, 23))
        self.button_15min_words.setStyleSheet("color: rgb(255, 255, 255);")
        self.button_15min_words.setObjectName("button_15min_words")
        self.button_15min_words.clicked.connect(self.open_window_15min_words)
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
        self.app_title.setGeometry(QtCore.QRect(210, 60, 331, 71))
        self.app_title.setStyleSheet("font: 30pt \"Sans Serif\";\n"
"color: rgb(255, 56, 56)")
        self.app_title.setObjectName("app_title")
        self.button_5min_num = QtWidgets.QPushButton(self.page_main_menu)
        self.button_5min_num.setGeometry(QtCore.QRect(260, 240, 141, 23))
        self.button_5min_num.setStyleSheet("color: rgb(255, 255, 255);")
        self.button_5min_num.setObjectName("button_5min_num")
        self.button_5min_num.clicked.connect(self.open_window_5min_nums)
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
        self.heart_img.setPixmap(QtGui.QPixmap("img/love.png"))
        self.heart_img.setScaledContents(True)
        self.heart_img.setObjectName("heart_img")
        self.stacked_windows.addWidget(self.page_main_menu)

#_______________________ SPEED CARDS____________________________

        self.page_speedcards = QtWidgets.QWidget()
        self.page_speedcards.setObjectName("page_speedcards")
        self.time_delay_label = QtWidgets.QLabel(self.page_speedcards)
        self.time_delay_label.setGeometry(QtCore.QRect(30, 60, 121, 16))
        self.time_delay_label.setStyleSheet("color:rgb(255, 255, 255)")
        self.time_delay_label.setObjectName("time_delay_label")
        self.time_delay_label.setVisible(True)
        self.button_begin = QtWidgets.QPushButton(self.page_speedcards)
        self.button_begin.setGeometry(QtCore.QRect(30, 100, 80, 23))
        self.button_begin.setStyleSheet("color: rgb(255, 255, 255);")
        self.button_begin.setObjectName("button_begin")
        self.button_begin.clicked.connect(self.applet_sc)
        self.button_begin.setVisible(True)
        self.button_pause = QtWidgets.QPushButton(self.page_speedcards)
        self.button_pause.setGeometry(QtCore.QRect(130, 100, 80, 23))
        self.button_pause.setStyleSheet("color: rgb(255, 255, 255);")
        self.button_pause.setObjectName("button_pause")
        self.button_pause.setVisible(False)
        self.button_pause.clicked.connect(self.pause_action)
        self.button_hide_timer = QtWidgets.QCheckBox(self.page_speedcards)
        self.button_hide_timer.setGeometry(QtCore.QRect(230, 100, 82, 23))
        self.button_hide_timer.setStyleSheet("color: rgb(255, 255, 255);")
        self.button_hide_timer.setObjectName("button_hide_timer")
        self.button_hide_timer.clicked.connect(self.hide_timer)
        self.button_hide_timer.setVisible(True)
        self.button_recall = QtWidgets.QPushButton(self.page_speedcards)
        self.button_recall.setGeometry(QtCore.QRect(330, 100, 80, 23))
        self.button_recall.setStyleSheet("color: rgb(255, 255, 255);")
        self.button_recall.setObjectName("button_recall")
        self.button_recall.setVisible(False)
        self.button_recall.clicked.connect(self.recall_sc_fn)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.page_speedcards)
        self.doubleSpinBox.setGeometry(QtCore.QRect(160, 60, 61, 24))
        self.doubleSpinBox.setStyleSheet("background-color: rgb(102, 102, 102);")
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.doubleSpinBox.setMinimum(0)
        self.doubleSpinBox.setDecimals(2)
        self.doubleSpinBox.setVisible(True)
        self.button_next_sc = QtWidgets.QPushButton(self.page_speedcards)
        self.button_next_sc.setGeometry(QtCore.QRect(590, 280, 80, 23))
        self.button_next_sc.setStyleSheet("color: rgb(255, 255, 255);")
        self.button_next_sc.clicked.connect(self.manual_next)
        self.button_next_sc.setObjectName("button_next_sc")
        self.button_next_sc.setVisible(False)
        self.button_prev_sc = QtWidgets.QPushButton(self.page_speedcards)
        self.button_prev_sc.setGeometry(QtCore.QRect(590, 320, 80, 23))
        self.button_prev_sc.setStyleSheet("color: rgb(255, 255, 255);")
        self.button_prev_sc.setObjectName("button_prev_sc")
        self.button_prev_sc.clicked.connect(self.manual_prev)
        self.button_prev_sc.setVisible(False)
        self.button_quit = QtWidgets.QPushButton(self.page_speedcards)
        self.button_quit.setGeometry(QtCore.QRect(430, 100, 141, 23))
        self.button_quit.setStyleSheet("color: rgb(255, 255, 255);")
        self.button_quit.setObjectName("button_quit")
        self.button_quit.clicked.connect(self.return_to_main_menu)
        self.button_exit_2 = QtWidgets.QPushButton(self.page_speedcards)
        self.button_exit_2.setGeometry(QtCore.QRect(590, 100, 80, 23))
        self.button_exit_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.button_exit_2.setObjectName("button_exit_2")
        self.button_exit_2.clicked.connect(self.exit_the_app)
        self.card_image = QtWidgets.QLabel(self.page_speedcards)
        self.card_image.setGeometry(QtCore.QRect(270, 150, 181, 261))
        self.card_image.setText("")
        pixmap = QtGui.QPixmap("card_images/back.png")
        self.card_image.setPixmap(pixmap.scaled(150,300,QtCore.Qt.KeepAspectRatio))
        self.lcdNumber = QtWidgets.QLCDNumber(self.page_speedcards)
        self.lcdNumber.setGeometry(QtCore.QRect(590, 160, 111, 31))
        self.lcdNumber.setObjectName("lcdNumber")
        self.checkBox = QtWidgets.QCheckBox(self.page_speedcards)
        self.checkBox.setGeometry(QtCore.QRect(590, 210, 85, 21))
        self.checkBox.setStyleSheet("color: rgb(255, 255, 255);")
        self.checkBox.setObjectName("checkBox")
        self.checkBox.stateChanged.connect(self.manual_mode)
        self.card_no_sc = QtWidgets.QLabel(self.page_speedcards)
        self.card_no_sc.setGeometry(QtCore.QRect(530, 300, 41, 20))
        self.card_no_sc.setStyleSheet("color:rgb(255, 255, 255)")
        self.card_no_sc.setObjectName("card_no_sc")
        self.stacked_windows.addWidget(self.page_speedcards)

#___________________5 MINUTE WORDS___________________________

        self.page_5min_nums = QtWidgets.QWidget()
        self.page_5min_nums.setObjectName("page_5min_nums")
        # quit button
        self.button_quit_2 = QtWidgets.QPushButton(self.page_5min_nums)
        self.button_quit_2.setGeometry(QtCore.QRect(210, 50, 131, 23))
        self.button_quit_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.button_quit_2.setObjectName("button_quit_2")
        self.button_quit_2.clicked.connect(self.return_to_main_menu)
        # begin button
        self.begin_fmn = QtWidgets.QPushButton(self.page_5min_nums)
        self.begin_fmn.setGeometry(QtCore.QRect(30, 50, 80, 23))
        self.begin_fmn.setStyleSheet("color: rgb(255, 255, 255);")
        self.begin_fmn.setObjectName("begin_fmn")
        self.begin_fmn.clicked.connect(self.applet_fmn)
        # exit button
        self.exit_fmn = QtWidgets.QPushButton(self.page_5min_nums)
        self.exit_fmn.setGeometry(QtCore.QRect(350, 50, 80, 23))
        self.exit_fmn.setStyleSheet("color: rgb(255, 255, 255);")
        self.exit_fmn.setObjectName("exit_fmn")
        self.exit_fmn.clicked.connect(self.exit_the_app)
        # prev button
        self.button_prev = QtWidgets.QPushButton(self.page_5min_nums)
        self.button_prev.setGeometry(QtCore.QRect(230, 380, 80, 23))
        self.button_prev.setStyleSheet("color: rgb(255, 255, 255);")
        self.button_prev.setVisible(False)
        self.button_prev.setObjectName("button_prev")
        self.button_prev.clicked.connect(self.click_prev)
        # next button
        self.button_next = QtWidgets.QPushButton(self.page_5min_nums)
        self.button_next.setGeometry(QtCore.QRect(380, 380, 80, 23))
        self.button_next.setStyleSheet("color: rgb(255, 255, 255);")
        self.button_next.setVisible(False)
        self.button_next.setObjectName("button_next")
        self.button_next.clicked.connect(self.click_next)
        # recall button
        self.recall_fmn = QtWidgets.QPushButton(self.page_5min_nums)
        self.recall_fmn.setGeometry(QtCore.QRect(120, 50, 80, 23))
        self.recall_fmn.setStyleSheet("color: rgb(255, 255, 255);")
        self.recall_fmn.setObjectName("recall_fmn")
        self.recall_fmn.setVisible(False)
        self.recall_fmn.clicked.connect(self.recall_fmn_fn)
        # lcd watch 
        self.timer_fmn = QtWidgets.QLCDNumber(self.page_5min_nums)
        self.timer_fmn.setGeometry(QtCore.QRect(563, 32, 131, 41))
        self.timer_fmn.setObjectName("timer_fmn")
        # number display panel
        self.disp_panel_fmn = QtWidgets.QTextBrowser(self.page_5min_nums)
        self.disp_panel_fmn.setGeometry(QtCore.QRect(90, 100, 511, 251))
        self.disp_panel_fmn.setObjectName("disp_panel_fmn")
        self.disp_panel_fmn.setStyleSheet("font: 13.5pt \"Sans Serif\";\n"
"color: rgb(255, 255, 255);")
        # page no label
        self.page_no_fmn = QtWidgets.QLabel(self.page_5min_nums)
        self.page_no_fmn.setGeometry(QtCore.QRect(327, 380, 34, 21))
        self.page_no_fmn.setObjectName("page_no_fmn")
        self.page_no_fmn.setStyleSheet("color: rgb(255, 255, 255);")
        # hide clock checkbox
        self.hide_clock_checkbox = QtWidgets.QCheckBox(self.page_5min_nums)
        self.hide_clock_checkbox.setGeometry(QtCore.QRect(620, 90, 85, 21))
        self.hide_clock_checkbox.setStyleSheet("color: rgb(255, 255, 255);")
        self.hide_clock_checkbox.setObjectName("hide_clock_checkbox")
        self.hide_clock_checkbox.stateChanged.connect(self.hide_timer)

        self.stacked_windows.addWidget(self.page_5min_nums)

#___________________15 MINUTE RANDOM WORDS______________________

        self.page_15min_words = QtWidgets.QWidget()
        self.page_15min_words.setObjectName("page_15min_words")
        self.button_begin_7 = QtWidgets.QPushButton(self.page_15min_words)
        self.button_begin_7.setGeometry(QtCore.QRect(30, 50, 80, 23))
        self.button_begin_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.button_begin_7.setObjectName("button_begin_7")
        self.button_recall_4 = QtWidgets.QPushButton(self.page_15min_words)
        self.button_recall_4.setGeometry(QtCore.QRect(130, 50, 80, 23))
        self.button_recall_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.button_recall_4.setObjectName("button_recall_4")
        self.button_quit_7 = QtWidgets.QPushButton(self.page_15min_words)
        self.button_quit_7.setGeometry(QtCore.QRect(230, 50, 131, 23))
        self.button_quit_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.button_quit_7.setObjectName("button_quit_7")
        self.button_quit_7.clicked.connect(self.return_to_main_menu)
        self.button_exit_10 = QtWidgets.QPushButton(self.page_15min_words)
        self.button_exit_10.setGeometry(QtCore.QRect(380, 50, 80, 23))
        self.button_exit_10.setStyleSheet("color: rgb(255, 255, 255);")
        self.button_exit_10.setObjectName("button_exit_10")
        self.button_exit_10.clicked.connect(self.exit_the_app)
        self.lcdNumber_15min_words = QtWidgets.QLCDNumber(self.page_15min_words)
        self.lcdNumber_15min_words.setGeometry(QtCore.QRect(640, 50, 64, 23))
        self.lcdNumber_15min_words.setObjectName("lcdNumber_15min_words")
        self.stacked_windows.addWidget(self.page_15min_words)

#________________ SPOKEN NUMBERS____________________________

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
        self.num_disp_sn.setStyleSheet("font: 13.5pt \"Sans Serif\";\n color: rgb(255, 255, 255);")
        self.speaker_icon_sn = QtWidgets.QLabel(self.page_sn)
        self.speaker_icon_sn.setGeometry(QtCore.QRect(350, 120, 161, 141))
        self.speaker_icon_sn.setText("")
        self.speaker_icon_sn.setObjectName("speaker_icon_label")
        pixmap = QtGui.QPixmap("sn/speaker_icon.png")
        self.speaker_icon_sn.setPixmap(pixmap.scaled(150,300,QtCore.Qt.KeepAspectRatio))
        self.speaker_icon_sn.setVisible(False)
        self.stacked_windows.addWidget(self.page_sn)

#___________________BINARY NUMBERS _________________________

        self.page_bn = QtWidgets.QWidget()
        self.page_bn.setObjectName("page_bn")
        self.prev_bn = QtWidgets.QPushButton(self.page_bn)
        self.prev_bn.setGeometry(QtCore.QRect(237, 388, 80, 23))
        self.prev_bn.setStyleSheet("color: rgb(255, 255, 255);")
        self.prev_bn.setObjectName("prev_bn")
        self.prev_bn.setDisabled(True)
        self.prev_bn.setVisible(False)
        self.prev_bn.clicked.connect(self.click_prev_bn)
        self.button_quit_bn = QtWidgets.QPushButton(self.page_bn)
        self.button_quit_bn.setGeometry(QtCore.QRect(217, 58, 131, 23))
        self.button_quit_bn.setStyleSheet("color: rgb(255, 255, 255);")
        self.button_quit_bn.setObjectName("button_quit_bn")
        self.button_quit_bn.clicked.connect(self.return_to_main_menu)
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
        self.disp_panel_bn.setStyleSheet("font: 13.5pt \"Sans Serif\";\n"
"color: rgb(255, 255, 255);")
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
        self.stacked_windows.addWidget(self.page_bn)

#========================================================================================

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

#========================================================================================

    def pause_action(self):
        if self.running_applet == True:
            print("Pausing the applet")
            if self.app_no == 1:
                self.button_pause.setText(self._translate("main_window","unpause"))
            self.running_applet = not self.running_applet
        else:
            print("Unpausing the applet")
            if self.app_no == 1:
                self.button_pause.setText(self._translate("main_window","pause"))
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
        self.counter = 0
        if self.app_no == 1:
            pixmap = QtGui.QPixmap("card_images/back.png")
            self.card_image.setPixmap(pixmap.scaled(150,300,QtCore.Qt.KeepAspectRatio))
        if self.app_no == 2:
            self.disp_panel_fmn.setPlainText(self._translate("main_window",""))
            self.page_no_fmn.setText(self._translate("main_window","{}/10".format(self.counter+1)))
            self.button_next.setDisabled(True)
            self.button_prev.setDisabled(True)
            self.button_begin.setText(self._translate("main_window","begin"))
        if self.app_no == 4:
            self.speaker_icon_sn.setVisible(False)
            self.num_disp_sn.setVisible(False)
            self.recall_sn.setVisible(False)
        if self.app_no == 5:
            self.disp_panel_bn.setPlainText(self._translate("main_window",""))
            self.page_no_bn.setText(self._translate("main_window","{}/10".format(self.counter+1)))
            self.next_bn.setDisabled(True)
            self.prev_bn.setDisabled(True)

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
            self.card_image.setPixmap(pixmap.scaled(150,300,QtCore.Qt.KeepAspectRatio))
            self.card_image.setObjectName("card_image")
            self.counter += 1
            self.card_no_sc.setText(self._translate("main_window", "{}/52".format(str(self.counter))))
            if not self.checkBox.isChecked() and self.running_applet:
                QtCore.QTimer.singleShot(self.time_step*1260, self.update_image)
#        elif self.running_applet == False:
#            self.counter += 1
#            update_image(self)

#                self.running_applet = False
#                self.stop_watch()
#                self.button_begin.setText(self._translate("main_window","begin"))
#                self.button_pause.setVisible(False)
#                self.counter = 0

    def applet_sc(self):
        self.app_no = 1
        self.time_step = self.doubleSpinBox.value()
        if self.running_applet == False: # clicked when 'begin' visible, applet not running
            self.button_begin.setText(self._translate("main_window","stop"))
            self.button_pause.setVisible(True)
            self.time_delay_label.setVisible(True)
            self.doubleSpinBox.setVisible(True)
            self.start_watch()
            self.button_recall.setVisible(False)
            ranks = [str(n) for n in range(2,11)] + list('JQKA')
            suits = ['S', 'D', 'C', 'H']
            Deck = [rank + suit for suit in suits for rank in ranks]
            
            Cards = random.sample(Deck, 52)
            self.images = []
            img_path = "card_images/"
            
            for i in range(52):
                img_name = (Cards[i]+ ".png")
                full_img_loc = img_path + img_name
                self.images = self.images + [full_img_loc]
    
            self.counter = 0
            self.running_applet = True
            self.update_image()
        else: # clicked when 'stop' visible, applet running
            self.button_begin.setText(self._translate("main_window","begin"))
            self.button_pause.setVisible(False)
            self.stop_watch()
            self.button_recall.setVisible(True)
            self.running_applet = False

    def recall_sc_fn(self):
        print("speedcards recall")
        self.counter = 0
        pixmap = QtGui.QPixmap("card_images/back.png")
        self.card_image.setPixmap(pixmap.scaled(150,300,QtCore.Qt.KeepAspectRatio))
        self.card_no_sc.setText(self._translate("main_window", "--/52"))
        self.button_recall.setVisible(False)
        self.time_delay_label.setVisible(False)
        self.doubleSpinBox.setVisible(False)
        self.button_next_sc.setVisible(True)
        self.button_prev_sc.setVisible(True)
        self.button_begin.setText(self._translate("main_window","restart"))
        self.watch_reset()
        self.checkBox.setChecked(True)

    def showLCD(self):
        text = str(datetime.timedelta(milliseconds=self.watch_counter))[:-3]
        if self.app_no == 1:
            self.lcdNumber.setDigitCount(11)
            if not self.is_watch_reset:  # if "is_watch_reset" is False
                self.lcdNumber.display(text)
            else:
                self.lcdNumber.display('0:00:00.000')
        if self.app_no == 2:
            self.timer_fmn.setDigitCount(11)
            if not self.is_watch_reset:  # if "is_watch_reset" is False
                self.timer_fmn.display(text)
            else:
                self.timer_fmn.display('0:00:00.000')

        if self.app_no == 4:
            self.timer_sn.setDigitCount(11)
            if not self.is_watch_reset:  # if "is_watch_reset" is False
                self.timer_sn.display(text)
            else:
                self.timer_sn.display('0:00:00.000')

        if self.app_no == 5:
            self.timer_bn.setDigitCount(11)
            if not self.is_watch_reset:  # if "is_watch_reset" is False
                self.timer_bn.display(text)
            else:
                self.timer_bn.display('0:00:00.000')

    def run_watch(self):
        self.watch_counter += 1
        self.showLCD()

    def start_watch(self):
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
        matr2str = '\n'.join('    '.join('%d' %x for x in y) for y in self.num_matrix[self.counter])
        self.disp_panel_fmn.setPlainText(self._translate("main_window",matr2str))

    def click_next(self):
        if self.counter >= 49:
            self.button_next.setDisabled(True)
            self.button_prev.setDisabled(False)
        else:
            self.button_next.setDisabled(False)
            self.button_prev.setDisabled(False)
            self.counter += 1
            self.page_no_fmn.setText(self._translate("main_window","{}/10".format(self.counter+1)))
            self.display_num_matrix()

    def click_prev(self):
        if self.counter <= 0:
            self.button_prev.setDisabled(True)
            self.button_next.setDisabled(False)
        else:
            self.button_prev.setDisabled(False)
            self.button_next.setDisabled(False)
            self.counter -= 1
            self.page_no_fmn.setText(self._translate("main_window","{}/50".format(self.counter+1)))
            self.display_num_matrix()
    def recall_fmn_fn(self):
        self.watch_reset()
        self.counter = 0
        self.recall_fmn.setVisible(False)
        self.disp_panel_fmn.setVisible(True)
        self.button_next.setVisible(True)
        self.button_next.setDisabled(False)
        self.button_prev.setVisible(True)
        self.button_prev.setDisabled(False)
        self.page_no_fmn.setVisible(True)
        self.page_no_fmn.setText(self._translate("main_window","{}/50".format(self.counter+1)))


    def applet_fmn(self):
        self.app_no = 2
        print("clicked begin applet 5min num")
        if self.running_applet:
            self.begin_fmn.setText(self._translate("main_window","begin"))
            self.running_applet = False
            self.stop_watch()
            self.button_next.setVisible(False)
            self.button_prev.setVisible(False)
            self.disp_panel_fmn.setVisible(False)
            self.recall_fmn.setVisible(True)
            self.page_no_fmn.setVisible(False)
        elif not self.running_applet:
            self.begin_fmn.setText(self._translate("main_window","stop"))
            self.counter = 0
            self.running_applet = True
            self.button_next.setVisible(True)
            self.button_prev.setVisible(True)
            self.disp_panel_fmn.setVisible(True)
            self.recall_fmn.setVisible(False)
            self.page_no_fmn.setVisible(True)
            self.num_matrix = np.random.randint(10, size=(50,10,15)) # create a num matrix 15x10x10
            self.start_watch()
            self.page_no_fmn.setText(self._translate("main_window","{}/50".format(self.counter+1)))
            self.display_num_matrix()

    def manual_mode(self):
        self.button_next_sc.setVisible(self.checkBox.isChecked())
        self.button_prev_sc.setVisible(self.checkBox.isChecked())
        if self.checkBox.isChecked():
             self.time_step = 1704351
        else :
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
        matr2str = '\n'.join('    '.join('%d' %x for x in y) for y in self.num_matrix_bn[self.counter])
        self.disp_panel_bn.setPlainText(self._translate("main_window",matr2str))

    def click_next_bn(self):
        if self.counter >= 49:
            self.next_bn.setDisabled(True)
            self.prev_bn.setDisabled(False)
        else:
            self.next_bn.setDisabled(False)
            self.prev_bn.setDisabled(False)
            self.counter += 1
            self.page_no_bn.setText(self._translate("main_window","{}/50".format(self.counter+1)))
            self.display_num_matrix_bn()

    def click_prev_bn(self):
        if self.counter <= 0:
            self.prev_bn.setDisabled(True)
            self.next_bn.setDisabled(False)
        else:
            self.prev_bn.setDisabled(False)
            self.next_bn.setDisabled(False)
            self.counter -= 1
            self.page_no_bn.setText(self._translate("main_window","{}/50".format(self.counter+1)))
            self.display_num_matrix_bn()

#fold_here
    def recall_bn_fn(self):
        self.watch_reset()
        self.counter = 0
        self.recall_bn.setVisible(False)
        self.disp_panel_bn.setVisible(True)
        self.next_bn.setVisible(True)
        self.prev_bn.setVisible(True)
        self.page_no_bn.setVisible(True)
        self.page_no_bn.setText(self._translate("main_window","{}/50".format(self.counter+1)))


    def applet_bn(self):
        self.app_no = 5
        print("clicked begin applet bn")
        if self.running_applet:
            self.begin_bn.setText(self._translate("main_window","begin"))
            self.running_applet = False
            self.stop_watch()
            self.next_bn.setVisible(False)
            self.prev_bn.setVisible(False)
            self.disp_panel_bn.setVisible(False)
            self.recall_bn.setVisible(True)
            self.page_no_bn.setVisible(False)
        elif not self.running_applet:
            self.begin_bn.setText(self._translate("main_window","stop"))
            self.counter = 0
            self.running_applet = True
            self.next_bn.setVisible(True)
            self.prev_bn.setVisible(True)
            self.recall_bn.setVisible(False)
            self.next_bn.setDisabled(False)
            self.disp_panel_bn.setVisible(True)
            self.page_no_bn.setVisible(True)
            self.num_matrix_bn = np.random.randint(2, size=(50,10,15)) # create a num matrix 15x10x10
            self.start_watch()
            self.page_no_bn.setText(self._translate("main_window","{}/50".format(self.counter+1)))
            self.display_num_matrix_bn()

    def hide_timer(self):
        if self.app_no == 1:
            self.lcdNumber.setVisible(not self.button_hide_timer.isChecked())
        if self.app_no == 2:
            self.timer_fmn.setVisible(not self.hide_clock_checkbox.isChecked())
        if self.app_no == 4:
            self.timer_sn.setVisible(not self.hide_timer_sn.isChecked())
        if self.app_no == 5:
            self.timer_bn.setVisible(not self.checkbox_bn.isChecked())

    def update_sn(self):
        print("entered update_sn")
        if self.counter < 1000 and self.running_applet == True:
            print("counter = " + str(self.counter))
            print("sn/" + str(self.num_list_sn[self.counter]) + ".wav")
            QSound.play("sn/" + str(self.num_list_sn[self.counter]) + ".wav")
            self.counter += 1
            QtCore.QTimer.singleShot(1260, self.update_sn)

    def recall_sn_fn(self):
            self.watch_reset()
            self.recall_sn.setVisible(False)
            self.num_disp_sn.setVisible(True)
            ls2str = ""
            for i in range(self.counter):
                ls2str = ls2str + str(i+1) + ") " + str(self.num_list_sn[i]) + "\n"
            self.num_disp_sn.setPlainText(self._translate("main_window",ls2str))

    def applet_sn(self):
        self.app_no = 4
        print("clicked begin applet sn")
        if not self.running_applet: # when begin clicked while not running
            self.begin_sn.setText(self._translate("main_window","stop"))
            self.counter = 0
            self.running_applet = True
            self.num_list_sn = np.random.randint(10, size=(1000))
            self.start_watch()
            self.recall_sn.setVisible(False)
            self.num_disp_sn.setVisible(False)
            self.speaker_icon_sn.setVisible(True)
            self.update_sn()
        else: # when stop clicked while running
            self.begin_sn.setText(self._translate("main_window","begin"))
            self.running_applet = False
            self.stop_watch()
            self.speaker_icon_sn.setVisible(False)
            self.num_disp_sn.setVisible(False)
            self.recall_sn.setVisible(True)



#========================================================================================

    def retranslateUi(self, main_window):
        self._translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(self._translate("main_window", "MainWindow"))
        self.app_descr.setHtml(self._translate("main_window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:20pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#ffffff;\">This app is aimed at users who wish to hone their memorizing skills for events like XMT and WMC. Choose from the following list to begin your training session:</span></p></body></html>"))
        self.button_15min_words.setText(self._translate("main_window", "15-minute random list of words"))
        self.button_exit.setText(self._translate("main_window", "Exit"))
        self.speed_cards_button.setText(self._translate("main_window", "Speed Cards"))
        self.app_title.setText(self._translate("main_window", "MnemoPy Arena"))
        self.button_5min_num.setText(self._translate("main_window", "5-minute numbers"))
        self.time_delay_label.setText(self._translate("main_window", "Enter time delay :"))
        self.button_begin.setText(self._translate("main_window", "begin"))
        self.button_pause.setText(self._translate("main_window", "pause"))
        self.button_hide_timer.setText(self._translate("main_window", "hide timer"))
        self.button_recall.setText(self._translate("main_window", "recall"))
        self.button_quit.setText(self._translate("main_window", "quit to main menu"))
        self.button_exit_2.setToolTip(self._translate("main_window", "<html><head/><body><p>exit the program</p></body></html>"))
        self.button_exit_2.setWhatsThis(self._translate("main_window", "<html><head/><body><p>exit the program</p></body></html>"))
        self.button_exit_2.setText(self._translate("main_window", "exit"))
        self.button_quit_2.setText(self._translate("main_window", "quit to main menu"))
        self.begin_fmn.setText(self._translate("main_window", "begin"))
        self.exit_fmn.setText(self._translate("main_window", "exit"))
        self.button_prev.setText(self._translate("main_window", "prev"))
        self.disp_panel_fmn.setPlainText(self._translate("main_window",""))
        self.button_next.setText(self._translate("main_window", "next"))
        self.checkBox.setText(self._translate("main_window", "manual"))
        self.recall_fmn.setText(self._translate("main_window", "recall"))
        self.hide_clock_checkbox.setText(self._translate("main_window", "hide clock"))
        self.button_next_sc.setText(self._translate("main_window", "next"))
        self.button_prev_sc.setText(self._translate("main_window", "prev"))
        self.button_sn.setText(self._translate("main_window", "Spoken numbers"))
        self.button_bn.setText(self._translate("main_window", "Binary numbers"))
        self.button_begin_7.setText(self._translate("main_window", "begin"))
        self.button_recall_4.setText(self._translate("main_window", "recall"))
        self.button_quit_7.setText(self._translate("main_window", "quit to main menu"))
        self.button_exit_10.setText(self._translate("main_window", "exit"))
        self.begin_sn.setText(self._translate("main_window", "begin"))
        self.recall_sn.setText(self._translate("main_window", "recall"))
        self.quit_sn.setText(self._translate("main_window", "quit to main menu"))
        self.exit_sn.setText(self._translate("main_window", "exit"))
        self.hide_timer_sn.setText(self._translate("main_window", "hide timer"))
        self.prev_bn.setText(self._translate("main_window", "prev"))
        self.button_quit_bn.setText(self._translate("main_window", "quit to main menu"))
        self.checkbox_bn.setText(self._translate("main_window", "hide clock"))
        self.begin_bn.setText(self._translate("main_window", "begin"))
        self.button_exit_bn.setText(self._translate("main_window", "exit"))
        self.recall_bn.setText(self._translate("main_window", "recall"))
        self.next_bn.setText(self._translate("main_window", "next"))
        self.card_no_sc.setText(self._translate("main_window", "--/52"))

#========================================================================================

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_main_window()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
