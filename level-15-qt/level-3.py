from PySide6 import QtCore, QtWidgets

class GameWindow(QtWidgets.QWidget):
    
    def __init__(self):
        super().__init__()

        layout = QtWidgets.QGridLayout(self)

        label = QtWidgets.QLabel()
        label.setText("Start")
        label.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(label, 0, 1, 1, 3)

        button_1 = QtWidgets.QPushButton("-")
        button_1.clicked.connect(lambda: self.on_token(button_1))
        layout.addWidget(button_1, 1, 1)

        button_2 = QtWidgets.QPushButton("-")
        button_2.clicked.connect(lambda: self.on_token(button_2))
        layout.addWidget(button_2, 1, 2)

        button_3 = QtWidgets.QPushButton("-")
        button_3.clicked.connect(lambda: self.on_token(button_3))
        layout.addWidget(button_3, 1, 3)


        button_4 = QtWidgets.QPushButton("-")
        button_4.clicked.connect(lambda: self.on_token(button_4))
        layout.addWidget(button_4, 2, 1)

        button_5 = QtWidgets.QPushButton("-")
        button_5.clicked.connect(lambda: self.on_token(button_5))
        layout.addWidget(button_5, 2, 2)

        button_6 = QtWidgets.QPushButton("-")
        button_6.clicked.connect(lambda: self.on_token(button_6))
        layout.addWidget(button_6, 2, 3)


        button_7 = QtWidgets.QPushButton("-")
        button_7.clicked.connect(lambda: self.on_token(button_7))
        layout.addWidget(button_7, 3, 1)

        button_8 = QtWidgets.QPushButton("-")
        button_8.clicked.connect(lambda: self.on_token(button_8))
        layout.addWidget(button_8, 3, 2)

        button_9 = QtWidgets.QPushButton("-")
        button_9.clicked.connect(lambda: self.on_token(button_9))
        layout.addWidget(button_9, 3, 3)

        button_reset = QtWidgets.QPushButton("Reset")
        button_reset.clicked.connect(lambda: self.on_reset(button_reset))
        layout.addWidget(button_reset, 4, 1)

        button_print = QtWidgets.QPushButton("🖨")
        button_print.clicked.connect(lambda: self.on_reset(button_print))
        layout.addWidget(button_print, 4, 2)

        on_ai = QtWidgets.QPushButton("💿")
        on_ai.clicked.connect(lambda: self.on_ai(on_ai))
        layout.addWidget(on_ai, 4, 3)

    def on_token(self, button):
        if button.text() == "X":
            button.setText("0")
        else:
            button.setText("X")

    def on_reset(self, button):
        pass

    def on_print(self, button):
        pass

    def on_ai(self, button):
        pass

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = GameWindow()
    widget.show()

    app.exec()