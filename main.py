# Standard Library
import sys
import time

# Third Library
from PySide6.QtWidgets import QApplication

from src.login import LoginBox
from src.main_page import MainPage


def main():
    app = QApplication([])
    login_window = LoginBox()
    login_window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
