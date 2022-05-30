import sys
from PyQt5.QtWidgets import *
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.table_widget()
        self.setWindowTitle("Spreadsheet")
        self.show()
    def table_widget(self):
        vbox = QVBoxLayout()
        table = QTableWidget()
        table.setRowCount(100)
        table.setColumnCount(100)
        vbox.addWidget(table)
        self.setLayout(vbox)
app = QApplication(sys.argv)
window = Window()
app.exec_()