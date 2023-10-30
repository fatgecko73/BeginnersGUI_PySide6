from PySide6.QtWidgets import QApplication, QLabel
from PySide6.QtCore import Qt


app = QApplication()
pet_shop_sign = QLabel('Bolton Pet Shop')

# # 1 - change the font style
# changed_font = pet_shop_sign.font()
# changed_font.setBold(True)
# changed_font.setPointSize(48)
# changed_font.setFamily('Calisto MT')
# pet_shop_sign.setFont(changed_font)

# # 2 - change the font colour  (actually, the foreground colour)
# pet_shop_sign.setStyleSheet(f'color: #ffe170;')

# # 3 - change the background colour
# pet_shop_sign.setStyleSheet(f'background-color: #485d78;')   # (Oops, we lost something!)

# # 4 - change background and foreground colour
# pet_shop_sign.setStyleSheet(f'color: #ffe170;'
#                             f'background-color: #485d78;')

# # 5 - add a bit of space (padding) around the edge
# pet_shop_sign.setStyleSheet(f'color: #ffe170;'
#                             f'background-color: #485d78;'
#                             f'padding: 20px')

# # 6 - add a border
# pet_shop_sign.setStyleSheet("border: 2px solid #ffe170;"
#                             "color: #ffe170;"
#                             "background-color: #485d78;"
#                             "padding: 20px;")

# # 7 - change the size of the widget
# pet_shop_sign.setFixedWidth(300)      # we'll talk more about sizing in the next module
# pet_shop_sign.setFixedHeight(80)

# # 8 - Autosize the widget!
# pet_shop_sign.adjustSize()

# # 9 - reposition the widget
# pet_shop_sign.move(200, 200)    # moves the widget to the x, y location specified

# # 10 - make frameless
# pet_shop_sign.setWindowFlags(Qt.WindowType.FramelessWindowHint)

# # 11 - add a tooltip
# pet_shop_sign.setToolTip('Welcome to the Bolton Pet Shop')

# # 12 - change the displayed text
# pet_shop_sign.setText('The Ipswich Pet Shop')    # Oops something's not right! What do we need to add?


pet_shop_sign.show()
app.exec()
