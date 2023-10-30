from PySide6.QtWidgets import (QWidget, QLabel, QComboBox, QCheckBox, QSlider, QGroupBox, QVBoxLayout, QPushButton,
                               QSizePolicy, QHBoxLayout)
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap


# Exercises:
# 1. Modify the code to update the total price automatically so the user doesn't need to click the "Update Price" button
# 2. When pet food is 10kg, the 'Extras' box size changes dimensions slightly - update the code to prevent this 'glitch'


class BuyAPet(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        # price data
        self.pet_price = {'Dog': 1000, 'Cat': 800, 'Fish': 50, 'Bird': 200, 'Norwegian Blue': 2000}

        # create our widgets
        self.pet_type = QLabel('Select your pet:')
        self.pet_combobox = QComboBox()
        self.pet_combobox.addItems(['Dog', 'Cat', 'Fish', 'Bird', 'Norwegian Blue'])
        self.pet_combobox.currentTextChanged.connect(self.update_animal)

        extras_group_box = QGroupBox('Extras')
        self.toy_checkbox = QCheckBox("Include Toy ($50)")
        self.treat_checkbox = QCheckBox("Include Treats ($30)")
        self.quantity_label = QLabel('Pet Food ($10/kg):')
        self.quantity_slider = QSlider()
        self.quantity_slider.setOrientation(Qt.Orientation.Horizontal)  # Vertical orientation
        self.quantity_slider.setTickPosition(QSlider.TickPosition.TicksAbove)
        self.quantity_slider.setRange(0, 10)
        self.quantity_slider.valueChanged.connect(self.update_food_kg)

        # calculate price
        self.calculate_price = QPushButton('Update Price')
        self.calculate_price.clicked.connect(self.update_price)

        self.price_label = QLabel("Total Price: $0")

        # animal image
        pix_map = QPixmap('images/dog.png')
        pix_map = pix_map.scaledToHeight(200)
        self.animal_image = QLabel('Image')
        self.animal_image.setPixmap(pix_map)

        # set up layout
        extras_group_box_layout = QVBoxLayout()
        extras_group_box_layout.addWidget(self.toy_checkbox)
        extras_group_box_layout.addWidget(self.treat_checkbox)
        extras_group_box_layout.addWidget(self.quantity_label)
        extras_group_box_layout.addWidget(self.quantity_slider)
        extras_group_box.setLayout(extras_group_box_layout)

        order_details_layout = QVBoxLayout()
        order_details_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        order_details_layout.addWidget(self.pet_type)
        order_details_layout.addWidget(self.pet_combobox)
        order_details_layout.addWidget(extras_group_box)
        order_details_layout.addWidget(self.calculate_price)
        order_details_layout.addWidget(self.price_label)

        main_layout = QHBoxLayout()
        main_layout.addLayout(order_details_layout)
        main_layout.addWidget(self.animal_image)

        self.setLayout(main_layout)

        # size policy
        self.pet_combobox.setSizePolicy(QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed))
        self.calculate_price.setSizePolicy(QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed))
        extras_group_box.setSizePolicy(QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed))

    def update_price(self):
        pet = self.pet_combobox.currentText()
        toy = self.toy_checkbox.isChecked()
        treat = self.treat_checkbox.isChecked()

        total_price = self.pet_price[pet]
        if toy:
            total_price += 50
        if treat:
            total_price += 30

        total_price += self.quantity_slider.value() * 10

        self.price_label.setText(f"Total Price: ${total_price}")

    def update_food_kg(self):
        self.quantity_label.setText(f'Pet Food ($10/kg): {self.quantity_slider.value()} kg')

    def update_animal(self):
        if self.pet_combobox.currentText() == 'Dog':
            pix_map = QPixmap('images/dog.png')
        elif self.pet_combobox.currentText() == 'Cat':
            pix_map = QPixmap('images/kitten.png')
        elif self.pet_combobox.currentText() == 'Fish':
            pix_map = QPixmap('images/fish.png')
        elif self.pet_combobox.currentText() == 'Bird':
            pix_map = QPixmap('images/bird.png')
        elif self.pet_combobox.currentText() == 'Norwegian Blue':
            pix_map = QPixmap('images/NorwegianBlue.png')
        else:
            self.animal_image.hide()
            return

        if pix_map:
            self.animal_image.show()
            pix_map = pix_map.scaledToHeight(200)
            self.animal_image.setPixmap(pix_map)

