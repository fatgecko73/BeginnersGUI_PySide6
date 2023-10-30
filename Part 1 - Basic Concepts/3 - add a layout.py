from PySide6.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout

app = QApplication([])

label1 = QLabel('Welcome to the Pet Shop')

label2 = QLabel('Norwegian Blues For Sale!')
label2.setMinimumWidth(500)

# put the two QLabel objects into a single "layout"
layout = QVBoxLayout()      # vertical box layout - each new widget is added vertically, from top to bottom.
layout.addWidget(label1)     # label1 is added first
layout.addWidget(label2)    # label2 is added vertically below label1

# layouts can't be 'shown' directly, so we must assign the layout to a widget, which can be shown
pet_shop_widget = QWidget()
pet_shop_widget.setLayout(layout)
pet_shop_widget.show()

app.exec()
