from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QMainWindow, QSizePolicy, QLayout
from PySide6.QtCore import Qt

app = QApplication()

# Step 1a
# QMainWindow is a special widget that has useful features for the main window of an application.  These
# includes a status bar, menu bar, tool bar, docking widgets and other features.  We're not using those
# features in this simple app, but it's important to know they are there.
main_window = QMainWindow()

# Step 1b
# the QMainWindow class has a special CentralWidget attribute - it is the widget that contains most of your
# app's main widgets/layouts.  The CentralWidget can be any type of widget - we're just going to use the
# generic QWidget object as our CentralWidget, and then add other widgets inside that widget's layout.
central_widget = QWidget()
main_window.setCentralWidget(central_widget)

# Step 1c
# we can now create the widget(s) we want to add inside the central widget. Let's start with our Pet Shop Sign...
pet_shop_sign = QLabel('Bolton Pet Shop')
# ... and customise it using some of the attributes we learned in the previous module
changed_font = pet_shop_sign.font()
changed_font.setBold(True)
changed_font.setPointSize(48)
changed_font.setFamily('Calisto MT')
pet_shop_sign.setFont(changed_font)
pet_shop_sign.setStyleSheet("border: 2px solid #333333;"
                            "color: #773377;"
                            "background-color: #B2EBF2;"
                            "padding: 20px;")
pet_shop_sign.adjustSize()


# # Step 4
# # now let's add the widget to a layout object which will be applied to the CentralWidget.
# # The hierarchy of widgets and layouts can get confusing - can you write out the hierarchy we're creating here?
# pet_shop_layout = QVBoxLayout()
# pet_shop_layout.addWidget(pet_shop_sign)
# central_widget.setLayout(pet_shop_layout)
# # what happened to our widget?!


# # Step 5
# # we need to manage how the widget size behaves, using the setSizePolicy function.
# # the size policy of a widget affects how a widget behaves when its parent layout is resized.  The size policy
# # uses the "sizeHint" property of the widget, which contains the preferred dimensions of the widget (as
# # calculated automatically by PySide6).  You can't directly set the sizeHint size.
#
# # Available size policies include:
# # Fixed - the widget size does not change irrespective of the size of the parent layout
# # Ignored - the widget size ignores the sizeHint and will just fill all available space
# # Minimum - widgets will maintain its sizeHint as a minimum, but will expand if extra layout space is available
# # Maximum - widgets will maintain its sizeHint as a maximum, but will shrink if extra layout space is available
# # Preferred - the widget can shrink or grow bigger than its set size (default)
# # Other options include Expanding and MinimumExpanding. Some difference between these policies only become apparent
# # where multiple widgets are competing in a single layout
# pet_shop_sign.setSizePolicy(QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed))


# # Step 6
# # we want to align our pet shop sign to the middle top of the layout
# # Note that alignment is set on the layout object, not the widget.
# pet_shop_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)

# maximise the main window so it fills the screen space
main_window.showMaximized()

main_window.show()
app.exec()
