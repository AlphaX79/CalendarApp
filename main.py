import sys

from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QTabWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QLineEdit,
    QHBoxLayout,
)
from PySide6.QtCore import Qt, QLocale
from PySide6.QtGui import QDoubleValidator



#def print_result():


def button_clicked():
    locale = QLocale.system()

    number1, _ = locale.toDouble(entry_box_1.text())
    number2, _ = locale.toDouble(entry_box_2.text())
    result = str(number1 + number2)
    result_lay.addWidget(QLabel(result, alignment = Qt.AlignmentFlag.AlignCenter))


app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("CalendarApp")
window.resize(1600, 900)

tabs = QTabWidget()
calc_tab = QWidget()
secondary_tab = QWidget()

label = QLabel("Test Label  1")
button = QPushButton("Calculate")

#Validator to work with coma separator
validator = QDoubleValidator(decimals=3)
validator.setLocale(QLocale.system())

entry_box_1 = QLineEdit()
entry_box_1.setValidator(validator)
entry_box_2 = QLineEdit()
entry_box_2.setValidator(validator)

button.clicked.connect(button_clicked)

#Calculator TAB
calc_layout = QVBoxLayout()

#nested layouts
input_boxes_layout = QHBoxLayout()

input_1_box_layout = QHBoxLayout()
input_2_box_layout = QHBoxLayout()
result_lay = QVBoxLayout()

input_1_box_layout.addWidget(QLabel("First number"), alignment = Qt.AlignmentFlag.AlignCenter)
input_1_box_layout.addWidget(entry_box_1)
# input_1_box_layout.addStretch()    #fills remaining space with emptiness
input_2_box_layout.addWidget(QLabel("Second number"))
input_2_box_layout.addWidget(entry_box_2)
input_2_box_layout.addStretch()

calc_layout.addWidget(label, alignment =Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignCenter)
calc_layout.addLayout(input_boxes_layout)
input_boxes_layout.addLayout(input_1_box_layout)
input_boxes_layout.addLayout(input_2_box_layout)
calc_layout.addStretch()
calc_layout.addWidget(button)
calc_layout.addLayout(result_lay)
calc_tab.setLayout(calc_layout)

# TABS Setting
tabs.addTab(calc_tab, "Calculator")
tabs.addTab(secondary_tab, "Secondary")

layout = QVBoxLayout()
layout.addWidget(tabs)
window.setLayout(layout)

window.show()

sys.exit(app.exec())