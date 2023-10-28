# importing various libraries
import sys
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout, QFormLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import random
from scipy.optimize import curve_fit
from numpy import array, exp



# main window
# which inherits QDialog
class Window(QDialog):
    # constructor
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.button = QPushButton('Plot')






        self.figure = plt.figure()

        self.canvas = FigureCanvas(plt.figure())

        self.toolbar = NavigationToolbar(self.canvas, self)

        layout = QFormLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        layout.addWidget(self.button)
        self.setLayout(layout)








        self.con()


    def con(self):
        self.button.clicked.connect(self.plot)

    # action called by the push button
    def plot(self):
        # random data
        values_y = array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 9, 8, 6, 5])
        values_x = array(range(len(values_y)))
        print(values_x)

        def mapping1(values_x, a, b, c):
            return a * values_x ** 2 + b * values_x + c

        # using the curve_fit() function
        args, covar = curve_fit(mapping1, values_x, values_y)
        print("Arguments: ", args)
        print("Co-Variance: ", covar)

        args, _ = curve_fit(mapping1, values_x, values_y)
        a, b, c = args[0], args[1], args[2]
        y_fit1 = a * values_x ** 2 + b * values_x + c

        plt.plot(values_x, values_y, 'bo', label="y - original")
        plt.plot(values_x, y_fit1, label="y = a * x^2 + b * x + c")
        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend(loc='best', fancybox=True, shadow=True)
        plt.grid(True)

        # refresh canvas
        self.canvas.draw()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Window()
    main.show()
    sys.exit(app.exec_())
