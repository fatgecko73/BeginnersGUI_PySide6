# As an exercise, build your own feedback widget using PySide6, with these features:
# 1. Allow the user to select the type of feedback from a drop down menu (QComboBox) - e.g. 'My pet is not well'
# 2. Allow the user to enter comments (QTextEdit)
# 3. Add a button for the user to submit their feedback (QPushButton)
# 4. If you're feeling confident, add a pop up message when the user clicks the button (QMessageBox - you might need
# to google how it works)


from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout


class FeedbackTab(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        # Delete the code below, and write your own feedback form

        # create the widgets
        self.placeholder = QLabel("This tab is for providing feedback")

        # set the layout
        layout = QVBoxLayout()
        layout.addWidget(self.placeholder)
        self.setLayout(layout)
