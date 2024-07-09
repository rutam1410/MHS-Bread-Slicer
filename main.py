import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from app.Pages.pageOne import PageOne
from app.Pages.pageTwo import PageTwo
from app.Pages.pageThree import PageThree
from app.Pages.pageFour import PageFour
from app.Pages.startPage import StartPage

from app.Settings.pinEntry import PinEntry
from app.Settings.settingsPage import SettingsPage  

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MHS Bread Slicer")
        self.setFixedSize(800, 480)  # Set fixed size for the window

        # Initialize variables to store selected options
        self.selected_bread_type = None
        self.selected_thickness = None

        # Create initial page and set it as central widget
        self.page_start = StartPage(main_window=self)
        self.setCentralWidget(self.page_start)
    
    def navigate_to_page_one(self):
        self.page_one = PageOne(main_window=self)
        self.setCentralWidget(self.page_one)
        
    def navigate_to_page_two(self, selected_breadtype):
        self.selected_bread_type = selected_breadtype
        self.page_two = PageTwo(main_window=self)
        self.setCentralWidget(self.page_two)

    def navigate_to_page_three(self, selected_thickness):
        self.selected_thickness = selected_thickness
        self.page_three = PageThree(self.selected_bread_type, self.selected_thickness, main_window=self)
        self.setCentralWidget(self.page_three)
    
    def navigate_to_page_four(self):
        self.page_four = PageFour(main_window=self)
        self.setCentralWidget(self.page_four)

    def open_settings(self):
        self.pin_entry = PinEntry(main_window=self)
        self.setCentralWidget(self.pin_entry)

    def navigate_to_page_settings(self):
        self.page_settings = SettingsPage(main_window=self)
        self.setCentralWidget(self.page_settings)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setGeometry(100, 100, 800, 480)  # Set main window geometry
    window.show()
    sys.exit(app.exec())
