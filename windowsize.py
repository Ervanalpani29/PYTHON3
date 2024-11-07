from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QMainWindow

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.label = QLabel(self)
        self.label.setText("Label")
        self.label.move(200,0)
        self.button = QPushButton(self)
        self.button.setText("Button1")
        self.setGeometry(0,0,400,400)
        self.setWindowTitle("Belajar PyQt5")

app = QApplication([])
window = MyWindow()
window.show()
app.exec()
