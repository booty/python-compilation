import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QLineEdit

class HelloWorldWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello World PyQt")
        self.init_ui()

    def init_ui(self):
        self.label = QLabel("Hello, PyQt!", self)
        self.input_field = QLineEdit(self)
        self.input_field.setPlaceholderText("Type something...")
        self.button = QPushButton("Click Me", self)
        self.button.clicked.connect(self.on_button_click)
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.input_field)
        layout.addWidget(self.button)
        
        self.setLayout(layout)

    def on_button_click(self):
        text = self.input_field.text()
        self.label.setText(f"You typed: {text}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HelloWorldWindow()
    window.show()
    sys.exit(app.exec_())