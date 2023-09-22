import sys
from datetime import datetime

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from random import choice
from PyQt5.QtCore import QTimer

seconds = 0
test_number = 0


with open("data/tests.txt", mode ='r', encoding ='utf-8') as file:
    testler = file.readlines()
    quiz = [i for i in range(0, len(testler), 6)]

length = len(quiz)

class Test_Number(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TestNumber")
        self.setWindowIcon(QIcon("images\exam_background1.jpg"))
        self.setStyleSheet('background:rgb(212, 201, 255)')


        self.question_number = QLineEdit(self)
        self.question_number.setValidator(QIntValidator())
        self.question_number.setGeometry(750, 450, 300, 100)
        self.question_number.setFont(QFont('Times', 20))
        self.question_number.setStyleSheet("  background:rgb(222, 237, 255);\n"
                                "  border:2px solid rgb(122, 14, 255);\n"
                                "  border-radius:20px;\n"
                                "  color : black;\n")

        with open('data/answers.txt', mode ='r', encoding ='utf-8') as answers:
            self.test_length = len(answers.readlines())


        question_label = QLabel(self)
        question_label.setGeometry(650, 300, 1500, 100)
        question_label.setText('Input Test Number:')
        question_label.setFont(QFont('Times', 40))


        accept_button = QPushButton(self)
        accept_button.setGeometry(1100, 450, 200, 100)
        accept_button.setText("Confirm")
        accept_button.setFont(QFont('Times', 20))
        accept_button.setStyleSheet("QPushButton{\n"
                      "  background:rgb(64, 179, 255);\n"
                      "  border:rgb(112, 167, 255);\n"
                      "  border-radius:20px;\n"
                      "  color : white;\n"
                      "}\n"
                      "\n"
                      "QPushButton:hover{\n"
                      "  background:rgb(121, 179, 255);\n"
                      "  border:2px solid rgb(185, 21, 255);\n"
                      "}")
        accept_button.clicked.connect(self.AcceptButtonClicked)

    def AcceptButtonClicked(self):
        global test_number
        if self.question_number.text() == '':
            message_box = QMessageBox()
            message_box.setIcon(QMessageBox.Information)

            message_box.setText("Input Test Number!")
            message_box.setWindowTitle("Information MessageBox")
            message_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

            retval = message_box.exec_()

        test_number = int(self.question_number.text())
        if 0 < test_number <= self.test_length:
            self.close()
            self.Test_Window = Test_Window()
            self.Test_Window.showMaximized()

        else:
            message_box = QMessageBox()
            message_box.setIcon(QMessageBox.Information)

            message_box.setText(f"There are {self.test_length} tests in exam!")
            message_box.setWindowTitle("Information MessageBox")
            message_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

            retval = message_box.exec_()


class Test_Window(QWidget):
    def __init__(self):
        super().__init__()
        global seconds
        global quiz
        self.correct = 0
        self.wrong = 0

        self.resize(900, 500)
        with open(r'data\background.txt.', 'r') as background:
            self.setStyleSheet(f'background:{background.read()}')
        self.setWindowTitle("Quiz")

        self.setWindowIcon(QIcon("images\exam_background1.jpg"))
        testler = open("data/tests.txt", "r", encoding ="utf-8").readlines()
        self.question = QLabel(self)
        self.variant_a = QPushButton(self)
        self.variant_a.move(620, 400)

        self.variant_b = QPushButton(self)
        self.variant_b.move(620, 500)

        self.variant_c = QPushButton(self)
        self.variant_c.move(620, 600)

        self.variant_d = QPushButton(self)
        self.variant_d.move(620, 700)

        self.variant_e = QPushButton(self)
        self.variant_e.move(620, 800)

        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.updateTimer)

        self.minutes = 0
        self.hours = 0

        self.label = QLabel(self)
        self.label.setText("00:00:00")
        self.label.setGeometry(870, 0, 400, 300)


        self.label.setFont(QFont('Times', 40))


        self.chosen_number = choice(quiz)
        quiz.remove(self.chosen_number)

        self.max_size = 0
        for k in testler[self.chosen_number : self.chosen_number + 6]:
            self.max_size = max(self.max_size, len(k))

        for i in testler[self.chosen_number : self.chosen_number + 6]:
            if i[0] == "A" and i[1] == ')':
                self.SetButton(self.variant_a, i)

            elif i[0] == "B" and i[1] == ')':
                self.SetButton(self.variant_b, i)


            elif i[0] == "C" and i[1] == ')':
                self.SetButton(self.variant_c, i)


            elif i[0] == "D" and i[1] == ')':
                self.SetButton(self.variant_d, i)


            elif i[0] == "E" and i[1] == ')':
                self.SetButton(self.variant_e, i)

            else:
                self.question.setGeometry(500, 300, 1500, 100)
                self.question.setText(i)
                self.question.setFont(QFont('Times', 20))


        self.variant_a.clicked.connect(self.ChangeText)
        self.variant_b.clicked.connect(self.ChangeText)
        self.variant_c.clicked.connect(self.ChangeText)
        self.variant_d.clicked.connect(self.ChangeText)
        self.variant_e.clicked.connect(self.ChangeText)


    def SetButton(self, button, i):
        button.setText(i)
        button.setFont(QFont('Times', 20))
        button.adjustSize()
        button.setStyleSheet("QPushButton{\n"
                                "  background:rgb(122, 14, 255);\n"
                                "  border:2px solid rgb(122, 14, 255);\n"
                                "  border-radius:20px;\n"
                                "  color : white;\n"
                                "}\n"
                                "\n"
                                "QPushButton:hover{\n"
                                "  background:rgb(185, 21, 255);\n"
                                "  border:2px solid rgb(185, 21, 255);\n"
                                "}")

        #button.resize(self.max_size + 700, button.height())
        button.resize(self.max_size * 10 + 150, button.height())


    def updateTimer(self):
        global seconds
        seconds += 1

        self.hours = (seconds // 3600)
        self.minutes = (seconds // 60) % 60

        seconds_string = str(seconds % 60)
        minutes_string = str(self.minutes)
        hours_string = str(self.hours)

        if seconds % 60 < 10 : seconds_string = '0' + seconds_string
        if self.minutes < 10 : minutes_string = '0' + minutes_string
        if self.hours < 10 : hours_string = '0' + hours_string

        self.label.setText(hours_string + ':' + minutes_string + ':' + seconds_string)


    def ChangeText(self):
        global quiz
        global length
        global test_number

        self.clicked_button = self.sender()
        with open('data/answers.txt', 'r', encoding ='utf8') as answers:
            answers_r = answers.readlines()
            if self.clicked_button.text() == answers_r[self.chosen_number // 6]:
                self.clicked_button.setStyleSheet('background:green')
                self.correct += 1
                correct_timer = QTimer(self)
                correct_timer.start(1000)
                correct_timer.timeout.connect(self.Set_Text)

            else:
                self.clicked_button.setStyleSheet('background:red')
                for k in [self.variant_a, self.variant_b, self.variant_c, self.variant_d, self.variant_e]:
                    if k.text() in answers_r:
                        k.setStyleSheet('background:green')

                self.wrong += 1
                wrong_timer = QTimer(self)
                wrong_timer.start(7000)
                wrong_timer.timeout.connect(self.Set_Text)

        if length - test_number == len(quiz):
            with open('data/results.txt', 'a', encoding ='utf-8') as results:
                today = datetime.now()
                results.write(f'{self.correct} Correct {self.wrong} Wrong {str(today)[:-7]}\n')

            sys.exit()

        self.chosen_number = choice(quiz)
        quiz.remove(self.chosen_number)


        self.max_size = 0
        for k in testler[self.chosen_number: self.chosen_number + 6]:
            self.max_size = max(self.max_size, len(k))


    def Set_Text(self):
        for i in testler[self.chosen_number : self.chosen_number + 6]:
            if i[0] == "A" and i[1] == ')':
                self.SetButton(self.variant_a, i)

            elif i[0] == "B" and i[1] == ')':
                self.SetButton(self.variant_b, i)

            elif i[0] == "C" and i[1] == ')':
                self.SetButton(self.variant_c, i)


            elif i[0] == "D" and i[1] == ')':
                self.SetButton(self.variant_d, i)


            elif i[0] == "E" and i[1] == ')':
                self.SetButton(self.variant_e, i)

            else:
                self.question.setText(i)