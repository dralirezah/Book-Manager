"""Centralized light/dark themes for Book Manager."""

class AppStyle:
    """Manage Appstyle related application behavior."""
    THEMES = {
        "light": {
            "bg": "#F4F7FB", "surface": "#FFFFFF", "surface_alt": "#F8FAFC",
            "text": "#172033", "muted": "#667085", "border": "#D8E0EC",
            "accent": "#2563EB", "accent_hover": "#1D4ED8", "selection": "#DBEAFE",
            "header": "#EEF2F7", "disabled": "#F2F4F7", "danger": "#DC2626",
            "hover": "#EFF6FF", "sidebar": "#FFFFFF"
        },
        "dark": {
            "bg": "#171B2A", "surface": "#20263A", "surface_alt": "#252D43",
            "text": "#E6EAF5", "muted": "#A6B0C8", "border": "#39445F",
            "accent": "#5685FF", "accent_hover": "#7198FF", "selection": "#354B78",
            "header": "#2A334B", "disabled": "#252B3D", "danger": "#EF6262",
            "hover": "#2D3853", "sidebar": "#1D2335"
        }
    }

    @classmethod
    def stylesheet(cls, theme="light"):
        """Handle Stylesheet."""
        c = cls.THEMES.get(theme, cls.THEMES["light"])
        return f"""
        * {{ font-family: 'Segoe UI', Arial, sans-serif; font-size: 13px; }}
        QMainWindow, QWidget#centralWidget, QStackedWidget#pages,
        QWidget#Form, QWidget#homePage, QWidget#placeholderPage,
        QWidget#ShowBooks {{ background-color: {c['bg']}; color: {c['text']}; }}
        QWidget#sidebar {{ background-color: {c['sidebar']}; border-right: 1px solid {c['border']}; }}
        QWidget#sidebarDivider, QFrame#separator, QWidget#line_header {{ background-color: {c['border']}; border: none; }}
        QWidget#formCard {{ background-color: {c['surface']}; border: 1px solid {c['border']}; border-radius: 12px; }}
        QLabel {{ color: {c['text']}; background: transparent; }}
        QLabel#logo {{ color: {c['text']}; font-size: 19px; font-weight: 700; padding: 12px 4px; }}
        QLabel#pageTitle {{ font-size: 24px; font-weight: 700; }}
        QLabel#pageSubtitle, QLabel#hint, QLabel#lbl_subtitle, QLabel#lbl_count, QLabel#lbl_page {{ color: {c['muted']}; }}
        QLabel#pageSubtitle {{ font-size: 12px; }}
        QLabel#sectionTitle, QLabel#lbl_title {{ font-size: 16px; font-weight: 700; }}
        QPushButton {{ background-color: {c['surface']}; color: {c['text']}; border: 1px solid {c['border']}; border-radius: 8px; padding: 9px 14px; min-height: 18px; }}
        QPushButton:hover {{ background-color: {c['hover']}; border-color: {c['accent']}; }}
        QPushButton:pressed {{ background-color: {c['selection']}; }}
        QPushButton:disabled {{ color: {c['muted']}; background-color: {c['disabled']}; border-color: {c['border']}; }}
        QPushButton#btn_add, QPushButton#btn_change, QPushButton#btn_find,
        QPushButton#btn_search, QPushButton#btn_refresh, QPushButton#btn_next_page,
        QPushButton#themeButton {{ background-color: {c['accent']}; color: #FFFFFF; border: 1px solid {c['accent']}; font-weight: 600; }}
        QPushButton#btn_add:hover, QPushButton#btn_change:hover, QPushButton#btn_find:hover,
        QPushButton#btn_search:hover, QPushButton#btn_refresh:hover, QPushButton#btn_next_page:hover,
        QPushButton#themeButton:hover {{ background-color: {c['accent_hover']}; border-color: {c['accent_hover']}; }}
        QPushButton#btn_delete {{ background-color: {c['danger']}; color: white; border: 1px solid {c['danger']}; font-weight: 600; }}
        QPushButton#btn_delete:hover {{ background-color: {c['danger']}; }}
        QPushButton#menuButton0, QPushButton#menuButton1, QPushButton#menuButton2,
        QPushButton#menuButton3, QPushButton#menuButton4, QPushButton#menuButton5, QPushButton#menuButton6, 
        QPushButton#exitButton {{ text-align: left; padding-left: 14px; min-height: 22px; font-size: 13px; }}
        QPushButton#exitButton:hover {{ background-color: {c['hover']}; }}
        QTextEdit, QTextBrowser, QLineEdit, QSpinBox, QComboBox, QTableWidget {{
            background-color: {c['surface']}; color: {c['text']}; border: 1px solid {c['border']};
            border-radius: 7px; padding: 8px; selection-background-color: {c['selection']};
            selection-color: {c['text']}; font-family: 'Segoe UI', Arial, sans-serif; font-size: 14px;
        }}
        QTextEdit:focus, QTextBrowser:focus, QLineEdit:focus, QSpinBox:focus, QComboBox:focus {{ border: 1px solid {c['accent']}; }}
        QTextEdit#txt_title, QTextEdit#txt_author, QTextBrowser#txtb_reading {{ font-family: 'Segoe UI', Arial, sans-serif; font-size: 14px; padding: 10px; }}
        QComboBox::drop-down {{ border: none; width: 24px; }}
        QComboBox QAbstractItemView {{ background-color: {c['surface']}; color: {c['text']}; selection-background-color: {c['selection']}; }}
        QTableWidget {{ gridline-color: {c['border']}; alternate-background-color: {c['surface_alt']}; }}
        QHeaderView::section {{ background-color: {c['header']}; color: {c['text']}; padding: 9px; border: none; border-bottom: 1px solid {c['border']}; font-weight: 600; }}
        QGroupBox {{ background-color: {c['surface']}; color: {c['text']}; border: 1px solid {c['border']}; border-radius: 10px; margin-top: 12px; padding: 12px; font-weight: 600; }}
        QGroupBox::title {{ subcontrol-origin: margin; left: 12px; padding: 0 5px; color: {c['text']}; }}
        """
# Git practice
# Sorting feature development


# Version A
# Version B

# New update in master
# Second update in master