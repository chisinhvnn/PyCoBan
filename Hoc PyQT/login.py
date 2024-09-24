import sys
from PySide6 import QtCore,QtGui,QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QFrame, QWidget
from PySide6.QtCore import QSize
class MainWidown(QMainWindow):
    def __init__(self):
        super().__init__()

        #Đặt tên tiêu đề
        self.setWindowTitle("Đăng nhập")
        #Khai báo Layuot
        main_layuot = QVBoxLayout()
        #Khai báo Widget
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_widget.setLayout(main_layuot)
        #thiết lập kích thước
        self.resize(QSize(400, 300))


        lv1Fame = QFrame()
        lv1Fame.setStyleSheet("background: red;")
        lv2Fame = QFrame()
        lv2Fame.setStyleSheet("background: red;")
        lv3Fame = QFrame()
        lv3Fame.setStyleSheet("background: blue;")

        main_layuot.addWidget(lv1Fame)
        main_layuot.addWidget(lv2Fame)
        main_layuot.addWidget(lv3Fame)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWidown()
    window.show()
    sys.exit(app.exec())
