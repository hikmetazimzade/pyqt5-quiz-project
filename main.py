from PyQt5.QtWidgets import *
import sys
import MainMenu

app = QApplication(sys.argv)
main_menu = MainMenu.Main_Window()
main_menu.showMaximized()
sys.exit(app.exec())