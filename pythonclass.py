from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QMainWindow

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.label = QLabel("Label", self)
        self.label.setText("label1")
        self.label.move(200, 0)
        self.button = QPushButton(self)
        self.button.setText("button")

app = QApplication([])
window = MyWindow()
window.show()
app.exec()
