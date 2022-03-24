from PySide6 import QtWidgets

class MyWidget(QtWidgets.QWidget):
    
    def __init__(self):
        super().__init__()

        self.button = QtWidgets.QPushButton("Click me!")
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.button)
        

        self.button.clicked.connect(self.magic)

    def magic(self):
        self.button.setText("X")

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    app.exec()