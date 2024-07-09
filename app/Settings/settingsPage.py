import os
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QMessageBox, QGridLayout
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QPixmap, QIcon

class SettingsPage(QDialog):
    def __init__(self, parent=None, main_window=None):
        super().__init__(parent)
        self.main_window = main_window

        main_layout = QVBoxLayout(self)

        # Define paths to resources
        res_dir = os.path.join(os.path.dirname(__file__), '..', 'res', 'icon')

        # Back button
        back_icon_path = os.path.join(res_dir, '..', 'icon', 'back.png')
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
        main_layout.addWidget(self.back_button, alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)

        # Add a label for the title
        title_label = QLabel("SETTINGS")
        title_label.setStyleSheet("font-size: 36px; font-weight: bold;")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(title_label)

        # Add a spacer to push options to the middle
        main_layout.addStretch(10)

        # Grid layout for options10
        grid_layout = QGridLayout()
        grid_layout.setSpacing(20)  # Adjust spacing between buttons
        main_layout.addLayout(grid_layout)

        options = [
            "Change Bread Type and Thickness",
            "Slicer Lid Open",
            "Maintenance Mode",
            "Change Pin"
        ]

        # Add buttons for each option
        for index, option_text in enumerate(options):
            button = QPushButton(option_text)
            button.setStyleSheet(
                "QPushButton {"
                "   background-color: rgba(0, 0, 0, 0);"
                "   color: Black;"
                "   font-size: 20px;"
                "   font-weight: bold;"
                "   border: 2px solid black;"
                "   border-radius: 10px;"
                "}"
                "QPushButton:hover {"
                "   background-color: rgba(150, 150, 150, 0.7);"  # Hover effect
                "}"
                "QPushButton:pressed {"
                "   background-color: rgba(150, 150, 150, 0.7);"  # Press effect
                "}"
            )
            button.setFixedSize(QSize(360, 50))  # Set a fixed size for the buttons
            button.clicked.connect(lambda checked, text=option_text: self.on_option_clicked(text))
            grid_layout.addWidget(button, index, 10)  # Place each button in a new row

        # Add a spacer at the bottom for layout balance
        main_layout.addStretch()

    def on_option_clicked(self, option_text):
        QMessageBox.information(self, 'Option Clicked', f'Clicked: {option_text}')
        # Add logic to handle each option click

    def on_back_button_clicked(self):
        if self.main_window:
            self.main_window.navigate_to_page_one()  # Replace with appropriate navigation
            self.close()
