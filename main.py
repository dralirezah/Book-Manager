"""Book Manager application logic and supporting components."""

import sys
import json
from pathlib import Path

from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, QHBoxLayout,
    QGridLayout, QFrame, QProgressBar, QPushButton, QScrollArea
)

from data.main_ui import Ui_MainWindow
from data.style import AppStyle
from data.addbook import AddBook
from data.change import ChangeProgress
from data.showbooks import ShowBooks
from data.delete import DeleteBooks
from data.editbook import EditBook


class MainWindow(QMainWindow):
    """Manage Mainwindow related application behavior."""
    def __init__(self):
        """Initialize the object and prepare its required state."""
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.current_theme = "light"
        QApplication.instance().setStyleSheet(AppStyle.stylesheet(self.current_theme))

        self.home_page = self.create_home_page()
        self.change_progress_book = ChangeProgress()
        self.show_book = ShowBooks()
        self.show_book.setStyleSheet("")
        self.add_book = AddBook()
        self.edit_page = EditBook()
        self.delete_book = DeleteBooks()
        self.about_page = self.create_about_page()

        for page in (self.home_page, self.change_progress_book, self.show_book,
                     self.add_book, self.edit_page, self.delete_book, self.about_page):
            self.ui.pages.addWidget(page)

        for index, button in enumerate(self.ui.buttons):
            button.clicked.connect(lambda checked=False, i=index: self.navigate(i))
        self.ui.exit_button.clicked.connect(self.close)
        self.ui.theme_button.clicked.connect(self.toggle_theme)
        self.ui.pages.setCurrentIndex(0)

    def navigate(self, index):
        """Handle Navigate."""
        self.ui.pages.setCurrentIndex(index)
        if index == 0:
            self.refresh_home_page()

    def toggle_theme(self):
        """Handle Toggle theme."""
        self.current_theme = "dark" if self.current_theme == "light" else "light"
        QApplication.instance().setStyleSheet(AppStyle.stylesheet(self.current_theme))
        if self.current_theme == "dark":
            self.ui.theme_button.setText("☀  Light theme")
            self.ui.theme_button.setToolTip("Switch to light theme")
        else:
            self.ui.theme_button.setText("☾  Dark theme")
            self.ui.theme_button.setToolTip("Switch to dark theme")

    def read_books(self):
        """Read and return Books data."""
        candidates = [Path("Books.json"), Path("data/Books.json")]
        for path in candidates:
            try:
                with path.open("r", encoding="utf-8") as file:
                    data = json.load(file)
                if isinstance(data, list) and data:
                    return data
                if isinstance(data, list):
                    return data
            except (OSError, json.JSONDecodeError):
                pass
        return []

    def create_home_page(self):
        """Build and return the Home page interface."""
        page = QWidget()
        page.setObjectName("homePage")
        outer = QVBoxLayout(page)
        outer.setContentsMargins(28, 24, 28, 24)
        outer.setSpacing(16)

        heading = QLabel("Reading Dashboard")
        heading.setObjectName("pageTitle")
        subtitle = QLabel("Your personal library at a glance")
        subtitle.setObjectName("pageSubtitle")
        outer.addWidget(heading)
        outer.addWidget(subtitle)

        self.stats_grid = QGridLayout()
        self.stats_grid.setSpacing(12)
        outer.addLayout(self.stats_grid)

        self.reading_heading = QLabel("Currently Reading")
        self.reading_heading.setObjectName("sectionTitle")
        outer.addWidget(self.reading_heading)

        self.reading_list = QVBoxLayout()
        self.reading_list.setSpacing(10)
        outer.addLayout(self.reading_list)
        outer.addStretch(1)
        self.refresh_home_page()
        return page

    def clear_layout(self, layout):
        """Handle Clear layout."""
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            child_layout = item.layout()
            if widget:
                widget.deleteLater()
            elif child_layout:
                self.clear_layout(child_layout)

    def make_stat_card(self, label, number, symbol):
        """Handle Make stat card."""
        card = QFrame()
        card.setObjectName("statCard")
        box = QVBoxLayout(card)
        box.setContentsMargins(16, 14, 16, 14)
        icon = QLabel(symbol)
        icon.setObjectName("statIcon")
        name = QLabel(label)
        name.setObjectName("statLabel")
        value = QLabel(str(number))
        value.setObjectName("statValue")
        box.addWidget(icon)
        box.addWidget(name)
        box.addWidget(value)
        return card

    def refresh_home_page(self):
        """Refresh the Home page data and interface."""
        if not hasattr(self, "stats_grid"):
            return
        self.clear_layout(self.stats_grid)
        self.clear_layout(self.reading_list)
        books = self.read_books()
        total = len(books)
        reading = [b for b in books if str(b.get("status", "")).lower() == "reading"]
        finished = [b for b in books if str(b.get("status", "")).lower() == "finished"]
        unread = [b for b in books if str(b.get("status", "")).lower() == "unread"]
        for i, (label, count, symbol) in enumerate([
            ("Total Books", total, "▤"), ("Reading Now", len(reading), "◷"),
            ("Finished", len(finished), "✓"), ("Unread", len(unread), "▣")
        ]):
            self.stats_grid.addWidget(self.make_stat_card(label, count, symbol), i // 2, i % 2)

        if not reading:
            empty = QLabel("No books are currently marked as Reading.")
            empty.setObjectName("emptyState")
            self.reading_list.addWidget(empty)
        for book in reading:
            title_text = str(book.get("title", "Untitled"))
            author_text = str(book.get("author", "Unknown author"))
            try:
                pages = max(0, int(book.get("pages", 0)))
                current = max(0, min(pages, int(book.get("current_page", 0))))
            except (ValueError, TypeError):
                pages, current = 0, 0
            percent = round(current * 100 / pages) if pages else 0
            card = QFrame()
            card.setObjectName("readingCard")
            row = QHBoxLayout(card)
            row.setContentsMargins(16, 12, 16, 12)
            info = QVBoxLayout()
            title = QLabel(title_text)
            title.setObjectName("bookTitle")
            author = QLabel(author_text)
            author.setObjectName("pageSubtitle")
            progress_text = QLabel(f"{current} of {pages} pages  •  {max(0, pages-current)} pages remaining")
            progress_text.setObjectName("progressText")
            bar = QProgressBar()
            bar.setRange(0, 100)
            bar.setValue(percent)
            bar.setTextVisible(True)
            bar.setFormat(f"{percent}%")
            info.addWidget(title)
            info.addWidget(author)
            info.addWidget(progress_text)
            info.addWidget(bar)
            row.addLayout(info, 1)
            self.reading_list.addWidget(card)

    def create_about_page(self):
        """Build and return the About page interface."""
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setContentsMargins(40, 35, 40, 35)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        title = QLabel("About Me")
        title.setObjectName("pageTitle")
        description = QLabel("Python developer and book lover.\n\nThis is my personal Book Manager project, built with Python and PySide6.")
        description.setObjectName("pageSubtitle")
        description.setWordWrap(True)
        github = QPushButton("  GitHub Profile")
        github.setIcon(QIcon.fromTheme("github"))
        github.clicked.connect(lambda: __import__('webbrowser').open("https://github.com/"))
        layout.addWidget(title)
        layout.addSpacing(12)
        layout.addWidget(description)
        layout.addSpacing(18)
        layout.addWidget(github, 0, Qt.AlignmentFlag.AlignLeft)
        layout.addStretch(1)
        return page


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    app.setStyleSheet(AppStyle.stylesheet("light"))
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
