from PySide6.QtWidgets import QApplication, QWidget, QCheckBox, QMessageBox,\
    QPushButton, QLabel, QTextBrowser, QTextEdit, QVBoxLayout, QLineEdit,\
    QButtonGroup, QListView, QLineEdit
from PySide6.QtGui import QCloseEvent, QPixmap, QIcon, QColor, QPalette
import sys
import random


class GeneratorWindow(QWidget):

    normal_char = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
                   "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                   "u", "v", "x", "y", "z"]

    temp = []
    temp2 = []

    def __init__(self):
        super().__init__()

        self.image()
        self.checkboxes()
        self.outputbox_inputbox()
        self.pushbuttons()
        self.send_signal()
        self.show_screen()

    def show_screen(self):
        # config of window and icons
        width = 300
        height = 400
        self.setFixedSize(width, height)
        self.setWindowTitle("Password Generator")
        icon = r"C:\Users\tomas\PycharmProjects\UdemyKurs\nowy_folder2\padlock2.png"
        self.setWindowIcon(QIcon(icon))
        self.setStyleSheet("background-color:lightblue;")

        self.show()

    def image(self):

        pix_label = QLabel(self)
        image = QPixmap(r"C:\Users\tomas\PycharmProjects\UdemyKurs\nowy_folder2\padlock2.png")
        pix_label.setPixmap(image)
        pix_label.move(150, 200)
        # version information
        version = QLabel(self)
        version.setText("v.1.0.2")
        version.move(3, 3)
        version.setStyleSheet("background-color: yellow")

    def outputbox_inputbox(self):
        # Display and configure box where passes are shown
        self.field = QTextEdit(self)
        self.field.resize(200, 20)
        self.field.move(50, 150)
        self.field.setReadOnly(True)
        # Field to input data
        self.field_input = QLineEdit(self)
        self.field_input.move(10, 300)
        self.field_input.resize(80, 20)
        self.field_input.setText("10")
        self.field_label = QLabel(self)
        self.field_label.setText("Password length (10-20)")
        self.field_label.move(10, 280)

    def checkboxes(self):
        # Display and configure checkboxes
        self.checkbox_1 = QCheckBox("Add numbers", self)
        self.checkbox_1.move(10, 330)
        self.checkbox_2 = QCheckBox("Add special signs", self)
        self.checkbox_2.move(10, 350)
        self.checkbox_3 = QCheckBox("Add big letters", self)
        self.checkbox_3.move(10, 370)

        # WITH FOR METHOD
        # checkboxes = ["Add numbers", "Add special signs", "Add big letters"]
        # lay = QVBoxLayout(self)
        # self.group = QButtonGroup()
        # i = 0
        # for check in checkboxes:
        #     button = QCheckBox("{}".format(check), self)
        #     lay.addWidget(button)
        #     self.group.addButton(button, i)
        #     i += 1
        #
        # self.group.setExclusive(False)
        # self.group.idClicked.connect(self.show_something)

    def pushbuttons(self):

        # Quit_Button
        self.exit_btn = QPushButton("Quit", self)
        self.exit_btn.move(220, 370)

        # Generate_Button
        self.gen_btn = QPushButton("Generate", self) # , clicked=self.show_something
        self.gen_btn.move(106, 180)

    def closeEvent(self, event: QCloseEvent):
        # Close Event
        should_close = QMessageBox.question(self, "Closing", "Do you want to close?",
                                            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if should_close == QMessageBox.Yes:
            event.accept() # Note: sys.exit() works the same
        else:
            event.ignore()

    def send_signal(self):
        # Exit button
        self.exit_btn.clicked.connect(QApplication.instance().quit)
        # Generate button
        self.gen_btn.clicked.connect(self.show_something)

        # clicked
        self.checkbox_1.clicked.connect(self.add_numbers)
        self.checkbox_2.clicked.connect(self.special_sign)
        self.checkbox_3.clicked.connect(self.big_letters)


    def show_something(self, signal):
        if signal == False:
            a = self.generate_password()
            self.field.setText("{}".format(a))

    def add_numbers(self, signal):
        numbers = [i for i in range(0, 10)]
        if signal == True:
            GeneratorWindow.normal_char.extend(numbers)
        elif signal == False:
            for number in numbers:
                GeneratorWindow.normal_char.remove(number)
        print(GeneratorWindow.normal_char)

    def big_letters(self, signal):
        letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I",
                    "J", "K", "M", "N", "L", "O", "P", "Q", "R",
                    "S", "T", "U", "V", "X", "Y", "Z"]
        if signal == True:
            for i in range(20):
                a = random.choice(GeneratorWindow.normal_char)
                a = str(a)
                GeneratorWindow.normal_char.append(a.upper())
                GeneratorWindow.temp.append(a.upper())
                GeneratorWindow.temp2.append(a)
                GeneratorWindow.normal_char.remove(a)
        elif signal == False:
            for use in GeneratorWindow.temp2:
                GeneratorWindow.normal_char.append(use)
            GeneratorWindow.temp2.clear()
            for use in GeneratorWindow.temp:
                GeneratorWindow.normal_char.remove(use)
            GeneratorWindow.temp.clear()
        print(GeneratorWindow.normal_char)

    def special_sign(self, signal):
        signs = ["!", "@", "#", "$", "%", "?", "/", "[", "]", "!", "@", "#", "$", "%", "?", "/", "[", "]"]
        if signal == True:
            GeneratorWindow.normal_char.extend(signs)
        elif signal == False:
            for sign in signs:
                GeneratorWindow.normal_char.remove(sign)
        print(GeneratorWindow.normal_char)

    def generate_password(self):
        password = ""
        chars = GeneratorWindow.normal_char
        a = self.field_input.text()
        i = 0
        try:
            a = int(a)
            while i < a:
                if a < 10 or a > 20:
                    QMessageBox.critical(self, "Error", "Length must be beetwen 10-20")
                    break
                char = random.choice(chars)
                char = str(char)
                password += char
                i += 1
        except Exception:
            pass
        return password


if __name__ == "__main__":

    win = QApplication(sys.argv)

    generator_window = GeneratorWindow()

    win.exec()
