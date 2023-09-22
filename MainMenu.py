import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from Tests import Test_Number
from ShowResults import ResultWindow
from Background import Backrgound_Window

class Main_Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 200, 800, 800)
        self.setWindowTitle("Main Menu")
        self.setWindowIcon(QIcon('images\main_menu_pic.png'))
        self.setStyleSheet('background:rgb(255, 116, 70)')

        main_button = QPushButton(self)
        main_button.setGeometry(700, 150, 600, 200)
        main_button.setText('Start Test')
        main_button.setFont(QFont('Times', 60))

        main_button.setStyleSheet("QPushButton{\n"
                                  "  background:rgb(51, 49, 127);\n"
                                  "  border:rgb(255, 195, 126);\n"
                                  "  border-radius:20px;\n"
                                  "  color : white;\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton:hover{\n"
                                  "  background:rgb(64, 64, 255);\n"
                                  "  border:2px solid rgb(185, 21, 255);\n"
                                  "}")
        main_button.clicked.connect(self.Main_Button)

        results_button = QPushButton(self)
        results_button.setText('See The Results')
        results_button.setGeometry(700, 450, 600, 200)
        results_button.setFont(QFont('Times', 50))

        results_button.setStyleSheet("QPushButton{\n"
                                  "  background:rgb(51, 49, 127);\n"
                                  "  border:rgb(255, 195, 126);\n"
                                  "  border-radius:20px;\n"
                                  "  color : white;\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton:hover{\n"
                                  "  background:rgb(64, 64, 255);\n"
                                  "  border:2px solid rgb(185, 21, 255);\n"
                                  "}")
        results_button.clicked.connect(self.Result_Button)


        background_button = QPushButton(self)
        background_button.setText('Choose Background Color')
        background_button.setGeometry(700, 750, 600, 200)
        background_button.setFont(QFont('Times', 32))
        background_button.setStyleSheet("QPushButton{\n"
                                  "  background:rgb(51, 49, 127);\n"
                                  "  border:rgb(255, 195, 126);\n"
                                  "  border-radius:20px;\n"
                                  "  color : white;\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton:hover{\n"
                                  "  background:rgb(64, 64, 255);\n"
                                  "  border:2px solid rgb(185, 21, 255);\n"
                                  "}")
        background_button.clicked.connect(self.Background_Button)

        exit_button = QPushButton(self)
        exit_button.setText('Exit Program')
        exit_button.setGeometry(10, 30, 300, 100)
        exit_button.setFont(QFont('Times', 20))
        exit_button.setStyleSheet("QPushButton{\n"
                                  "  background:rgb(51, 49, 127);\n"
                                  "  border:rgb(255, 195, 126);\n"
                                  "  border-radius:20px;\n"
                                  "  color : white;\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton:hover{\n"
                                  "  background:rgb(64, 64, 255);\n"
                                  "  border:2px solid rgb(185, 21, 255);\n"
                                  "}")
        exit_button.clicked.connect(self.ExitProgram)


    def Main_Button(self):
        self.close()
        self.tests = Test_Number()
        self.tests.showMaximized()

    def ExitProgram(self):
        sys.exit()

    def Result_Button(self):
        self.close()
        self.show_results = ResultWindow()
        self.show_results.showMaximized()

    def Background_Button(self):
        self.close()
        self.background = Backrgound_Window()
        self.background.showMaximized()