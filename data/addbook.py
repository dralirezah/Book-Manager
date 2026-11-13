"""Book Manager application logic and supporting components."""

from PySide6.QtWidgets import QMessageBox, QWidget
from .addbook_ui import Ui_Form
from .database import FileHandling

status_book = ("Unread", "Reading", "Finished")
genres_book = ("Novel", "History", "Philosophy", "Biography", "Poetry", "Religious", "Science")


class AddBook(QWidget):
    """Manage Addbook related application behavior."""
    def __init__(self):
        """Initialize the object and prepare its required state."""
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.cb_genres.addItems(genres_book)
        self.ui.btn_add.clicked.connect(self.add_book)
        self.ui.btn_cancel.clicked.connect(self.clear_form)

    def get_valid_name(self, text_widget, subject):
        """Handle Get valid name."""
        name = text_widget.toPlainText().strip()
        if not name:
            QMessageBox.warning(self, "Invalid Input", f"Please enter {subject}.")
            return None
        return name

    def clear_form(self):
        """Handle Clear form."""
        self.ui.txt_title.clear()
        self.ui.txt_author.clear()
        self.ui.sb_pages.setValue(1)
        self.ui.cb_genres.setCurrentIndex(0)

    def add_book(self):
        """Handle Add book."""
        title = self.get_valid_name(self.ui.txt_title, "Title")
        if title is None:
            return
        author = self.get_valid_name(self.ui.txt_author, "Author")
        if author is None:
            return
        pages = self.ui.sb_pages.value()
        if pages < 1:
            QMessageBox.warning(self, "Invalid Input", "Total pages must be at least 1.")
            return

        books = FileHandling.load_list_json()
        next_id = max((book.get("id", 0) for book in books), default=0) + 1
        books.append({
            "id": next_id, "title": title, "author": author,
            "pages": pages, "current_page": 0,
            "genres": self.ui.cb_genres.currentText(), "status": status_book[0]
        })
        FileHandling.save_list_json(books)
        QMessageBox.information(self, "Success", "Book added successfully!")
        self.clear_form()
