# import sys 
# from PyQt5 import uic
# from PyQt5.QtWidgets import QApplication

# Form, Window = uic.loadUiType("dialog.ui")

# app = QApplication([])
# #app.enterInputFilePushButton.clicked.connect(app.browse_folder)
# window = Window()
# form = Form()

# form.setupUi(window)
# window.show()

# app.exec()


from inspect import _void
import sys  # sys нужен для передачи argv в QApplication
import os  # Отсюда нам понадобятся методы для отображения содержимого директорий

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QLabel, QApplication)
from PyQt5.QtGui import QPixmap


import dialog  # Это наш конвертированный файл дизайна
import graphwindow

class SecondWindow(QtWidgets.QWidget):
    def __init__(self, parent=None): #если собрался передавать аргументы, то не забудь их принять (nameofargument, self, parent=None)
        super().__init__(parent, QtCore.Qt.Window)
        self.build() #ну и передать в открывающееся окно соответственно (nameofargument, self)
        self.load_image("pic1.jpg")
        #self.closeButton.clicked.connect(self.closeWin)
        
    def build(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Graphics')  

    def load_image(self, file_name):
        pixmap = QPixmap(file_name)

        self.label = QLabel(self)
        self.label.setPixmap(pixmap)
        self.label.resize(pixmap.width(), pixmap.height())

        self.resize(pixmap.width(), pixmap.height())

    def closeWin(self):
        self.close()

class ThirdWindow(QtWidgets.QWidget):
    def __init__(self, parent=None): #если собрался передавать аргументы, то не забудь их принять (nameofargument, self, parent=None)
        super().__init__(parent, QtCore.Qt.Window)
        self.build() #ну и передать в открывающееся окно соответственно (nameofargument, self)
        self.load_image("pic2.jpg")
        #self.closeButton.clicked.connect(self.closeWin)
        
    def build(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Graphics')  

    def load_image(self, file_name):
        pixmap = QPixmap(file_name)

        self.label = QLabel(self)
        self.label.setPixmap(pixmap)
        self.label.resize(pixmap.width(), pixmap.height())

        self.resize(pixmap.width(), pixmap.height())

    def closeWin(self):
        self.close()


class ExampleApp(QtWidgets.QDialog, dialog.Ui_Dialog):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        plan = self.enterInputFilePushButton.clicked.connect(self.browse_file)  # Выполнить функцию browse_folder
        postavki=self.enterInputFilePushButton_2.clicked.connect(self.browse_file_2)
        self.prognosButton.clicked.connect(self.openWin)
        self.closeButton.clicked.connect(self.closeWin)

    def openWin(self):
        self.secondWin = SecondWindow(self) #здесь можешь передавать аргументы во второе окно (nameofargument, self) 
        self.thirdWin = ThirdWindow(self) #здесь можешь передавать аргументы во второе окно (nameofargument, self) 
        self.secondWin.show()  
        self.thirdWin.show()  

    def closeWin(self):
        self.close()

    def browse_file(self):
        input_file = QtWidgets.QFileDialog.getOpenFileName(self, "Выберите файл")
        if (len(str(input_file))>0):
            self.fileName.setText(str(input_file)[2:len(str(input_file))-19:])
            return input_file
        
    def browse_file_2(self):
        input_file = QtWidgets.QFileDialog.getOpenFileName(self, "Выберите файл")
        if (len(str(input_file))>0):
            self.fileName_2.setText(str(input_file)[2:len(str(input_file))-19:])
            return input_file
    
def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
    