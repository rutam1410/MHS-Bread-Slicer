from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QLabel

class HelperMethods:
    
    @staticmethod
    def set_background_image(label: QLabel, image_path: str):
        pixmap = QPixmap(image_path)
        label.setPixmap(pixmap)
        label.setScaledContents(True)
