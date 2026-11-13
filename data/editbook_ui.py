from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QWidget, QLabel, QPushButton, QSpinBox, QTextEdit, QComboBox,
    QVBoxLayout, QHBoxLayout, QFormLayout, QFrame, QSizePolicy
)


class Ui_Form:
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setMinimumSize(900, 650)

        root = QVBoxLayout(Form)
        root.setContentsMargins(30, 26, 30, 24)
        root.setSpacing(18)

        header = QHBoxLayout()
        self.lbl_title = QLabel("▧  Edit Book")
        self.lbl_title.setObjectName("pageTitle")
        self.lbl_subtitle = QLabel("Update the details of a book in your library")
        self.lbl_subtitle.setObjectName("pageSubtitle")
        self.lbl_subtitle.setAlignment(
            Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter
        )
        header.addWidget(self.lbl_title)
        header.addStretch(1)
        header.addWidget(self.lbl_subtitle)
        root.addLayout(header)

        self.separator = QFrame()
        self.separator.setObjectName("separator")
        self.separator.setFrameShape(QFrame.Shape.HLine)
        self.separator.setFixedHeight(2)
        root.addWidget(self.separator)

        body = QHBoxLayout()
        body.setSpacing(24)

        # Left panel: find a book and preview its current details.
        self.left_panel = QWidget()
        left_layout = QVBoxLayout(self.left_panel)
        left_layout.setContentsMargins(0, 0, 0, 0)
        left_layout.setSpacing(12)

        self.find_card = QWidget()
        self.find_card.setObjectName("formCard")
        find_layout = QFormLayout(self.find_card)
        find_layout.setContentsMargins(20, 20, 20, 20)
        find_layout.setSpacing(12)

        self.lbl_find_id = QLabel("Book ID")
        self.sb_find_id = QSpinBox()
        self.sb_find_id.setObjectName("sb_find_id")
        self.sb_find_id.setRange(1, 999999)
        self.sb_find_id.setMinimumHeight(42)
        self.btn_find = QPushButton("Find Book")
        self.btn_find.setObjectName("btn_find")
        self.btn_find.setMinimumHeight(42)
        find_layout.addRow(self.lbl_find_id, self.sb_find_id)
        find_layout.addRow("", self.btn_find)
        left_layout.addWidget(self.find_card)

        self.lbl_details = QLabel("Book details")
        self.lbl_details.setObjectName("sectionTitle")
        left_layout.addWidget(self.lbl_details)

        self.txtb_details = QTextEdit()
        self.txtb_details.setObjectName("txtb_reading")
        self.txtb_details.setReadOnly(True)
        self.txtb_details.setFont(QFont("Segoe UI", 11))
        self.txtb_details.setPlaceholderText(
            "Find a book by ID to see its current details here."
        )
        self.txtb_details.setMinimumHeight(220)
        self.txtb_details.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding
        )
        left_layout.addWidget(self.txtb_details, 1)
        body.addWidget(self.left_panel, 2)

        # Right panel: editable fields.
        self.form_card = QWidget()
        self.form_card.setObjectName("formCard")
        form = QFormLayout(self.form_card)
        form.setContentsMargins(22, 22, 22, 22)
        form.setSpacing(13)
        form.setLabelAlignment(
            Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter
        )
        form.setFieldGrowthPolicy(
            QFormLayout.FieldGrowthPolicy.ExpandingFieldsGrow
        )

        self.lbl_title_field = QLabel("Book title")
        self.txt_title = QTextEdit()
        self.txt_title.setObjectName("txt_title")
        self.txt_title.setFont(QFont("Segoe UI", 11))
        self.txt_title.setPlaceholderText("Enter the book title")
        self.txt_title.setFixedHeight(66)

        self.lbl_author = QLabel("Author")
        self.txt_author = QTextEdit()
        self.txt_author.setObjectName("txt_author")
        self.txt_author.setFont(QFont("Segoe UI", 11))
        self.txt_author.setPlaceholderText("Enter the author's name")
        self.txt_author.setFixedHeight(66)

        self.lbl_pages = QLabel("Total pages")
        self.sb_pages = QSpinBox()
        self.sb_pages.setObjectName("sb_pages")
        self.sb_pages.setRange(1, 9999)
        self.sb_pages.setMinimumHeight(42)

        self.lbl_current_page = QLabel("Current page")
        self.sb_current_page = QSpinBox()
        self.sb_current_page.setObjectName("sb_current_page")
        self.sb_current_page.setRange(0, 9999)
        self.sb_current_page.setMinimumHeight(42)

        self.lbl_genre = QLabel("Genre")
        self.cb_genres = QComboBox()
        self.cb_genres.setObjectName("cb_genres")
        self.cb_genres.setMinimumHeight(42)

        self.lbl_status = QLabel("Reading status")
        self.cb_status = QComboBox()
        self.cb_status.setObjectName("cb_status")
        self.cb_status.setMinimumHeight(42)
        self.cb_status.setEnabled(False)
        self.cb_status.setToolTip("Status is calculated from the current page.")

        form.addRow(self.lbl_title_field, self.txt_title)
        form.addRow(self.lbl_author, self.txt_author)
        form.addRow(self.lbl_pages, self.sb_pages)
        form.addRow(self.lbl_current_page, self.sb_current_page)
        form.addRow(self.lbl_genre, self.cb_genres)
        form.addRow(self.lbl_status, self.cb_status)

        body.addWidget(self.form_card, 3)
        root.addLayout(body, 1)

        self.lbl_hint = QLabel(
            "Find a book first. Its ID cannot be changed; status follows the current page."
        )
        self.lbl_hint.setObjectName("hint")
        self.lbl_hint.setWordWrap(True)
        self.lbl_hint.setAlignment(Qt.AlignmentFlag.AlignCenter)
        root.addWidget(self.lbl_hint)

        footer = QHBoxLayout()
        footer.addStretch(1)
        self.btn_clear = QPushButton("Cancel / Clear")
        self.btn_clear.setObjectName("btn_cancel")
        self.btn_clear.setMinimumSize(130, 44)
        self.btn_save = QPushButton("Save Changes")
        self.btn_save.setObjectName("btn_change")
        self.btn_save.setMinimumSize(150, 44)
        self.btn_save.setEnabled(False)
        footer.addWidget(self.btn_clear)
        footer.addWidget(self.btn_save)
        root.addLayout(footer)

        Form.setWindowTitle("Edit Book")
