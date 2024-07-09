import os
from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QSpacerItem, QSizePolicy
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtCore import Qt, QSize, QTimer

class PageOne(QWidget):
    def __init__(self, parent=None, main_window=None):
        super().__init__(parent)
        self.main_window = main_window
        self.selected_breadtype = None
        
        # Define paths to resources
        res_dir = os.path.join(os.path.dirname(__file__), '..', 'res', 'BreadSelect')
        image_path = os.path.join(res_dir, 'breadSelectBG.png')
        settings_icon_path = os.path.join(os.path.dirname(__file__), '..', 'res', 'icon', 'settings.png')
        
        # Create main layout
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)  # Remove margins around the layout
        self.setLayout(self.layout)
        
        # Background label with image
        self.background_label = QLabel(self)
        self.set_background_image(self.background_label, image_path)
        self.layout.addWidget(self.background_label)
        
        # Create an inner layout for the background_label to hold the content
        self.inner_layout = QVBoxLayout(self.background_label)
        self.inner_layout.setContentsMargins(0, 0, 0, 0)
        self.background_label.setLayout(self.inner_layout)
        
        # Spacer above header label to create gap
        self.inner_layout.addSpacing(40)  # Increased spacing to move content down

        # Create a horizontal layout for the label and settings button
        self.header_layout = QHBoxLayout()
        
        # Overlay label for "Select Bread Type"
        self.select_bread_label = QLabel("Select Bread Type", self.background_label)
        self.select_bread_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.select_bread_label.setStyleSheet("color: white; font-size: 36px; font-weight: bold;")
        
        # Settings button
        self.settings_button = QPushButton(self.background_label)
        self.settings_button.setFixedSize(50, 50)
        self.settings_button.setIcon(QIcon(settings_icon_path))
        self.settings_button.setIconSize(QSize(45, 45))
        self.settings_button.setStyleSheet("background-color: rgba(0, 0, 0, 0); border: none;")
        self.settings_button.clicked.connect(self.open_settings_menu)
        
        # Add the label to the header layout with expanding spacers on either side
        self.header_layout.addSpacerItem(QSpacerItem(250, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))
        self.header_layout.addWidget(self.select_bread_label, 0, Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        self.header_layout.addSpacerItem(QSpacerItem(20, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))
        
        # Add the settings button to the header layout aligned to the top right corner
        self.header_layout.addWidget(self.settings_button, 0, Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignRight)
        self.header_layout.addSpacerItem(QSpacerItem(30, 0, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum))  # Add spacer to right of settings button
        
        # Add the header layout to the inner layout
        self.inner_layout.addLayout(self.header_layout)
        
        # Add some spacing at the top to move the label and button down a bit
        self.inner_layout.addSpacerItem(QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum))
        
        # Add transparent buttons for bread options
        bread_options = [
            "White Bread",
            "Whole Wheat Bread",
            "Sprouted Grain Bread",
            "Multigrain Sprouted Bread"
        ]
        
        button_height = 50  # Adjust button height as needed
        spacing_between_buttons = 10  # Increased spacing between buttons

        # Spacer to push buttons down from the top
        self.inner_layout.addSpacerItem(QSpacerItem(0, 100, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        for option in bread_options:
            button = QPushButton(option, self.background_label)
            button.setStyleSheet(
                "QPushButton {"
                "   background-color: rgba(0, 0, 0, 0);"
                "   color: white;"
                "   font-size: 24px;"  # Adjusted font size
                "   font-weight: bold;"
                "   border: 2px solid white;"
                "   border-radius: 10px;"
                "}"
                "QPushButton:hover {"
                "   background-color: rgba(150, 150, 150, 0.7);"  # Hover effect
                "}"
            )
            button.setFixedSize(350, button_height)
            button.clicked.connect(lambda _, bt=option: self.handle_button_click(bt))

            self.inner_layout.addWidget(button, 0, Qt.AlignmentFlag.AlignCenter)
            self.inner_layout.addSpacerItem(QSpacerItem(0, spacing_between_buttons, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum))
        
        # Spacer to push buttons up from the bottom
        self.inner_layout.addSpacerItem(QSpacerItem(0, 100, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

    def set_background_image(self, label, image_path):
        pixmap = QPixmap(image_path)
        label.setPixmap(pixmap)
        label.setScaledContents(True)
        
    def open_settings_menu(self):
        if self.main_window:
            self.main_window.open_settings()

    def handle_button_click(self, bread_type):
        self.selected_breadtype = bread_type  # Store the selected bread type
        self.navigate_to_page_three()  # Navigate to PageThree with selected option

    def navigate_to_page_three(self):
        if self.main_window:
            self.main_window.navigate_to_page_three(self.selected_breadtype)
