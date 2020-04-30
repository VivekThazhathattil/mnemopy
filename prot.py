import datetime
import random
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_main_window(object):
    def setupUi(self, main_window):
        
        self.running_applet = False
        self.counter = 0

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
        self.stacked_windows.addWidget(self.page_main_menu)

#========================================================================================

        self.page_speedcards = QtWidgets.QWidget()
        self.page_speedcards.setObjectName("page_speedcards")
        self.time_delay_label = QtWidgets.QLabel(self.page_speedcards)
        self.time_delay_label.setGeometry(QtCore.QRect(30, 60, 121, 16))
        self.time_delay_label.setStyleSheet("color:rgb(255, 255, 255)")
        self.time_delay_label.setObjectName("time_delay_label")
        self.button_begin = QtWidgets.QPushButton(self.page_speedcards)
        self.button_begin.setGeometry(QtCore.QRect(30, 100, 80, 23))
        self.button_begin.setStyleSheet("color: rgb(255, 255, 255);")
        self.button_begin.setObjectName("button_begin")
        self.button_begin.clicked.connect(self.image_display)
        self.button_pause = QtWidgets.QPushButton(self.page_speedcards)
        self.button_pause.setGeometry(QtCore.QRect(130, 100, 80, 23))
        self.button_pause.setStyleSheet("color: rgb(255, 255, 255);")
        self.button_pause.setObjectName("button_pause")
        self.button_pause.clicked.connect(self.pause_action)
        self.button_hide_timer = QtWidgets.QPushButton(self.page_speedcards)
        self.button_hide_timer.setGeometry(QtCore.QRect(230, 100, 80, 23))
        self.button_hide_timer.setStyleSheet("color: rgb(255, 255, 255);")
        self.button_hide_timer.setObjectName("button_hide_timer")
        self.button_recall = QtWidgets.QPushButton(self.page_speedcards)
        self.button_recall.setGeometry(QtCore.QRect(330, 100, 80, 23))
        self.button_recall.setStyleSheet("color: rgb(255, 255, 255);")
        self.button_recall.setObjectName("button_recall")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.page_speedcards)
        self.doubleSpinBox.setGeometry(QtCore.QRect(160, 60, 61, 24))
        self.doubleSpinBox.setStyleSheet("background-color: rgb(102, 102, 102);")
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.doubleSpinBox.setMinimum(0)
        self.doubleSpinBox.setDecimals(2)
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
        self.stacked_windows.addWidget(self.page_speedcards)

#========================================================================================

        self.page_5min_nums = QtWidgets.QWidget()
        self.page_5min_nums.setObjectName("page_5min_nums")
        # quit button
        self.button_quit_2 = QtWidgets.QPushButton(self.page_5min_nums)
        self.button_quit_2.setGeometry(QtCore.QRect(210, 50, 131, 23))
        self.button_quit_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.button_quit_2.setObjectName("button_quit_2")
        self.button_quit_2.clicked.connect(self.return_to_main_menu)
        # begin button
        self.button_begin_2 = QtWidgets.QPushButton(self.page_5min_nums)
        self.button_begin_2.setGeometry(QtCore.QRect(30, 50, 80, 23))
        self.button_begin_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.button_begin_2.setObjectName("button_begin_2")
        self.button_begin_2.clicked.connect(self.applet_5min_num)
        # exit button
        self.button_exit_3 = QtWidgets.QPushButton(self.page_5min_nums)
        self.button_exit_3.setGeometry(QtCore.QRect(350, 50, 80, 23))
        self.button_exit_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.button_exit_3.setObjectName("button_exit_3")
        self.button_exit_3.clicked.connect(self.exit_the_app)
        # prev button
        self.button_prev = QtWidgets.QPushButton(self.page_5min_nums)
        self.button_prev.setGeometry(QtCore.QRect(230, 380, 80, 23))
        self.button_prev.setStyleSheet("color: rgb(255, 255, 255);")
        self.button_prev.setObjectName("button_prev")
        # next button
        self.button_next = QtWidgets.QPushButton(self.page_5min_nums)
        self.button_next.setGeometry(QtCore.QRect(340, 380, 80, 23))
        self.button_next.setStyleSheet("color: rgb(255, 255, 255);")
        self.button_next.setObjectName("button_next")
        self.button_next.clicked.connect(self.click_next)
        # pause button
        self.button_pause_2 = QtWidgets.QPushButton(self.page_5min_nums)
        self.button_pause_2.setGeometry(QtCore.QRect(120, 50, 80, 23))
        self.button_pause_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.button_pause_2.setObjectName("button_pause_2")
        self.button_prev.clicked.connect(self.click_prev)
        # lcd watch 
        self.lcdNumber_5min = QtWidgets.QLCDNumber(self.page_5min_nums)
        self.lcdNumber_5min.setGeometry(QtCore.QRect(630, 50, 64, 23))
        self.lcdNumber_5min.setObjectName("lcdNumber_5min")
        # number display panel
        self.disp_5min_panel = QtWidgets.QTextBrowser(self.page_5min_nums)
        self.disp_5min_panel.setGeometry(QtCore.QRect(90, 100, 511, 251))
        self.disp_5min_panel.setObjectName("disp_5min_panel")
        self.disp_5min_panel.setStyleSheet("font: 13.5pt \"Sans Serif\";\n"
"color: rgb(255, 255, 255);")
        self.stacked_windows.addWidget(self.page_5min_nums)

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
            self.button_pause.setText(self._translate("MainWindow","unpause"))
            self.running_applet = not self.running_applet
        else:
            print("Unpausing the applet")
            self.button_pause.setText(self._translate("MainWindow","pause"))
            self.running_applet = not self.running_applet
            self.start_watch()
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

    def return_to_main_menu(self):
        self.watch_reset()
        self.counter = 0
        pixmap = QtGui.QPixmap("card_images/back.png")
        self.card_image.setPixmap(pixmap.scaled(150,300,QtCore.Qt.KeepAspectRatio))
        self.running_applet = False
        print("returning to the main menu")
        self.stacked_windows.setCurrentIndex(0)

    def update_image(self):
        if self.counter < 52 and self.running_applet == True:
            print("counter = " + str(self.counter))
            pic_temp = str(self.images[self.counter])
            pixmap = QtGui.QPixmap(pic_temp)
            print(str(self.images[self.counter]))
            self.card_image.setPixmap(pixmap.scaled(150,300,QtCore.Qt.KeepAspectRatio))
            self.card_image.setObjectName("card_image")
            QtCore.QTimer.singleShot(self.time_step*1260, self.update_image)
            self.counter += 1
        if self.counter == 52:
                self.running_applet = False
                self.stop_watch()
    def image_display(self):
        self.time_step = self.doubleSpinBox.value()
        if self.running_applet == False:
            self.start_watch()
            ranks = [str(n) for n in range(2,11)] + list('JQKA')
            suits = ['S', 'D', 'C', 'H']
            Deck = [rank + suit for suit in suits for rank in ranks]
            
            Cards = random.sample(Deck, 52)
            self.images = []
            img_path = "/home/tvivek/experimental/python_work/fluent_python/card_images/"
            #img_path = "card_images/"
            
            for i in range(52):
                img_name = (Cards[i]+ ".png")
                full_img_loc = img_path + img_name
                self.images = self.images + [full_img_loc]
    
            self.counter = 0
            self.running_applet = True
            self.update_image()

    def showLCD(self):
        text = str(datetime.timedelta(milliseconds=self.watch_counter))[:-3]
        self.lcdNumber.setDigitCount(11)
        if not self.is_watch_reset:  # if "is_watch_reset" is False
            self.lcdNumber.display(text)
        else:
            self.lcdNumber.display('0:00:00.000')

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
        print("displaying the number matrix")
        matr2str = '\n'.join('    '.join('%d' %x for x in y) for y in self.num_matrix[self.counter])
        self.disp_5min_panel.setPlainText(self._translate("main_window",matr2str))

    def click_next(self):
        if self.counter == 10:
            self.button_next.setDisabled(True)
        else:
            self.button_next.setDisabled(False)
            self.counter += 1
            self.display_num_matrix()

    def click_prev(self):
        if self.counter == 0:
            self.button_prev.setDisabled(True)
        else:
            self.button_prev.setDisabled(False)
            self.counter -= 1
            self.display_num_matrix()

    def applet_5min_num(self):
        print("clicked applet 5min num")
        if not self.running_applet:
            print("yo mama")
            self.running_applet = True
            self.num_matrix = np.random.randint(10, size=(10,10,15)) # create a num matrix 15x10x10
            self.start_watch()
            self.counter = 0
            self.display_num_matrix()

#    def hide_timer(self):
        
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
        self.button_begin_2.setText(self._translate("main_window", "begin"))
        self.button_exit_3.setText(self._translate("main_window", "exit"))
        self.button_prev.setText(self._translate("main_window", "prev"))
        self.button_next.setText(self._translate("main_window", "next"))
        self.checkBox.setText(self._translate("main_window", "manual"))
        self.button_pause_2.setText(self._translate("main_window", "pause"))

#========================================================================================

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_main_window()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
