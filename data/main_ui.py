from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QStackedWidget
)
from PySide6.QtGui import QIcon


class Ui_MainWindow:
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowTitle("Book Manager v1")
        MainWindow.resize(1280, 760)
        MainWindow.setMinimumSize(1050, 650)

        self.central_widget = QWidget()
        self.central_widget.setObjectName("centralWidget")
        MainWindow.setCentralWidget(self.central_widget)

        self.main_layout = QHBoxLayout(self.central_widget)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        self.sidebar = QWidget()
        self.sidebar.setObjectName("sidebar")
        self.sidebar.setFixedWidth(225)
        self.sidebar_layout = QVBoxLayout(self.sidebar)
        self.sidebar_layout.setContentsMargins(14, 20, 14, 16)
        self.sidebar_layout.setSpacing(9)

        self.logo = QLabel("📚  Book Manager")
        self.logo.setObjectName("logo")
        self.logo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.sidebar_layout.addWidget(self.logo)

        self.sidebar_divider = QWidget()
        self.sidebar_divider.setFixedHeight(1)
        self.sidebar_layout.addWidget(self.sidebar_divider)
        self.sidebar_layout.addSpacing(8)

        self.buttons = []
        menu_items = [
            "⌂   Home", "✎   Change Progress", "▤   Manage Books",
            "+   Add Book", "▧   Edit Book", "⌫   Delete Book", "ⓘ   About Me"
        ]
        for index, text in enumerate(menu_items):
            button = QPushButton(text)
            button.setObjectName(f"menuButton{index}")
            button.setMinimumHeight(44)
            self.sidebar_layout.addWidget(button)
            self.buttons.append(button)

        self.sidebar_layout.addStretch()

        self.theme_button = QPushButton("☾  Dark theme")
        self.theme_button.setObjectName("themeButton")
        self.theme_button.setMinimumHeight(44)
        self.sidebar_layout.addWidget(self.theme_button)

        self.exit_button = QPushButton("↪   Exit")
        self.exit_button.setObjectName("exitButton")
        self.exit_button.setMinimumHeight(44)
        self.sidebar_layout.addWidget(self.exit_button)

        self.pages = QStackedWidget()
        self.pages.setObjectName("pages")
        self.main_layout.addWidget(self.sidebar)
        self.main_layout.addWidget(self.pages, 1)
