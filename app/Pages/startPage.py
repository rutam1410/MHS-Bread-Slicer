from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout
from app.Utils.helper_methods import HelperMethods
import os

class StartPage(QWidget):
    def __init__(self, parent=None, main_window=None):
        super().__init__(parent)
        self.main_window = main_window
        
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)  # Remove margins around the layout
        self.setLayout(self.layout)  
        
        # Ensure the res directory is correctly referenced
        res_dir = os.path.join(os.path.dirname(__file__), '..', 'res')
        image_path = os.path.join(res_dir, 'startPage_bg.png')
        
        self.background_label = QLabel(self)
        self.layout.addWidget(self.background_label)
        
        HelperMethods.set_background_image(self.background_label, image_path)

    def mousePressEvent(self, event):
        self.navigate_to_page_one()

    def navigate_to_page_one(self):
        if self.main_window:
            self.main_window.navigate_to_page_one()
