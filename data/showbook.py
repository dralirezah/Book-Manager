"""Book Manager application logic and supporting components."""

from PySide6.QtWidgets import QMessageBox, QWidget, QVBoxLayout
from .showbooks_ui import Ui_Form
from PySide6.QtCore import Qt
from .database import FileHandling


class ShowBook(QWidget) :
    
    """Manage Showbook related application behavior."""
    list_book = FileHandling.load_list_json()
    def __init__(self):
        
        """Initialize the object and prepare its required state."""
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
            
        for book in self.list_book:
            self.ui.table_books.setItem(10,20,30)
                
            