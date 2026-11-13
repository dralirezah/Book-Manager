"""Book Manager application logic and supporting components."""


from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QTableWidgetItem, QHeaderView
from .database import FileHandling
from .showbooks_ui import Ui_Form

status_book = (
    "Unread",
    "Reading",
    "Finished"
)

class ShowBooks(QWidget):
    """Manage Showbooks related application behavior."""
    list_book = FileHandling.load_list_json()
    keys = ["Id", "Title", "Author","Pages", "Current page","Genre", "Status"]
    
    def __init__(self):
        """Initialize the object and prepare its required state."""
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.show_all_books()
        
        
        
        # search and refresh book
        self.ui.le_search.textEdited.connect(self.searchbook)
        self.ui.btn_search.clicked.connect(self.searchbook)
        self.ui.btn_refresh.clicked.connect(self.refreshbook)
        self.ui.cb_sort_books.currentIndexChanged.connect(self.sortbook)
        
        
        # change status of cb status
        self.ui.cb_filter_status.currentIndexChanged.connect(self.changestatus)
    
    
    
    
    # function for search and refresh    
    def searchbook(self) :
        """Handle Searchbook."""
        self.ui.cb_filter_status.setCurrentIndex(0)
        list_books = self.list_book
        text = self.ui.le_search.text()
        search = str(text.lower())
        search_result = [book for book in list_books if search in book['title'].lower() or search in book['author'].lower()]
        
        self.HorizontalHeaderLabels()
        self.ui.table_books.setRowCount(0)
        self.ui.table_books.setRowCount(len(search_result))
        self.ui.lbl_count.setText(f"Showing {len(search_result)} books")   
        
        for row_idx, book in enumerate(search_result):
            for col_idx, key in enumerate(book.keys()):
                value = str(book.get(key, ""))
                item = QTableWidgetItem(value)
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                self.ui.table_books.setItem(row_idx, col_idx, item) 
        
    def refreshbook(self) :
        """Handle Refreshbook."""
        self.ui.le_search.setText("")    
        self.show_all_books()
        self.ui.cb_filter_status.setCurrentIndex(0)
        
    # function for change cb_status    
    def changestatus(self) :
        """Handle Changestatus."""
        status = self.ui.cb_filter_status.currentIndex()
        
        if status == 0 :
            self.show_all_books()
            self.ui.cb_sort_books.setCurrentIndex(0)
        elif status == 1:
            self.show_unread_books()
            self.ui.cb_sort_books.setCurrentIndex(0)
        elif status == 2 :
            self.show_reading_books()
            self.ui.cb_sort_books.setCurrentIndex(0)
        elif status == 3 :
            self.show_finished_books()      
            self.ui.cb_sort_books.setCurrentIndex(0)     
        
    # Functions of fill header row of table
    def HorizontalHeaderLabels(self) :  
        
        """Handle Horizontalheaderlabels."""
        id_key = self.keys          
        self.ui.table_books.setColumnCount(len(id_key))
        self.ui.table_books.setHorizontalHeaderLabels(id_key)        
    
    # Functions of show book in table
    def show_all_books(self):

        """Handle Show all books."""
        books = self.list_book
        self.HorizontalHeaderLabels()
        self.ui.table_books.setRowCount(len(books))
        self.ui.lbl_count.setText(f"Showing {len(books)} books")
        for row_idx, book in enumerate(books):
            for col_idx, key in enumerate(book.keys()):
                value = str(book.get(key, ""))
                item = QTableWidgetItem(value)
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                self.ui.table_books.setItem(row_idx, col_idx, item)
   
    def show_unread_books(self) :
        
        """Handle Show unread books."""
        books = self.list_book
        self.HorizontalHeaderLabels()
        self.ui.table_books.setRowCount(0)
        unread_books = [book for book in books if book['status'] == status_book[0]]
        self.ui.table_books.setRowCount(len(unread_books))
        self.ui.lbl_count.setText(f"Showing {len(unread_books)} books")
        
        for row_idx, book in enumerate(unread_books):
            for col_idx, key in enumerate(book.keys()):
                if book['status'] == status_book[0] :
                    value = str(book.get(key, ""))
                    item = QTableWidgetItem(value)
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                    self.ui.table_books.setItem(row_idx, col_idx, item)                
    
    def show_reading_books(self) :
            
        """Handle Show reading books."""
            books = self.list_book
            self.HorizontalHeaderLabels()
            self.ui.table_books.setRowCount(0)
            reading_books = [book for book in books if book['status'] == status_book[1]]
            self.ui.table_books.setRowCount(len(reading_books))
            self.ui.lbl_count.setText(f"Showing {len(reading_books)} books")
            
            
            
            for row_idx, book in enumerate(reading_books):
                for col_idx, key in enumerate(book.keys()):
                    if book['status'] == status_book[1] :
                        value = str(book.get(key, ""))
                        item = QTableWidgetItem(value)
                        item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                        self.ui.table_books.setItem(row_idx, col_idx, item)   

    def show_finished_books(self) :
            
        """Handle Show finished books."""
            books = self.list_book
            self.HorizontalHeaderLabels()
            self.ui.table_books.setRowCount(0)
            finished_books = [book for book in books if book['status'] == status_book[2]]
            self.ui.table_books.setRowCount(len(finished_books))
            self.ui.lbl_count.setText(f"Showing {len(finished_books)} books")
            
            
            for row_idx, book in enumerate(finished_books):
                for col_idx, key in enumerate(book.keys()):
                    if book['status'] == status_book[2] :
                        value = str(book.get(key, ""))
                        item = QTableWidgetItem(value)
                        item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                        self.ui.table_books.setItem(row_idx, col_idx, item)                            
                        
    def sortbook(self):
        """Handle Sortbook."""
        books = self.list_book
        
        status = self.ui.cb_sort_books.currentIndex()
        if status == 0 :
            self.ui.table_books.sortItems(0,Qt.SortOrder.AscendingOrder)
        elif status == 1 :    
            self.ui.table_books.sortItems(0,Qt.SortOrder.DescendingOrder)
        elif status == 2 :
            self.ui.table_books.sortItems(1,Qt.SortOrder.AscendingOrder)
        elif status == 3 :
            self.ui.table_books.sortItems(1,Qt.SortOrder.DescendingOrder) 
        elif status == 4 :
            self.ui.table_books.sortItems(3,Qt.SortOrder.AscendingOrder)
        elif status == 5 :
            self.ui.table_books.sortItems(3,Qt.SortOrder.DescendingOrder)                             