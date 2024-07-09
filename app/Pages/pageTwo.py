import os
from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import Qt, QSize

class PageTwo(QWidget):
    def __init__(self, parent=None, main_window=None):
        super().__init__(parent)
        self.main_window = main_window
        self.selected_thickness = None
        
        # Main layout for the page
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)  # Remove margins around the layout
        self.setLayout(self.layout)  
        
        # Ensure the res directory is correctly referenced
        res_dir = os.path.join(os.path.dirname(__file__), '..', 'res', 'Thickness')
        image_path = os.path.join(res_dir, 'thicknessBG.png')
        
        # Background label with image
        self.background_label = QLabel(self)
        self.background_label.setPixmap(QPixmap(image_path))
        self.background_label.setScaledContents(True)  # Ensure the image scales to fit the label
        self.layout.addWidget(self.background_label)
        
        # Create a layout for background_label to hold the content
        self.inner_layout = QVBoxLayout(self.background_label)
        self.inner_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Heading label
        self.heading_label = QLabel("Select Bread Thickness", self.background_label)
        self.heading_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.heading_label.setStyleSheet("font-size: 36px; font-weight: bold; color: white;")
        self.inner_layout.addWidget(self.heading_label)
        
        # Spacer
        self.inner_layout.addSpacing(60)
        
        # Buttons layout
        self.buttons_layout = QVBoxLayout()
        self.buttons_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.inner_layout.addLayout(self.buttons_layout)
        
        # Thickness buttons
        thickness_sizes = ["2mm", "4mm", "6mm", "8mm"]
        self.buttons = []
        for size in thickness_sizes:
            button = QPushButton(size, self.background_label)
            button.setStyleSheet(
                "QPushButton {"
                "   background-color: rgba(0, 0, 0, 0);"
                "   color: white;"
                "   font-size: 20px;"
                "   font-weight: bold;"
                "   border: 2px solid white;"
                "   border-radius: 10px;"
                "}"
                "QPushButton:hover {"
                "   background-color: rgba(150, 150, 150, 0.7);"  # Hover effect
                "}"
                "QPushButton:pressed {"
                "   background-color: rgba(150, 150, 150, 0.7);"  # Press effect
                "}"
            )
            button.setFixedSize(150, 50)
            button.clicked.connect(lambda checked, s=size: self.select_thickness(s))

            self.buttons.append(button)
            self.buttons_layout.addWidget(button)
            self.buttons_layout.addSpacing(10)  # Add spacing between buttons
        
        # Create back button
        back_icon_path = os.path.join(res_dir, '..', 'icon', 'back.png')
        self.back_button = QPushButton(self.background_label)
        self.back_button.setIcon(QIcon(back_icon_path))
        self.back_button.setIconSize(QSize(75, 120))
        self.back_button.setStyleSheet(
            "QPushButton {"
            "   background-color: rgba(0, 0, 0, 0);"
            "   border: none;"
            "}"
            "QPushButton:hover {"
            "   background-color: rgba(150, 150, 150, 0.5);"  # Light grey with some transparency
            "}"
        )
        self.back_button.setGeometry(50, 50, 60, 60)  # Adjust the position as needed
        self.back_button.clicked.connect(self.navigate_to_page_one)
        
        # Set layout for PageTwo
        self.setLayout(self.layout)

    def select_thickness(self, size):
        self.selected_thickness = size  # Store the selected thickness
        self.navigate_to_page_three()

    def navigate_to_page_three(self):
        if self.main_window:
            self.main_window.navigate_to_page_three(self.selected_thickness)

    def navigate_to_page_one(self):
        if self.main_window:
            self.main_window.navigate_to_page_one()
