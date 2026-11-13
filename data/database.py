"""Book Manager application logic and supporting components."""

import os
import json


import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QStackedWidget,
    QVBoxLayout,
    QWidget,
)



class FileHandling :

    """Manage Filehandling related application behavior."""
    def load_list_json() :
        """Handle Load list json."""
        try :
            if os.path.exists("Books.json") :
                with open("Books.json", "r") as file_loading :
                    loading_book = json.load(file_loading)
                    return loading_book
            else :
                with open("Books.json", "w") :
                    return []
        except :
            return []  

    def save_list_json(books) :  
        """Save the List json data."""
        try :
            with open("Books.json", "w") as file_saving :
                json.dump(books, file_saving, indent= 4)
        except FileNotFoundError as e:
            print(e) 
    
    
    
