"""Book Manager application logic and supporting components."""

from PySide6.QtWidgets import QMessageBox, QWidget
from .delete_ui import Ui_Form
from .database import FileHandling


class DeleteBooks(QWidget):
    """Manage Deletebooks related application behavior."""
    def __init__(self):
        """Initialize the object and prepare its required state."""
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self._found_book_id = None
        self.ui.btn_find.clicked.connect(self.orther_btn_find)
        self.ui.btn_cancel.clicked.connect(self.orther_btn_cancel)
        self.ui.btn_delete.clicked.connect(self.orther_btn_delete)

    def orther_btn_find(self):
        """Handle Orther btn find."""
        self.ui.txtb_reading.clear()
        self.find_book()

    def orther_btn_cancel(self):
        """Handle Orther btn cancel."""
        self._found_book_id = None
        self.ui.txtb_reading.clear()
        self.ui.btn_delete.setEnabled(False)
        self.ui.sb_find.setEnabled(True)
        self.ui.btn_find.setEnabled(True)

    def orther_btn_delete(self):
        """Handle Orther btn delete."""
        self.deleted_book()

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
            self.ui.btn_delete.setEnabled(False)
            return
        self._found_book_id = book_id
        self.print_reading_book(book)
        self.ui.btn_delete.setEnabled(True)
        self.ui.sb_find.setEnabled(False)
        self.ui.btn_find.setEnabled(False)

    def deleted_book(self):
        """Handle Deleted book."""
        if self._found_book_id is None:
            return
        books = FileHandling.load_list_json()
        book = next((item for item in books if item.get("id") == self._found_book_id), None)
        if book is None:
            QMessageBox.warning(self, "Not Found", "This book no longer exists.")
            self.orther_btn_cancel()
            return
        answer = QMessageBox.question(
            self, "Delete Book", f"Do you want to delete '{book.get('title', '')}'?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )
        if answer != QMessageBox.StandardButton.Yes:
            return
        FileHandling.save_list_json([item for item in books if item.get("id") != self._found_book_id])
        self._found_book_id = None
        self.ui.txtb_reading.setPlainText("Book deleted successfully.")
        self.ui.btn_delete.setEnabled(False)
        self.ui.sb_find.setEnabled(True)
        self.ui.btn_find.setEnabled(True)
        QMessageBox.information(self, "Success", "Book deleted successfully!")
