# Standard Library
import sys

# Third Library
from PySide6.QtCore import QRect, Qt
from PySide6.QtWidgets import QApplication, QGridLayout, QGroupBox, QWidget


class MainPage(QWidget):
    def __init__(self):
        super().__init__()
        # config
        self.setWindowTitle("مجتمع فولاد سامان")
        self.setGeometry(QRect(50, 50, 600, 600))
        layout = QGridLayout(self)
        top_group_box = QGroupBox()
        top_group_box.setStyle()
        main_group_box = QGroupBox()
        main_group_box.setAlignment(Qt.AlignCenter)
        layout.addWidget(top_group_box, 0, 0)
        layout.addWidget(main_group_box, 1, 0)


if __name__ == "__main__":
    app = QApplication([])
    window = MainPage()
    window.show()
    sys.exit(app.exec())
