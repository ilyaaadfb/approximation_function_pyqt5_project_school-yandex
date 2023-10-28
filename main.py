import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QTableWidgetItem, QMainWindow, QFileDialog
import openpyxl

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("untitledmain.ui", self)
        self.tableWidget.setColumnWidth(0, 40)
        self.tableWidget.setColumnWidth(1, 40)
        self.contact()

    def contact(self):
        self.button.clicked.connect(self.addRow)
        self.button_file.clicked.connect(self.choice_file)
        self.clear_button_browser.clicked.connect(self.clear_textBrowser)
        self.clear_button_table.clicked.connect(self.clear_table)

    def clear_textBrowser(self):
        self.textBrowser.clear()

    def clear_table(self):
        self.tableWidget.clear()

    def choice_file(self):
        filename, filetype = QFileDialog.getOpenFileName(self, "Выбрать файл", ".", "XLSX Files(*.xlsx)")
        self.textBrowser.append("Путь к файлу:")
        self.textBrowser.append(filename)
        self.textBrowser.append('*' * 50)
        self.filename_for_chice = filename
        print(self.filename_for_chice)
        self.load_data()

    def addRow(self):
        numRows = self.tableWidget.rowCount()
        self.tableWidget.setRowCount(numRows + 1)

    def load_data(self):
        path = str(self.filename_for_chice)
        workbook = openpyxl.load_workbook(path)
        sheet = workbook.active

        self.tableWidget.setRowCount(sheet.max_row)
        self.tableWidget.setColumnCount(sheet.max_column)

        list_values = list(sheet.values)
        self.tableWidget.setHorizontalHeaderLabels(list_values[0])

        row_index = 0
        for value_tuple in list_values[1:]:
            col_index = 0
            for value in value_tuple:
                self.tableWidget.setItem(row_index, col_index, QTableWidgetItem(str(value)))
                col_index += 1
            row_index += 1


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    mainwindow.show()
    sys.exit(app.exec_())
