import os
from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt6.QtGui import QMovie
from PyQt6.QtCore import QTimer, Qt, QSize

class PageFour(QWidget):
    def __init__(self, main_window=None):
        super().__init__()
        self.main_window = main_window

        # Main layout for the page
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)  # Remove margins around the layout
        self.setLayout(self.layout)

        # Label for the waiting text
        self.waiting_label = QLabel("Please wait, bread will dispense soon...", self)
        self.waiting_label.setStyleSheet("font-size: 36px; font-weight: bold; color: black;")
        self.waiting_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.waiting_label)

        # Label for the animated GIF
        self.gif_label = QLabel(self)
        self.gif_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.gif_label)
       
        # Spacer
        self.layout.addSpacing(100)

        # Load and set the GIF
        res_dir = os.path.join(os.path.dirname(__file__), '..', 'res', 'icon')
        gif_path = os.path.join(res_dir, 'waitingGif.gif')

        self.movie = QMovie(gif_path)
        self.movie.setScaledSize(QSize(200, 200))
        self.gif_label.setMovie(self.movie)
        self.movie.start()

        # Schedule the redirection to PageOne after 10 seconds
        QTimer.singleShot(10000, self.navigate_to_page_one)

    def navigate_to_page_one(self):
        if self.main_window:
            self.main_window.navigate_to_page_one()
