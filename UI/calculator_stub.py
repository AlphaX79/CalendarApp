from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton
from PySide6.QtCore import Qt, QLocale
from PySide6.QtGui import QDoubleValidator




class CalculatorUI(QWidget):
    def __init__(self, /):

        super().__init__()
        validator = QDoubleValidator(decimals=3)
        validator.setLocale(QLocale.system())
        self.locale = QLocale.system()

        self.entry_box_1 = QLineEdit()
        self.entry_box_1.setValidator(validator)
        self.entry_box_2 = QLineEdit()
        self.entry_box_2.setValidator(validator)
        self.button = QPushButton("Calculate")

        self.layout = self.generate_layout()
        self.result_label = QLabel(alignment=Qt.AlignmentFlag.AlignCenter)
        self.result_lay = QVBoxLayout()
        self.result_lay.addWidget(self.result_label)
        self.layout.addLayout(self.result_lay)
        self.button.clicked.connect(self.calculate_sum)
        self.setLayout(self.layout)

    def generate_layout(self):
        calc_layout = QVBoxLayout()
        label = QLabel("Calling it calculator is a little bit too much")


        input_boxes_layout = QHBoxLayout()
        input_1_box_layout = QHBoxLayout()
        input_2_box_layout = QHBoxLayout()
        input_1_box_layout.addWidget(QLabel("First number"), alignment=Qt.AlignmentFlag.AlignCenter)
        input_1_box_layout.addWidget(self.entry_box_1)
        # input_1_box_layout.addStretch()    #fills remaining space with emptiness
        input_2_box_layout.addWidget(QLabel("Second number"))
        input_2_box_layout.addWidget(self.entry_box_2)
        input_2_box_layout.addStretch()
        calc_layout.addWidget(label, alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignCenter)
        calc_layout.addLayout(input_boxes_layout)
        input_boxes_layout.addLayout(input_1_box_layout)
        input_boxes_layout.addLayout(input_2_box_layout)
        calc_layout.addStretch()
        calc_layout.addWidget(self.button)

        return calc_layout

    def update_results(self, result):
        self.result_label.setText(str(result))


    def calculate_sum(self):

        number1, _ = self.locale.toDouble(self.entry_box_1.text())
        number2, _ = self.locale.toDouble(self.entry_box_2.text())
        self.update_results(number1 + number2)



