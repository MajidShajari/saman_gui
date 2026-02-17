# Standard Library
import sys

# Third Library
from PySide6.QtCore import QRect, Qt
from PySide6.QtWidgets import (
    QApplication,
    QGridLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QWidget,
)

from utils.login_process import authenticate


class LoginBox(QWidget):
    def __init__(self):
        super().__init__()
        # config
        self.setWindowTitle("مجتمع فولاد سامان")
        self.setGeometry(QRect(100, 100, 300, 300))
        layout = QGridLayout(self)
        main_group_box = QGroupBox(title="ورود")
        main_group_box.setMaximumHeight(250)
        main_group_box.setAlignment(Qt.AlignCenter)
        layout.addWidget(main_group_box)

        # Login Layout
        login_group_layout = QGridLayout()
        main_group_box.setLayout(login_group_layout)
        login_group_layout.setColumnStretch(1, 1)
        login_group_layout.setRowStretch(0, 1)
        login_group_layout.setRowStretch(1, 1)
        login_group_layout.setRowStretch(2, 1)
        # User Name Group
        username_label = QLabel(text="نام کاربری")
        self.username_entry = QLineEdit()
        self.username_entry.setFixedWidth(200)
        username_group = QHBoxLayout()
        username_group.addWidget(self.username_entry, alignment=Qt.AlignCenter)
        username_group.addWidget(username_label, alignment=Qt.AlignCenter)
        # Password Group
        password_label = QLabel(text="رمز عبور")
        self.password_entry = QLineEdit()
        self.password_entry.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_entry.setFixedWidth(200)
        password_group = QHBoxLayout()
        password_group.addWidget(self.password_entry, alignment=Qt.AlignCenter)
        password_group.addWidget(password_label, alignment=Qt.AlignCenter)
        # Login Group
        login_button = QPushButton("ورود")
        guest_button = QPushButton("کاربر مهمان")
        button_group = QHBoxLayout()
        button_group.addWidget(login_button, alignment=Qt.AlignRight)
        button_group.addWidget(guest_button, alignment=Qt.AlignLeft)
        login_button.clicked.connect(self._handle_user_login)
        guest_button.clicked.connect(self._handle_guest_login)
        # Status
        self.status_label = QLabel(text="با نام کاربری و رمز عبور خود وارد شوید یا روی دکمه مهمان کلیک کنید.")
        self.status_label.setStyleSheet("color:blue;")

        status_group = QHBoxLayout()
        status_group.addWidget(self.status_label, alignment=Qt.AlignCenter)

        login_group_layout.addLayout(username_group, 0, 1, alignment=Qt.AlignCenter)
        login_group_layout.addLayout(password_group, 1, 1, alignment=Qt.AlignCenter)
        login_group_layout.addLayout(button_group, 2, 1, alignment=Qt.AlignCenter)
        login_group_layout.addLayout(status_group, 3, 1, alignment=Qt.AlignCenter)

    def _handle_user_login(self):
        if self.username_entry == "" or self.password_entry == "":
            self.status_label.setText("نام کاربری یا رمز عبور وارد نشده است")
            self.status_label.setStyleSheet("color: red;")
        else:
            try:
                if authenticate(self.username_entry, self.password_entry):
                    self.status_label.setText("ورود موفق آمیز")
                    self.status_label.setStyleSheet("color: green;")
                else:
                    self.status_label.setText("نام کاربری یا رمز عبور نامعتبر است")
                    self.status_label.setStyleSheet("color: red;")
            except Exception as e:
                self.status_label.setText("خطا در ارتباط با سرور")
                self.status_label.setStyleSheet("color: red;")

    def _handle_guest_login(self):
        self.status_label.setText("ورود به عنوان مهمان")
        self.status_label.setStyleSheet("color: blue;")


if __name__ == "__main__":
    app = QApplication([])
    window = LoginBox()
    window.show()
    sys.exit(app.exec())
