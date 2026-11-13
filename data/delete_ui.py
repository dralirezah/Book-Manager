from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QWidget, QLabel, QPushButton, QSpinBox, QTextBrowser, QVBoxLayout,
    QHBoxLayout, QFormLayout, QFrame, QSizePolicy
)


class Ui_Form:
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setMinimumSize(0, 0)
        root = QVBoxLayout(Form)
        root.setContentsMargins(30, 26, 30, 24)
        root.setSpacing(18)

        header = QHBoxLayout()
        self.label_4 = QLabel("⌫  Delete Book")
        self.label_4.setObjectName("pageTitle")
        self.label_5 = QLabel("Manage your books, grow your mind")
        self.label_5.setObjectName("pageSubtitle")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        header.addWidget(self.label_4)
        header.addStretch(1)
        header.addWidget(self.label_5)
        root.addLayout(header)

        self.widget_2 = QFrame()
        self.widget_2.setObjectName("separator")
        self.widget_2.setFrameShape(QFrame.Shape.HLine)
        self.widget_2.setFixedHeight(2)
        root.addWidget(self.widget_2)

        body = QHBoxLayout()
        body.setSpacing(24)
        self.txtb_reading = QTextBrowser()
        self.txtb_reading.setObjectName("txtb_reading")
        self.txtb_reading.setFont(QFont("Segoe UI", 11))
        self.txtb_reading.setPlaceholderText("Book details will appear here after you search by ID.")
        self.txtb_reading.setMinimumWidth(260)
        self.txtb_reading.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        body.addWidget(self.txtb_reading, 3)

        self.form_widget = QWidget()
        self.form_widget.setObjectName("formCard")
        form = QFormLayout(self.form_widget)
        form.setContentsMargins(22, 24, 22, 24)
        form.setSpacing(18)
        form.setFieldGrowthPolicy(QFormLayout.FieldGrowthPolicy.ExpandingFieldsGrow)

        self.label = QLabel("Book ID")
        self.sb_find = QSpinBox()
        self.sb_find.setObjectName("sb_find")
        self.sb_find.setRange(1, 999999)
        self.sb_find.setMinimumHeight(42)

        self.btn_find = QPushButton("Find Book")
        self.btn_find.setObjectName("btn_find")
        self.btn_find.setMinimumHeight(42)
        form.addRow(self.label, self.sb_find)
        form.addRow("", self.btn_find)

        self.label_2 = QLabel("New current page")
        self.sb_page = QSpinBox()
        self.sb_page.setObjectName("sb_page")
        self.sb_page.setRange(0, 9999)
        self.sb_page.setMinimumHeight(42)
        self.sb_page.setEnabled(False)

        body.addWidget(self.form_widget, 2)
        root.addLayout(body, 1)

        self.label_3 = QLabel("* If you don't know the ID, open Manage Books.")
        self.label_3.setObjectName("hint")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_3.setWordWrap(True)
        root.addWidget(self.label_3)

        footer = QHBoxLayout()
        footer.addStretch(1)
        self.btn_cancel = QPushButton("Cancel")
        self.btn_cancel.setObjectName("btn_cancel")
        self.btn_cancel.setMinimumSize(120, 44)
        self.btn_delete = QPushButton("Delete Book")
        self.btn_delete.setObjectName("btn_delete")
        self.btn_delete.setMinimumSize(140, 44)
        self.btn_delete.setEnabled(False)
        self.btn_change = QPushButton("Save Progress")
        self.btn_change.setObjectName("btn_change")
        self.btn_change.setMinimumSize(140, 44)
        self.btn_change.setEnabled(False)
        footer.addWidget(self.btn_cancel)
        footer.addWidget(self.btn_delete)
        root.addLayout(footer)
        Form.setWindowTitle("Delete Book")
