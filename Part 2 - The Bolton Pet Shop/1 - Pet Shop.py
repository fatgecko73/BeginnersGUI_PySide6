from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLabel, QComboBox, QCheckBox, QPushButton,
                               QLineEdit, QRadioButton, QSlider, QProgressBar, QMessageBox, QMainWindow, QGroupBox,
                               QTabWidget, QSizePolicy, QGraphicsDropShadowEffect)
from PySide6.QtCore import Qt
from tab_buy_a_pet import BuyAPet
from tab_pet_tag import PetTag


class ShopSign(QLabel):

    def __init__(self):
        super().__init__()

        self.setText('Bolton Pet Shop')
        changed_font = self.font()
        changed_font.setBold(True)
        changed_font.setPointSize(48)
        changed_font.setFamily('Calisto MT')
        self.setFont(changed_font)
        self.setStyleSheet("border: 3px solid #ffe170;"
                           "color: #ffe170; "
                           "background-color: #485d78;"
                           "padding: 20px;")
        self.adjustSize()
        self.setSizePolicy(QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed))


class BoltonPetShop(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)

        # Step 1 - Setup

        #  set parameters for the QMainWindow
        self.setWindowTitle("Pet Shop")

        # This time we will use a QTabWidget for as the CentralWidget for the QMainWindow
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        central_layout = QVBoxLayout()
        central_widget.setLayout(central_layout)

        # Create our shop sign, using all our previous customisations.  But this time we are calling our custom class
        # created above.
        pet_shop_sign = ShopSign()
        central_layout.addWidget(pet_shop_sign)

        # Step 2 - Create Tabs
        tab_widget = QTabWidget()
        tab1_label = QLabel('\nTab for buying pets\n')
        tab2_label = QLabel('\nTab for designing pet tags\n')
        tab3_label = QLabel('\nTab for providing feedback\n')

        tab1_widget = BuyAPet()
        tab2_widget = PetTag()

        tab_widget.addTab(tab1_widget, "Buy a Pet")
        tab_widget.addTab(tab2_widget, "Design a Pet Tag")
        tab_widget.addTab(tab3_label, "Feedback")

        central_layout.addSpacing(30)
        central_layout.addWidget(tab_widget)

        tab2_widget = QLabel('\nTab for designing pet tags\n')
        tab3_widget = QLabel('\nTab for providing feedback\n')

# # Create widgets to include in the app
# pet_type = QLabel('Select your pet:')
# pet_combobox = QComboBox()
# pet_combobox.addItems(['Dog', 'Cat', 'Fish', 'Bird', 'Norwegian Blue'])
#
# extras_group_box = QGroupBox('Extras')
# toy_checkbox = QCheckBox("Include Toy ($50)")
# treat_checkbox = QCheckBox("Include Treats ($30)")
# quantity_label = QLabel('Order Food:')
# quantity_slider = QSlider()
# quantity_slider.setOrientation(Qt.Orientation.Horizontal)  # Vertical orientation
# quantity_slider.setTickPosition(QSlider.TickPosition.TicksAbove)
# quantity_slider.setRange(1, 10)
#
# price_label = QLabel("Total Price: $0")
#
# calc_button = QPushButton('Calculate Total')
# calc_button.clicked.connect(calculate_total)
# payment_label = QLabel('Select Payment Method:')
# payment_radio_group = QWidget()
# credit_card_radio = QRadioButton("Credit Card")
# paypal_radio = QRadioButton("PayPal")
#
# # Progress bar
# progress_label = QLabel('Order Progress:')
# progress_bar = QProgressBar()
# progress_bar.setValue(0)
#
# # create the layout for the central widget
#
# extras_group_box_layout = QVBoxLayout()
#
# payment_layout = QVBoxLayout()
# payment_layout.addWidget(credit_card_radio)
# payment_layout.addWidget(paypal_radio)
# payment_radio_group.setLayout(payment_layout)
#
# layout = QVBoxLayout()
# layout.addWidget(pet_type)
# layout.addWidget(pet_combobox)
# layout.addWidget(toy_checkbox)
# layout.addWidget(treat_checkbox)
# layout.addWidget(price_label)
# layout.addWidget(calc_button)
# layout.addWidget(payment_label)
# layout.addWidget(payment_radio_group)
# layout.addWidget(quantity_label)
# layout.addWidget(quantity_slider)
# layout.addWidget(progress_label)
# layout.addWidget(progress_bar)
#
# central_widget.setLayout(layout)
#
# def calculate_total(self):
#     pet = pet_combobox.currentText()
#     toy = toy_checkbox.isChecked()
#     treat = treat_checkbox.isChecked()
#
#     total_price = pet_price[pet]
#     if toy:
#         total_price += 50
#     if treat:
#         total_price += 30
#
#     price_label.setText(f"Total Price: ${total_price}")


if __name__ == '__main__':
    app = QApplication()
    app.setStyle('Fusion')   # Fusion, Windows, Macintosh
    shop = BoltonPetShop()
    shop.show()
    app.exec()
