# -*- coding: utf-8 -*-
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout,
    QLabel, QLineEdit, QPushButton, QComboBox, QTableWidget,
    QTableWidgetItem, QHeaderView, QGroupBox, QAbstractItemView,
    QSizePolicy
)


class Ui_Form:
    def setupUi(self, ShowBooks):
        ShowBooks.setObjectName("ShowBooks")
        ShowBooks.resize(1250, 780)
        ShowBooks.setMinimumSize(950, 600)
        ShowBooks.setWindowTitle("Book Manager v1 — Show Books")

        self.central_layout = QVBoxLayout(ShowBooks)
        self.central_layout.setContentsMargins(22, 18, 22, 18)
        self.central_layout.setSpacing(16)

        # Header
        header = QHBoxLayout()
        self.lbl_title = QLabel("📖  Show Books")
        self.lbl_title.setObjectName("lbl_title")
        title_font = QFont("Segoe UI", 23)
        title_font.setBold(True)
        self.lbl_title.setFont(title_font)
        self.lbl_subtitle = QLabel("Manage your books, grow your mind")
        self.lbl_subtitle.setObjectName("lbl_subtitle")
        self.lbl_subtitle.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        header.addWidget(self.lbl_title)
        header.addStretch(1)
        header.addWidget(self.lbl_subtitle)
        self.central_layout.addLayout(header)

        self.line_header = QWidget()
        self.line_header.setFixedHeight(1)
        self.line_header.setObjectName("line_header")
        self.central_layout.addWidget(self.line_header)

        # Search and filter group
        self.gb_search_filter = QGroupBox("Search & Filter")
        self.gb_search_filter.setObjectName("gb_search_filter")
        filter_layout = QVBoxLayout(self.gb_search_filter)
        filter_layout.setContentsMargins(14, 18, 14, 14)
        filter_layout.setSpacing(12)

        search_row = QHBoxLayout()
        search_row.setSpacing(12)
        self.le_search = QLineEdit()
        self.le_search.setObjectName("le_search")
        self.le_search.setPlaceholderText("Search by title or author...")
        self.le_search.setClearButtonEnabled(True)
        self.le_search.setMinimumHeight(42)

        self.btn_search = QPushButton("⌕  Search")
        self.btn_search.setObjectName("btn_search")
        self.btn_search.setMinimumSize(125, 42)
        self.btn_refresh = QPushButton("⟳  Refresh")
        self.btn_refresh.setObjectName("btn_refresh")
        self.btn_refresh.setMinimumSize(125, 42)

        search_row.addWidget(self.le_search, 1)
        search_row.addWidget(self.btn_search)
        search_row.addWidget(self.btn_refresh)
        filter_layout.addLayout(search_row)

        controls_row = QGridLayout()
        controls_row.setHorizontalSpacing(12)
        controls_row.setVerticalSpacing(8)

        self.lbl_filter_status = QLabel("Filter by status:")
        self.lbl_filter_status.setObjectName("lbl_filter_status")
        self.cb_filter_status = QComboBox()
        self.cb_filter_status.setObjectName("cb_filter_status")
        self.cb_filter_status.addItems([
            "All Books", "Unread", "Reading", "Finished"
        ])
        self.cb_filter_status.setMinimumHeight(40)

        self.lbl_sort_books = QLabel("Sort by:")
        self.lbl_sort_books.setObjectName("lbl_sort_books")
        self.cb_sort_books = QComboBox()
        self.cb_sort_books.setObjectName("cb_sort_books")
        self.cb_sort_books.addItems([
            "ID (Ascending)",
            "ID (Descending)",
            "Title (A–Z)",
            "Title (Z–A)",
            "Pages (Ascending)",
            "Pages (Descending)",
        ])
        self.cb_sort_books.setMinimumHeight(40)

        controls_row.addWidget(self.lbl_filter_status, 0, 0)
        controls_row.addWidget(self.cb_filter_status, 0, 1)
        controls_row.addWidget(self.lbl_sort_books, 0, 2)
        controls_row.addWidget(self.cb_sort_books, 0, 3)
        controls_row.setColumnStretch(1, 1)
        controls_row.setColumnStretch(3, 1)
        filter_layout.addLayout(controls_row)
        self.central_layout.addWidget(self.gb_search_filter)

        # Books table
        self.table_books = QTableWidget()
        self.table_books.setObjectName("table_books")
        self.table_books.setColumnCount(7)
        
        self.table_books.setRowCount(0)
        self.table_books.setAlternatingRowColors(True)
        self.table_books.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.table_books.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.table_books.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table_books.setShowGrid(False)
        self.table_books.verticalHeader().setVisible(False)
        self.table_books.verticalHeader().setDefaultSectionSize(42)
        self.table_books.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.table_books.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        self.table_books.horizontalHeader().setSectionResizeMode(4, QHeaderView.ResizeMode.ResizeToContents)
        self.table_books.horizontalHeader().setSectionResizeMode(5, QHeaderView.ResizeMode.ResizeToContents)
        self.table_books.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.central_layout.addWidget(self.table_books, 1)

        # Footer
        footer = QHBoxLayout()
        self.lbl_count = QLabel("Showing 0 books")
        self.lbl_count.setObjectName("lbl_count")
        footer.addWidget(self.lbl_count)
        footer.addStretch(1)

        self.btn_prev_page = QPushButton("‹")
        self.btn_prev_page.setObjectName("btn_prev_page")
        self.btn_prev_page.setFixedSize(42, 40)
        self.btn_prev_page.setEnabled(False)
        self.lbl_page = QLabel("1 / 1")
        self.lbl_page.setObjectName("lbl_page")
        self.lbl_page.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbl_page.setMinimumWidth(54)
        self.btn_next_page = QPushButton("›")
        self.btn_next_page.setObjectName("btn_next_page")
        self.btn_next_page.setFixedSize(42, 40)
        self.btn_next_page.setEnabled(False)
        footer.addWidget(self.btn_prev_page)
        footer.addWidget(self.lbl_page)
        footer.addWidget(self.btn_next_page)
        self.central_layout.addLayout(footer)

        # Dark theme
        ShowBooks.setStyleSheet("""
            QWidget#ShowBooks {
                background-color: #171f33;
                color: #dce6ff;
                font-family: "Segoe UI";
                font-size: 10pt;
            }
            QLabel#lbl_title {
                color: #dce6ff;
                padding: 3px 0;
            }
            QLabel#lbl_subtitle, QLabel#lbl_count, QLabel#lbl_page {
                color: #aebfe7;
            }
            QWidget#line_header {
                background-color: #52658d;
            }
            QGroupBox#gb_search_filter {
                border: 1px solid #344568;
                border-radius: 9px;
                margin-top: 8px;
                padding-top: 8px;
                color: #c8d7fa;
                font-weight: bold;
            }
            QGroupBox#gb_search_filter::title {
                subcontrol-origin: margin;
                left: 14px;
                padding: 0 5px;
            }
            QLineEdit, QComboBox {
                background-color: #263451;
                border: 1px solid #40547b;
                border-radius: 6px;
                padding: 7px 10px;
                color: #e1e9ff;
                selection-background-color: #477cff;
            }
            QLineEdit:focus, QComboBox:focus {
                border: 1px solid #6c98ff;
            }
            QComboBox QAbstractItemView {
                background-color: #263451;
                color: #e1e9ff;
                selection-background-color: #477cff;
                border: 1px solid #40547b;
            }
            QPushButton {
                background-color: #263451;
                color: #e1e9ff;
                border: 1px solid #344568;
                border-radius: 7px;
                padding: 8px 14px;
            }
            QPushButton:hover {
                background-color: #344568;
            }
            QPushButton:pressed {
                background-color: #1e2a43;
            }
            QPushButton:disabled {
                color: #68799d;
                background-color: #202b42;
            }
            QPushButton#btn_search {
                background-color: #477cff;
                border: 1px solid #477cff;
                color: white;
                font-weight: bold;
            }
            QPushButton#btn_search:hover {
                background-color: #5d8cff;
            }
            QTableWidget#table_books {
                background-color: #171f33;
                alternate-background-color: #1b2740;
                color: #dce6ff;
                border: 1px solid #344568;
                border-radius: 8px;
                selection-background-color: #344c7c;
                selection-color: white;
                outline: 0;
            }
            QTableWidget#table_books::item {
                padding: 7px;
                border-bottom: 1px solid #293956;
            }
            QHeaderView::section {
                background-color: #263451;
                color: #c8d7fa;
                border: none;
                border-bottom: 1px solid #40547b;
                padding: 12px 8px;
                font-weight: bold;
            }
        """)
if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)

    MainWindow = QMainWindow()
    ui = Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()

    sys.exit(app.exec())
    
    