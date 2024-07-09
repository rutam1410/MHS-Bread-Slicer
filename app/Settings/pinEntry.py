import os
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QGridLayout, QMessageBox, QLabel
from PyQt6.QtGui import QFont, QIcon, QPixmap
from PyQt6.QtCore import Qt, QSize

class PinEntry(QWidget):
    def __init__(self, parent=None, main_window=None):
        super().__init__(parent)
        self.main_window = main_window
        
        # Define paths to resources
        res_dir = os.path.join(os.path.dirname(__file__), '..', 'res', 'icon')

        # Main layout for the page
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        # Top bar layout for the back button and heading label
        top_bar_layout = QHBoxLayout()
        top_bar_layout.setContentsMargins(20, 10, 10, 10)
        main_layout.addLayout(top_bar_layout)

        # Back button
        back_icon_path = os.path.join(res_dir, 'back.png')
        back_pixmap = QPixmap(back_icon_path)
        back_icon = QIcon(back_pixmap)

        self.back_button = QPushButton()
        self.back_button.setIcon(back_icon)
        self.back_button.setIconSize(QSize(75, 60))  # Reduced size for the back button
        self.back_button.setStyleSheet(
            "QPushButton {"
            "   background-color: transparent;"
            "   border: none;"
            "}"
            "QPushButton:hover {"
            "   background-color: rgba(150, 150, 150, 0.5);"  # Light grey with some transparency
            "}"
        )
        self.back_button.clicked.connect(self.on_back_button_clicked)
        top_bar_layout.addWidget(self.back_button, alignment=Qt.AlignmentFlag.AlignLeft)

        # Add a smaller spacer to reduce the gap between the back button and heading label
        top_bar_layout.addSpacing(20)

        # Heading label
        self.heading_label = QLabel("Enter PIN", self)
        self.heading_label.setStyleSheet("font-size: 36px; font-weight: bold; color: black;")
        self.heading_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        top_bar_layout.addWidget(self.heading_label, alignment=Qt.AlignmentFlag.AlignCenter)

        # Add another smaller spacer to balance the layout
        top_bar_layout.addSpacing(262)

        # Inner layout for main content
        inner_layout = QVBoxLayout()
        inner_layout.setContentsMargins(270, 10, 270, 20)  # Add margins around the layout
        inner_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addLayout(inner_layout)

        # Add spacing between the heading and the pin display
        inner_layout.addSpacing(10)

        self.pin_display = QLineEdit(self)
        self.pin_display.setFont(QFont("Arial", 28))
        self.pin_display.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.pin_display.setEchoMode(QLineEdit.EchoMode.Password)
        self.pin_display.setReadOnly(True)
        self.pin_display.setStyleSheet("background-color: white; color: black;")
        inner_layout.addWidget(self.pin_display)

        # Add spacing between the pin display and the grid layout
        inner_layout.addSpacing(10)

        grid_layout = QGridLayout()
        grid_layout.setSpacing(10)  # Add spacing between buttons
       
        buttons = [
            ('1', 0, 0), ('2', 0, 1), ('3', 0, 2),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2),
            ('C', 3, 0), ('0', 3, 1), ('OK', 3, 2),
        ]

        button_size = QSize(60, 60)  # Define the fixed size for buttons

        for btn_text, x, y in buttons:
            button = QPushButton(btn_text)
            button.setFont(QFont("Arial", 20))
            button.setStyleSheet("background-color: white; color: black; border: 2px solid #555555;")
            button.setFixedSize(button_size)
            button.clicked.connect(self.on_button_click)
            grid_layout.addWidget(button, x, y, Qt.AlignmentFlag.AlignCenter)

        inner_layout.addLayout(grid_layout)

        # Add spacing between the grid layout and the bottom of the inner layout
        inner_layout.addSpacing(10)

        # Predefined PIN and attempts variables
        self.predefined_pin = "8888"
        self.attempts = 0
        self.max_attempts = 3

    def on_back_button_clicked(self):
        if self.main_window:
            self.main_window.navigate_to_page_one()
            self.close()

    def on_button_click(self):
        sender = self.sender()
        text = sender.text()

        if text == 'C':
            self.pin_display.setText(self.pin_display.text()[:-1])
        elif text == 'OK':
            entered_pin = self.pin_display.text()
            if entered_pin == self.predefined_pin:
                QMessageBox.information(self, 'PIN Entered', 'Success! PIN is correct.')
                self.pin_display.clear()  # Clear the entered PIN
                self.attempts = 0  # Reset attempts on success
                if self.main_window:
                    self.main_window.navigate_to_page_settings()  # Correct navigation to settings page
            else:
                self.attempts += 1
                self.pin_display.clear()  # Clear the entered PIN
                if self.attempts >= self.max_attempts:
                    QMessageBox.warning(self, 'PIN Entered', 'Incorrect PIN. Maximum attempts reached.')
                    self.attempts = 0  # Reset attempts after warning
                    if self.main_window:
                        self.main_window.navigate_to_page_one()
                        self.close()
                else:
                    QMessageBox.warning(self, 'PIN Entered', f'Incorrect PIN. {self.max_attempts - self.attempts} attempts left.')
        else:
            if len(self.pin_display.text()) < 4:
                self.pin_display.setText(self.pin_display.text() + text)
