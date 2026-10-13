from PySide6.QtWidgets import (
    QWidget,
    QTabWidget,
    QMainWindow,
)
from UI.calculator_stub import CalculatorUI

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("CalendarApp")
        self.resize(1600, 900)
        self.tabs = QTabWidget()
        self.calc_tab = CalculatorUI()
        self.secondary_tab = QWidget() #TODO: replace with new tabs later on
        self.tabs.addTab(self.calc_tab, "Calculator")
        self.tabs.addTab(self.secondary_tab, "Secondary")
        self.setCentralWidget(self.tabs)






