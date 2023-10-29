import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QTableWidgetItem, QMainWindow, QFileDialog
import openpyxl
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout, QFormLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt


class MainWindow(QMainWindow):
    # интерфейс
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("untitledmain.ui", self)
        self.figure = plt.figure()
        self.canvas = FigureCanvas(plt.figure())
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.verticalLayout.addWidget(self.toolbar)
        self.verticalLayout.addWidget(self.canvas)
        self.setLayout(self.verticalLayout)
        self.tableWidget.setColumnWidth(0, 40)
        self.tableWidget.setColumnWidth(1, 40)
        self.spin.setMaximum(10000)
        self.contact()

    # взаимодействие интерфейса с методами
    def contact(self):
        self.button_file.clicked.connect(self.choice_file)
        self.clear_button_browser.clicked.connect(self.clear_textBrowser)
        self.clear_button_table.clicked.connect(self.clear_table)
        self.run_button.clicked.connect(self.show_graphic)
        self.spin.valueChanged.connect(self.change)

    # *****************************************************************************
    # получение значений из таблицы по X и по Y
    def get_Value_table(self):
        self.value_table_X = []
        self.value_table_Y = []
        for i in range(self.tableWidget.rowCount()):
            self.value_table_X.append(int(self.tableWidget.item(i, 0).text()))
            self.value_table_Y.append(int(self.tableWidget.item(i, 1).text()))
        self.textBrowser.append(f'X: {", ".join(list(map(str, self.value_table_X)))}')
        self.textBrowser.append(f'Y: {", ".join(list(map(str, self.value_table_Y)))}')

    # добавление строчки
    def change(self):
        self.tableWidget.setRowCount(int(self.spin.text()))
        self.dataExtent()

    # получение количества заполненных строк в таблице(количество точек)
    def dataExtent(self):
        self.maxRow = self.maxCol = -1
        for row in range(self.tableWidget.rowCount()):
            for col in range(self.tableWidget.columnCount()):
                item = self.tableWidget.item(row, col)
                if not item or not item.text():
                    continue
                self.maxRow = row
        self.maxRow += 1
        print('maxRow:', self.maxRow)  # КОЛИЧЕСТВО СТРОЧЕК

    # выбор файла и запись его пути в тест браузер
    def choice_file(self):
        filename, filetype = QFileDialog.getOpenFileName(self, "Выбрать файл", ".", "XLSX Files(*.xlsx)")
        self.textBrowser.append("Путь к файлу:")
        self.textBrowser.append(filename)
        self.textBrowser.append('*' * 50)
        self.filename_for_chice = filename
        self.load_data()
        self.dataExtent()
        self.maxRow_in_spin()
        self.get_Value_table()

    # запись количества строчек в спин
    def maxRow_in_spin(self):
        self.spin.setValue(self.maxRow)

    # запись данных из файла в таблицу
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

    # очищение текст браузера
    def clear_textBrowser(self):
        self.textBrowser.clear()

    # очистка таблицы
    def clear_table(self):
        self.tableWidget.clear()
        self.spin.setValue(0)

    # график
    def show_graphic(self):
        self.get_Value_table()
        plt.plot(self.value_table_X, self.value_table_Y)
        self.canvas.draw()

# запуск
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    mainwindow.show()
    sys.exit(app.exec_())
