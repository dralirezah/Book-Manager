"""Book Manager application logic and supporting components."""

from PySide6.QtWidgets import QMessageBox, QWidget

from .editbook_ui import Ui_Form
from .database import FileHandling

GENRES = ("Novel", "History", "Philosophy", "Biography", "Poetry", "Religious", "Science")
STATUSES = ("Unread", "Reading", "Finished")


class EditBook(QWidget):
    """Manage Editbook related application behavior."""
    def __init__(self):
        """Initialize the object and prepare its required state."""
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self._found_book_id = None

        self.ui.cb_genres.addItems(GENRES)
        self.ui.cb_status.addItems(STATUSES)

        self.ui.btn_find.clicked.connect(self.find_book)
        self.ui.btn_save.clicked.connect(self.save_changes)
        self.ui.btn_clear.clicked.connect(self.clear_form)
        self.ui.sb_pages.valueChanged.connect(self.update_page_limit)
        self.ui.sb_current_page.valueChanged.connect(self.update_status)

        self.set_editing_enabled(False)

    def set_editing_enabled(self, enabled):
        """Handle Set editing enabled."""
        for widget in (
            self.ui.txt_title,
            self.ui.txt_author,
            self.ui.sb_pages,
            self.ui.sb_current_page,
            self.ui.cb_genres,
        ):
            widget.setEnabled(enabled)
        self.ui.btn_save.setEnabled(enabled)

    def find_book(self):
        """Handle Find book."""
        book_id = self.ui.sb_find_id.value()
        books = FileHandling.load_list_json()
        book = next((item for item in books if item.get("id") == book_id), None)

        if book is None:
            self._found_book_id = None
            self.ui.txtb_details.setPlainText(
                "Book not found. Check the ID and try again."
            )
            self.clear_edit_fields()
            self.set_editing_enabled(False)
            QMessageBox.information(self, "Book Not Found", "No book with this ID was found.")
            return

        self._found_book_id = book_id
        self.ui.txt_title.setPlainText(str(book.get("title", "")))
        self.ui.txt_author.setPlainText(str(book.get("author", "")))

        pages = max(1, min(9999, int(book.get("pages", 1) or 1)))
        current_page = max(0, min(pages, int(book.get("current_page", 0) or 0)))
        self.ui.sb_pages.blockSignals(True)
        self.ui.sb_pages.setValue(pages)
        self.ui.sb_pages.blockSignals(False)
        self.ui.sb_current_page.setMaximum(pages)
        self.ui.sb_current_page.setValue(current_page)

        genre = str(book.get("genres", "Novel"))
        genre_index = self.ui.cb_genres.findText(genre)
        self.ui.cb_genres.setCurrentIndex(genre_index if genre_index >= 0 else 0)

        self.set_editing_enabled(True)
        self.update_status()
        self.show_book_details(book)

    def update_page_limit(self, pages):
        """Update the Page limit information."""
        self.ui.sb_current_page.setMaximum(pages)
        if self.ui.sb_current_page.value() > pages:
            self.ui.sb_current_page.setValue(pages)
        self.update_status()

    def update_status(self, *_):
        """Update the Status information."""
        pages = self.ui.sb_pages.value()
        current = self.ui.sb_current_page.value()
        if current <= 0:
            status = STATUSES[0]
        elif current >= pages:
            status = STATUSES[2]
        else:
            status = STATUSES[1]

        index = self.ui.cb_status.findText(status)
        if index >= 0:
            self.ui.cb_status.setCurrentIndex(index)

    def show_book_details(self, book):
        """Handle Show book details."""
        pages = int(book.get("pages", 0) or 0)
        current = int(book.get("current_page", 0) or 0)
        progress = current / pages * 100 if pages else 0
        self.ui.txtb_details.setPlainText(
            f"ID: {book.get('id', '')}\n"
            f"Title: {book.get('title', '')}\n"
            f"Author: {book.get('author', '')}\n"
            f"Genre: {book.get('genres', '')}\n"
            f"Progress: {current}/{pages} ({progress:.0f}%)\n"
            f"Status: {book.get('status', 'Unread')}"
        )

    def clear_edit_fields(self):
        """Handle Clear edit fields."""
        self.ui.txt_title.clear()
        self.ui.txt_author.clear()
        self.ui.sb_pages.setValue(1)
        self.ui.sb_current_page.setValue(0)
        self.ui.cb_genres.setCurrentIndex(0)
        self.ui.cb_status.setCurrentIndex(0)

    def clear_form(self):
        """Handle Clear form."""
        self._found_book_id = None
        self.ui.sb_find_id.setValue(1)
        self.ui.txtb_details.clear()
        self.clear_edit_fields()
        self.set_editing_enabled(False)

    def save_changes(self):
        """Save the Changes data."""
        if self._found_book_id is None:
            return

        title = self.ui.txt_title.toPlainText().strip()
        author = self.ui.txt_author.toPlainText().strip()
        if not title:
            QMessageBox.warning(self, "Invalid Input", "Please enter the book title.")
            self.ui.txt_title.setFocus()
            return
        if not author:
            QMessageBox.warning(self, "Invalid Input", "Please enter the author's name.")
            self.ui.txt_author.setFocus()
            return

        pages = self.ui.sb_pages.value()
        current_page = self.ui.sb_current_page.value()
        if current_page > pages:
            QMessageBox.warning(
                self, "Invalid Page",
                "Current page cannot be greater than the total number of pages."
            )
            return

        books = FileHandling.load_list_json()
        book = next((item for item in books if item.get("id") == self._found_book_id), None)
        if book is None:
            QMessageBox.warning(self, "Book Not Found", "This book no longer exists.")
            self.clear_form()
            return

        if current_page <= 0:
            status = STATUSES[0]
        elif current_page >= pages:
            status = STATUSES[2]
        else:
            status = STATUSES[1]

        book.update({
            "title": title,
            "author": author,
            "pages": pages,
            "current_page": current_page,
            "genres": self.ui.cb_genres.currentText(),
            "status": status,
        })
        FileHandling.save_list_json(books)
        self.show_book_details(book)
        QMessageBox.information(self, "Success", "Book details updated successfully.")
