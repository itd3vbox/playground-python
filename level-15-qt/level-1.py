from PySide6 import QtWidgets

class MyWidget(QtWidgets.QWidget):
    
    def __init__(self):
        super().__init__()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    app.exec()