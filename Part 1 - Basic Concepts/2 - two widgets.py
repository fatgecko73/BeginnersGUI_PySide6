from PySide6.QtWidgets import QApplication, QLabel

app = QApplication([])

label1 = QLabel('Welcome to the Pet Shop')
label1.show()

label2 = QLabel('Norwegian Blues For Sale!')
label2.show()

app.exec()

