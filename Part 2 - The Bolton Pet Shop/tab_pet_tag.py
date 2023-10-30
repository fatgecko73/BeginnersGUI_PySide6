from PySide6.QtWidgets import (QWidget, QLineEdit, QFontDialog, QComboBox, QFormLayout, QApplication, QPushButton,
                               QColorDialog, QLabel, QVBoxLayout, QHBoxLayout, QSizePolicy)
from PySide6.QtGui import QColor
from PySide6.QtCore import Qt


class PetTag(QWidget):  # we are subclassing the QWidget class - i.e. creating our own customised widget.

    def __init__(self, parent=None):  # this function is called whenever an instance of the PetTag class is created.

        super().__init__(parent)  # initiates the QWidget baseclass.

        # define widgets
        self.pet_name = QLineEdit()
        self.tag_material = QComboBox()
        self.tag_material.addItems(['Steel', 'Plastic', 'Gold Plated'])
        self.tag_font_button = QPushButton('Tag Font')
        self.tag_colour_button = QPushButton('Tag Colour')
        self.tag_display = QLabel("Enter your pet's name")
        self.tag_display.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # connect some widgets to specific actions (functions) when the widgets are changed by the user
        self.pet_name.textChanged.connect(lambda: self.tag_display.setText(self.pet_name.text()))
        self.tag_font_button.clicked.connect(self.choose_font)
        self.tag_colour_button.clicked.connect(self.choose_colour)

        # create the layout for the widgets
        form_layout = QFormLayout()
        form_layout.addRow('Pet Name', self.pet_name)
        form_layout.addRow('Material', self.tag_material)

        button_layout = QVBoxLayout()
        button_layout.addWidget(self.tag_font_button)
        button_layout.addWidget(self.tag_colour_button)

        inputs_layout = QHBoxLayout()
        inputs_layout.addLayout(form_layout)
        inputs_layout.addLayout(button_layout)

        global_layout = QVBoxLayout()
        global_layout.addLayout(inputs_layout)
        global_layout.addWidget(self.tag_display)

        self.setLayout(global_layout)

        # size policies
        self.pet_name.setSizePolicy(QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed))
        self.tag_material.setSizePolicy(QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed))

    def choose_font(self):
        # called when the user clicks the "Tag Font" button
        ok, font = QFontDialog.getFont()
        if ok:
            self.tag_display.setFont(font)

    def choose_colour(self):
        # called when the user clicks the "Tag Colour" button
        colour = QColorDialog.getColor()
        if colour.isValid():
            self.tag_display.setStyleSheet(f'background-color: {colour.name()};')


if __name__ == '__main__':
    app = QApplication()
    pt = PetTag()
    pt.show()
    app.exec()
