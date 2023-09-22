from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QFont
import MainMenu

class ResultWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(800, 200, 600, 600)
        self.setStyleSheet('background:rgb(236, 213, 255)')
        self.setWindowTitle('Results')
        self.setWindowIcon(QIcon(r'images\results.png'))

        with open('data/results.txt', mode ='r', encoding ='utf-8') as file:
            results = file.readlines()

        if len(results) == 0:
            info = QLabel(self)
            info.setGeometry(600, 300, 900, 150)
            info.setText('History Is Empty')
            info.setFont(QFont('Times', 70))


        else:
            label = QLabel(self)
            label.setText('Exam Results:')
            label.setFont(QFont('Times', 40))
            label.setGeometry(800, 120, 600, 150)
            result_number = len(results)

            y = 300
            for k in range(result_number):
                result_label = QLabel(self)
                result_label.setText(str(k + 1) + "- " + results[k])
                result_label.setFont(QFont('Times', 25))
                result_label.setGeometry(800, y, 1000, 150)
                y += 100

            delete_history = QPushButton(self)
            delete_history.setGeometry(10, 160, 300, 100)
            delete_history.setText('Delete History')
            delete_history.setFont(QFont('Times', 20))
            delete_history.setStyleSheet("QPushButton{\n"
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

            delete_history.clicked.connect(self.DeleteHistory)

        back_button = QPushButton(self)
        back_button.setText('Back To Main Menu')
        back_button.setGeometry(10, 30, 300, 100)
        back_button.setFont(QFont('Times', 20))
        back_button.setStyleSheet("QPushButton{\n"
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
        back_button.clicked.connect(self.BackButton)

    def BackButton(self):
        self.close()
        self.main_menu = MainMenu.Main_Window()
        self.main_menu.showMaximized()


    def DeleteHistory(self):
        open('data/results.txt', mode ='w', encoding ='utf-8').close()
        self.close()
        self.main_menu = MainMenu.Main_Window()
        self.main_menu.showMaximized()