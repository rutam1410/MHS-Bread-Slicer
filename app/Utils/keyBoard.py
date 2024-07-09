from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLineEdit

class Keyboard(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout(self)
        self.line_edit = QLineEdit(self)
        self.layout.addWidget(self.line_edit)
        
        buttons = [
            '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
            'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P',
            'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L',
            'Z', '^', 'X', 'C', 'V', 'B', 'N', 'M', '<-'
        ]
        
        for button in buttons:
            btn = QPushButton(button, self)
            btn.clicked.connect(lambda checked, b=button: self.press(b))
            self.layout.addWidget(btn)
        
        self.setLayout(self.layout)
        self.shift = False

    def press(self, key):
        if key == "<-":
            current_text = self.line_edit.text()
            self.line_edit.setText(current_text[:-1])
        elif key == "^":
            self.shift = not self.shift
            self.update_keys()
        else:
            self.line_edit.insert(key.lower() if not self.shift else key.upper())

    def update_keys(self):
        for button in self.findChildren(QPushButton):
            char = button.text()
            if char.isalpha():
                button.setText(char.lower() if not self.shift else char.upper())
