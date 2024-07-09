import os
from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import Qt, QSize

class PageThree(QWidget):
    def __init__(self, selected_bread_type="", selected_thickness="", parent=None, main_window=None):
        super().__init__(parent)
        self.main_window = main_window
        self.selected_bread_type = selected_bread_type
        self.selected_thickness = selected_thickness

        # Main layout for the page
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)  # Remove margins around the layout
        self.setLayout(self.layout)  
        
        # Ensure the res directory is correctly referenced
        res_dir = os.path.join(os.path.dirname(__file__), '..', 'res', 'Dispense')
        image_path = os.path.join(res_dir, 'dispenseBG.png')
        
        # Background label with image
        self.background_label = QLabel(self)
        self.background_label.setPixmap(QPixmap(image_path))
        self.background_label.setScaledContents(True)  # Ensure the image scales to fit the label
        self.layout.addWidget(self.background_label)
        
        # Create a layout for background_label to hold the content
        self.inner_layout = QVBoxLayout(self.background_label)
        self.inner_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Heading label
        self.heading_label = QLabel("Bread Dispense", self.background_label)
        self.heading_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.heading_label.setStyleSheet("font-size: 36px; font-weight: bold; color: white;")
        self.inner_layout.addWidget(self.heading_label)
        
        # spacing for header
        self.inner_layout.addSpacing(80)
        
        # Display selected options
        self.selected_labels_layout = QVBoxLayout()
        self.inner_layout.addLayout(self.selected_labels_layout)
        
        self.selected_bread_label = QLabel(f"You Selected Bread Type: {self.selected_bread_type}", self.background_label)
        self.selected_bread_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.selected_bread_label.setStyleSheet("font-size: 20px; color: white;")
        self.selected_labels_layout.addWidget(self.selected_bread_label)
        
        self.selected_thickness_label = QLabel(f"with Thickness: {self.selected_thickness}", self.background_label)
        self.selected_thickness_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.selected_thickness_label.setStyleSheet("font-size: 20px; color: white;")
        self.selected_labels_layout.addWidget(self.selected_thickness_label)
        
        # Spacer
        self.inner_layout.addSpacing(110)
        
        # Dispense button
        self.dispense_button = QPushButton("DISPENSE", self.background_label)
        self.dispense_button.setFixedSize(200, 60)
        self.dispense_button.setStyleSheet(
            "QPushButton {"
            "   background-color: rgba(0, 0, 0, 0);"
            "   color: white;"
            "   font-size: 24px;"
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
        self.dispense_button.clicked.connect(self.on_dispense_button_clicked)
        self.inner_layout.addWidget(self.dispense_button, 0, Qt.AlignmentFlag.AlignCenter)

        # Create back button
        back_icon_path = os.path.join(res_dir, '..', 'icon', 'back.png')
        self.back_button = QPushButton(self.background_label)
        self.back_button.setIcon(QIcon(back_icon_path))
        self.back_button.setIconSize(QSize(75, 75))
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
        self.back_button.clicked.connect(self.navigate_to_page_two)

    def navigate_to_page_two(self):
        if self.main_window:
            self.main_window.navigate_to_page_two(self.selected_bread_type)

    def on_dispense_button_clicked(self):
        if self.main_window:
            self.main_window.navigate_to_page_four()
