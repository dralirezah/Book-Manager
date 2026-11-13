"""Book Manager application logic and supporting components."""

from PySide6.QtWidgets import QMessageBox, QWidget
from .change_ui import Ui_Form
from .database import FileHandling

status_book = ("Unread", "Reading", "Finished")


class ChangeProgress(QWidget):
    """Manage Changeprogress related application behavior."""
    def __init__(self):
        """Initialize the object and prepare its required state."""
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self._found_book_id = None
        self.ui.btn_find.clicked.connect(self.orther_btn_find)
        self.ui.btn_cancel.clicked.connect(self.orther_btn_cancel)
        self.ui.btn_change.clicked.connect(self.orther_btn_change)

    def orther_btn_find(self):
        """Handle Orther btn find."""
        self.ui.txtb_reading.clear()
        self.find_book()

    def orther_btn_cancel(self):
        """Handle Orther btn cancel."""
        self._found_book_id = None
        self.ui.txtb_reading.clear()
        self.ui.btn_change.setEnabled(False)
        self.ui.sb_page.setEnabled(False)
        self.ui.sb_find.setEnabled(True)
        self.ui.btn_find.setEnabled(True)
        self.ui.sb_page.setMaximum(9999)
        self.ui.sb_page.setValue(0)

    def orther_btn_change(self):
        """Handle Orther btn change."""
        self.changed_book()

    def print_reading_book(self, book):
        """Handle Print reading book."""
        pages = book.get("pages", 0)
        current = book.get("current_page", 0)
        progress = (current / pages * 100) if pages else 0
        self.ui.txtb_reading.setPlainText(
            f"ID: {book.get('id', '')}\n"
            f"Title: {book.get('title', '')}\n"
            f"Author: {book.get('author', '')}\n"
            f"Genre: {book.get('genres', '')}\n"
            f"Progress: {current}/{pages} ({progress:.0f}%)\n"
            f"Status: {book.get('status', 'Unread')}"
        )

    def find_book(self):
        """Handle Find book."""
        book_id = self.ui.sb_find.value()
        books = FileHandling.load_list_json()
        book = next((item for item in books if item.get("id") == book_id), None)
        if book is None:
            self._found_book_id = None
            self.ui.txtb_reading.setPlainText("Book not found. Check the ID and try again.")
            self.ui.btn_change.setEnabled(False)
            self.ui.sb_page.setEnabled(False)
            return

        self._found_book_id = book_id
        self.print_reading_book(book)
        pages = int(book.get("pages", 0))
        current = int(book.get("current_page", 0))
        self.ui.sb_page.setMaximum(max(pages, 0))
        self.ui.sb_page.setValue(min(current, max(pages, 0)))
        if pages > 0 and current >= pages:
            self.ui.txtb_reading.append("\nThis book is already finished.")
            self.ui.btn_change.setEnabled(False)
            self.ui.sb_page.setEnabled(False)
        else:
            self.ui.btn_change.setEnabled(True)
            self.ui.sb_page.setEnabled(True)
        self.ui.sb_find.setEnabled(False)
        self.ui.btn_find.setEnabled(False)

    def changed_book(self):
        """Handle Changed book."""
        if self._found_book_id is None:
            return
        books = FileHandling.load_list_json()
        book = next((item for item in books if item.get("id") == self._found_book_id), None)
        if book is None:
            QMessageBox.warning(self, "Not Found", "This book no longer exists.")
            self.orther_btn_cancel()
            return
        page = self.ui.sb_page.value()
        if page < 0 or page > int(book.get("pages", 0)):
            QMessageBox.warning(self, "Invalid Page", "Current page must be within the book's page count.")
            return
        book["current_page"] = page
        book["status"] = status_book[2] if page >= int(book.get("pages", 0)) else (
            status_book[1] if page > 0 else status_book[0]
        )
        FileHandling.save_list_json(books)
        self.print_reading_book(book)
        if book["status"] == status_book[2]:
            self.ui.txtb_reading.append("\nThis book is finished!")
        QMessageBox.information(self, "Success", "Reading progress updated.")
        self.orther_btn_cancel()
