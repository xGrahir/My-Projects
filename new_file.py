from PySide6.QtWidgets import QApplication, QWidget, QLineEdit, QLabel, QPushButton, QMessageBox
from PySide6.QtGui import QCloseEvent, QIcon
import sys


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.line_edit()
        self.labels()
        self.process_button()
        self.screen_settings()

    def screen_settings(self):
        width = 200
        heigth = 250
        self.setFixedSize(width, heigth)
        self.setWindowTitle("CM")
        self.setStyleSheet("background-color: lightblue")
        # Icon
        icon_path = "ico2.png"
        self.setWindowIcon(QIcon(icon_path))

        self.show()

    def line_edit(self):
        # text boxes
        self.line_edit1 = QLineEdit(self)
        self.line_edit1.resize(110, 20)
        self.line_edit1.move((200-110)/2, 30)
        # -----------------------------------------------------
        self.line_edit2 = QLineEdit(self)
        self.line_edit2.resize(110, 20)
        self.line_edit2.move((200 - 110)/2, 70)
        self.line_edit2.setText("0.25")  # 0.25 is default
        # self.line_edit2.setAlignment(Qt.AlignCenter)
        # -----------------------------------------------------
        self.line_edit3 = QLineEdit(self)
        self.line_edit3.resize(110, 20)
        self.line_edit3.move((200 - 110) / 2, 110)
        # -----------------------------------------------------
        self.line_edit4 = QLineEdit(self)
        self.line_edit4.resize(110, 20)
        self.line_edit4.move((200 - 110) / 2, 180)
        self.line_edit4.setReadOnly(True)
        self.line_edit4.setStyleSheet("background-color: #f0eec2")
        # layout = QVBoxLayout()
        # for line in line_edit:
        #     line = QLineEdit(self)
        #     layout.addWidget(line)

    def labels(self):
        # Lables: 1. Product's price, 2. Monthly interest, 3. Number of months
        line1 = QLabel(self)
        line1.setText("Product's price:")
        line1.setStyleSheet("font: bold")
        line1.move((200 - 150) / 2, 10)
        # -----------------------------------------
        line2 = QLabel(self)
        line2.setText("Monthly interest (0.25 - 0.5):")
        line2.setStyleSheet("font: bold")
        line2.move((200 - 150) / 2, 50)
        # -----------------------------------------
        line3 = QLabel(self)
        line3.setText("Number of months:")
        line3.setStyleSheet("font: bold")
        line3.move((200 - 150) / 2, 90)
        # -----------------------------------------
        self.line4 = QLabel(self)
        self.line4.setStyleSheet("font: bold")
        self.line4.move((200 - 150) / 2, 210)

    def process_button(self):
        # generate process button
        proc_btn = QPushButton(self)
        proc_btn.setText("COUNT")
        proc_btn.resize(70, 20)
        proc_btn.move((200 - 70) / 2, 150)
        proc_btn.clicked.connect(self.count_method)

    def close_event(self, event: QCloseEvent):
        # Close program
        should_close = QMessageBox.question(self, "Closing", "Do you want to close?",
                                            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if should_close == QMessageBox.Yes:
            event.accept()  # Note: sys.exit() works the same
        else:
            event.ignore()

    def numbers(self):
        while True:
            k = self.line_edit1.text()
            r = self.line_edit2.text()
            n = self.line_edit3.text()
            if not k or not n or not r:
                QMessageBox.critical(self, "Error", "Fill the all fields")
                break
            else:
                try:
                    k = float(k)
                    n = int(n)
                    r = float(r)
                except ValueError:
                    QMessageBox.critical(self, "Error", "Cannot convert data. Maybe try use '.' instead of ',' or "
                                                        "number of months isn't integer.")
                    break
                else:
                    return k, n, r

    def logic(self):
        k, n, r = self.numbers()
        while True:
            if k < 0:
                QMessageBox.critical(self, "Error", "Product cost cannot be minus")
                break
            if n < 0:
                QMessageBox.critical(self, "Error", "Number of month cannot be minus")
                break
            if r < 0.25 or r > 0.5:
                QMessageBox.critical(self, "Error", "Interest cannot be lower than 0.25 and bigger than 0.5")
                break
            try:
                r = r/100
                n += 1
                p = 0.19
                # Counting
                a = r*(1-p)*k
                b = pow((1+r*(1-p)), n)
                c = (1+r*(1-p))
                s = a/(b-c)
            except ZeroDivisionError:
                QMessageBox.critical(self, "Error", "Division by zero occurred, change parameters")
            else:
                return s

    def count_method(self, signal):
        if signal is False:
            s = self.logic()
            self.line4.setText("You need to save monthly")
            self.line4.setStyleSheet("font:bold")
            self.line4.adjustSize()
            self.line_edit4.setText("{}".format(round(s, 2)))


if __name__ == "__main__":

    system = QApplication(sys.argv)

    main_prog = MainWindow()

    system.exec()
