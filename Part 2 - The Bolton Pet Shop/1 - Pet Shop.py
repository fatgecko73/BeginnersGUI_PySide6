from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLabel, QMainWindow, QTabWidget, QSizePolicy)
from tab_buy_a_pet import BuyAPet
from tab_pet_tag import PetTag
from tab_feedback import FeedbackTab


class ShopSign(QLabel):

    def __init__(self, parent=None):
        super().__init__(parent)

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

        tab1_widget = BuyAPet()
        tab2_widget = PetTag()
        tab3_widget = FeedbackTab()

        tab_widget.addTab(tab1_widget, "Buy a Pet")
        tab_widget.addTab(tab2_widget, "Design a Pet Tag")
        tab_widget.addTab(tab3_widget, "Feedback")

        central_layout.addSpacing(30)
        central_layout.addWidget(tab_widget)


if __name__ == '__main__':
    app = QApplication()
    app.setStyle('Fusion')   # Fusion, Windows, Macintosh
    shop = BoltonPetShop()
    shop.show()
    app.exec()
