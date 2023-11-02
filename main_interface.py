from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Function_approximation(object):
    def setupUi(self, Function_approximation):
        Function_approximation.setObjectName("Function_approximation")
        Function_approximation.resize(788, 591)
        Function_approximation.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(Function_approximation)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 951, 701))
        self.tabWidget.setStyleSheet("background-color: rgb(207, 207, 207);\n"
                                     "border-color: rgb(207, 207, 207);")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.textBrowser = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser.setGeometry(QtCore.QRect(200, 10, 581, 211))
        self.textBrowser.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                       "border-radius: 10px;\n"
                                       "font-size: 12px;\n"
                                       "color: #0d7907;\n"
                                       "font: 1.2rem \"Fira Sans\", sans-serif;\n"
                                       "border:0.5px solid black;")
        self.textBrowser.setObjectName("textBrowser")
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 140, 200))
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                       "border-radius: 10px;\n"
                                       "font-size: 15px;\n"
                                       "color: #0d7907;\n"
                                       "font: 1.2rem \"Fira Sans\", sans-serif;\n"
                                       "border:0.5px solid black;")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.spin = QtWidgets.QSpinBox(self.tab)
        self.spin.setGeometry(QtCore.QRect(10, 220, 140, 25))
        self.spin.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                "border-radius: 10px;\n"
                                "font-size: 12px;\n"
                                "color: #0d7907;\n"
                                "font: 1.2rem \"Fira Sans\", sans-serif;\n"
                                "border:0.5px solid black;")
        self.spin.setObjectName("spin")
        self.button_file = QtWidgets.QPushButton(self.tab)
        self.button_file.setGeometry(QtCore.QRect(10, 255, 141, 23))
        self.button_file.setStyleSheet("QPushButton {\n"
                                       "    background-color: rgb(255, 255, 255);\n"
                                       "    border-radius: 10px;\n"
                                       "    font-size: 15px;\n"
                                       "    color: #0d7907;\n"
                                       "    font: 1.2rem \"Fira Sans\", sans-serif;\n"
                                       "    border:0.5px solid black;\n"
                                       "}\n"
                                       "QPushButton:hover {\n"
                                       "    background-color: lightgreen;\n"
                                       "}")
        self.button_file.setObjectName("button_file")
        self.clear_button_table = QtWidgets.QPushButton(self.tab)
        self.clear_button_table.setGeometry(QtCore.QRect(10, 290, 140, 25))
        self.clear_button_table.setStyleSheet("QPushButton {\n"
                                              "    background-color: rgb(255, 255, 255);\n"
                                              "    border-radius: 10px;\n"
                                              "    font-size: 15px;\n"
                                              "    color: #0d7907;\n"
                                              "    font: 1.2rem \"Fira Sans\", sans-serif;\n"
                                              "    border:0.5px solid black;\n"
                                              "}\n"
                                              "QPushButton:hover {\n"
                                              "    background-color: lightgreen;\n"
                                              "}")
        self.clear_button_table.setObjectName("clear_button_table")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(220, 270, 561, 291))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.layoutWidget = QtWidgets.QWidget(self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 340, 141, 61))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.linear_radioButton = QtWidgets.QRadioButton(self.layoutWidget)
        self.linear_radioButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                              "border-radius: 10px;\n"
                                              "font-size: 15px;\n"
                                              "color: #0d7907;\n"
                                              "font: 1.2rem \"Fira Sans\", sans-serif;\n"
                                              "border:0.5px solid black;")
        self.linear_radioButton.setObjectName("linear_radioButton")
        self.verticalLayout_3.addWidget(self.linear_radioButton)
        self.nonlinear_radioButton = QtWidgets.QRadioButton(self.layoutWidget)
        self.nonlinear_radioButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                 "border-radius: 10px;\n"
                                                 "font-size: 15px;\n"
                                                 "color: #0d7907;\n"
                                                 "font: 1.2rem \"Fira Sans\", sans-serif;\n"
                                                 "border:0.5px solid black;")
        self.nonlinear_radioButton.setObjectName("nonlinear_radioButton")
        self.verticalLayout_3.addWidget(self.nonlinear_radioButton)
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(10, 321, 181, 20))
        self.label.setStyleSheet("border-radius: 10px;\n"
                                 "font-size: 12px;\n"
                                 "font: 1.2rem \"Fira Sans\", sans-serif;")
        self.label.setObjectName("label")
        self.clear_button_browser = QtWidgets.QPushButton(self.tab)
        self.clear_button_browser.setGeometry(QtCore.QRect(270, 234, 440, 21))
        self.clear_button_browser.setStyleSheet("QPushButton {\n"
                                                "    background-color: rgb(255, 255, 255);\n"
                                                "    border-radius: 10px;\n"
                                                "    font-size: 15px;\n"
                                                "    color: #0d7907;\n"
                                                "    font: 1.2rem \"Fira Sans\", sans-serif;\n"
                                                "    border:0.5px solid black;\n"
                                                "}\n"
                                                "QPushButton:hover {\n"
                                                "    background-color: lightgreen;\n"
                                                "}")
        self.clear_button_browser.setObjectName("clear_button_browser")
        self.comboBox = QtWidgets.QComboBox(self.tab)
        self.comboBox.setGeometry(QtCore.QRect(10, 410, 201, 41))
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                    "border-radius: 10px;\n"
                                    "font-size: 12px;\n"
                                    "color: #0d7907;\n"
                                    "font: 1.2rem \"Fira Sans\", sans-serif;\n"
                                    "border:0.5px solid black;")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.compare_checkBox = QtWidgets.QCheckBox(self.tab)
        self.compare_checkBox.setGeometry(QtCore.QRect(30, 460, 121, 31))
        self.compare_checkBox.setStyleSheet("font-size: 15px;\n"
                                            "border-radius: 20px;\n"
                                            "color: #0d7907;\n"
                                            "font: 1.2rem \"Fira Sans\", sans-serif;")
        self.compare_checkBox.setObjectName("compare_checkBox")
        self.run_button = QtWidgets.QPushButton(self.tab)
        self.run_button.setGeometry(QtCore.QRect(10, 500, 200, 61))
        self.run_button.setStyleSheet("QPushButton {\n"
                                      "    background-color: rgb(255, 255, 255);\n"
                                      "    border-radius: 10px;\n"
                                      "    font-size: 25px;\n"
                                      "    color: #D2691E;\n"
                                      "    font: 1.2rem \"Fira Sans\", sans-serif;\n"
                                      "    border:0.5px solid black;\n"
                                      "}\n"
                                      "QPushButton::hover{\n"
                                      "    background-color : lightgreen;\n"
                                      "}\n"
                                      "")
        self.run_button.setObjectName("run_button")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.view = QtWidgets.QTableView(self.tab_2)
        self.view.setGeometry(QtCore.QRect(10, 10, 381, 551))
        self.view.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                "border-radius: 10px;\n"
                                "color: #0d7907;\n"
                                "font: 1.2rem \"Fira Sans\", sans-serif;\n"
                                "border:0.5px solid black;")
        self.view.setObjectName("view")
        self.table_for_db = QtWidgets.QTableWidget(self.tab_2)
        self.table_for_db.setGeometry(QtCore.QRect(400, 270, 380, 291))
        self.table_for_db.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "border-radius: 10px;\n"
                                        "color: #0d7907;\n"
                                        "font: 1.2rem \"Fira Sans\", sans-serif;\n"
                                        "border:0.5px solid black;")
        self.table_for_db.setObjectName("table_for_db")
        self.table_for_db.setColumnCount(0)
        self.table_for_db.setRowCount(0)
        self.del_button = QtWidgets.QPushButton(self.tab_2)
        self.del_button.setGeometry(QtCore.QRect(445, 80, 300, 50))
        self.del_button.setStyleSheet("QPushButton {\n"
                                      "    background-color: rgb(255, 255, 255);\n"
                                      "    border-radius: 10px;\n"
                                      "    font-size: 20px;\n"
                                      "    color: #0d7907;\n"
                                      "    font: 1.2rem \"Fira Sans\", sans-serif;\n"
                                      "    border:0.5px solid black;\n"
                                      "}\n"
                                      "QPushButton:hover {\n"
                                      "    background-color: lightgreen;\n"
                                      "}")
        self.del_button.setObjectName("del_button")
        self.save_button = QtWidgets.QPushButton(self.tab_2)
        self.save_button.setGeometry(QtCore.QRect(445, 140, 300, 50))
        self.save_button.setStyleSheet("QPushButton {\n"
                                       "    background-color: rgb(255, 255, 255);\n"
                                       "    border-radius: 10px;\n"
                                       "    font-size: 20px;\n"
                                       "    color: #0d7907;\n"
                                       "    font: 1.2rem \"Fira Sans\", sans-serif;\n"
                                       "    border:0.5px solid black;\n"
                                       "}\n"
                                       "QPushButton:hover {\n"
                                       "    background-color: lightgreen;\n"
                                       "}")
        self.save_button.setObjectName("save_button")
        self.change_button = QtWidgets.QPushButton(self.tab_2)
        self.change_button.setGeometry(QtCore.QRect(445, 200, 300, 50))
        self.change_button.setStyleSheet("QPushButton {\n"
                                         "    background-color: rgb(255, 255, 255);\n"
                                         "    border-radius: 10px;\n"
                                         "    font-size: 20px;\n"
                                         "    color: #0d7907;\n"
                                         "    font: 1.2rem \"Fira Sans\", sans-serif;\n"
                                         "    border:0.5px solid black;\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "    background-color: lightgreen;\n"
                                         "}")
        self.change_button.setObjectName("change_button")
        self.id_spin = QtWidgets.QSpinBox(self.tab_2)
        self.id_spin.setGeometry(QtCore.QRect(445, 20, 300, 50))
        self.id_spin.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                   "border-radius: 10px;\n"
                                   "font-size: 20px;\n"
                                   "color: #0d7907;\n"
                                   "font: 1.2rem \"Fira Sans\", sans-serif;\n"
                                   "border:0.5px solid black;")
        self.id_spin.setObjectName("id_spin")
        self.tabWidget.addTab(self.tab_2, "")
        Function_approximation.setCentralWidget(self.centralwidget)

        self.retranslateUi(Function_approximation)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Function_approximation)

    def retranslateUi(self, Function_approximation):
        _translate = QtCore.QCoreApplication.translate
        Function_approximation.setWindowTitle(_translate("Function_approximation", "MainWindow"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Function_approximation", "X"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Function_approximation", "Y"))
        self.button_file.setText(_translate("Function_approximation", "Выбор файла"))
        self.clear_button_table.setText(_translate("Function_approximation", "Очистить таблицу"))
        self.linear_radioButton.setText(_translate("Function_approximation", "Линейная"))
        self.nonlinear_radioButton.setText(_translate("Function_approximation", "Нелинейная"))
        self.label.setText(_translate("Function_approximation", "Выберите вид аппроксимации:"))
        self.clear_button_browser.setText(_translate("Function_approximation", "Очисть браузер"))
        self.comboBox.setItemText(0, _translate("Function_approximation", "Квадратичная: \'y = a*x^2+b*x+c\'"))
        self.comboBox.setItemText(1,
                                  _translate("Function_approximation", "Кубическая: \'y = a*x^3 + b*x^2 + c*x + d\'"))
        self.comboBox.setItemText(2, _translate("Function_approximation", "Степенная:  \'y = k*x^n\'"))
        self.comboBox.setItemText(3,
                                  _translate("Function_approximation", "Экспоненциальная I типа: \'y = a*exp(b^x)\'"))
        self.comboBox.setItemText(4, _translate("Function_approximation", "Экспоненциальная II типа: \'y = a*b^x\'"))
        self.comboBox.setItemText(5, _translate("Function_approximation", "Логарифмическая: \'y = b + a*log(x)\'"))
        self.comboBox.setItemText(6, _translate("Function_approximation", "Гиперболическая:  \'y = b+a/x\'"))
        self.compare_checkBox.setText(_translate("Function_approximation", "Сравнить"))
        self.run_button.setText(_translate("Function_approximation", "RUN"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Function_approximation", "Tab 1"))
        self.del_button.setText(_translate("Function_approximation", "Удалить"))
        self.save_button.setText(_translate("Function_approximation", "Сохранить"))
        self.change_button.setText(_translate("Function_approximation", "Загрузить"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Function_approximation", "Tab 2"))
