import sys
from PySide6.QtWidgets import QApplication, QMainWindow,  QMessageBox
from PySide6.QtGui import QAction





class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Пример верхнего меню")
        self.setGeometry(100, 100, 600, 400)

        # Создаем меню
        self.create_menu()

    def create_menu(self):
        menu_bar = self.menuBar()  # Создание меню

        # Создаем меню "Файл"
        file_menu = menu_bar.addMenu("Файл")

        # Создаем действия для меню "Файл"
        new_action = QAction("Создать", self)
        new_action.triggered.connect(self.new_file)  # Подключаем действие

        open_action = QAction("Открыть", self)
        open_action.triggered.connect(self.open_file)

        save_action = QAction("Сохранить", self)
        save_action.triggered.connect(self.save_file)

        exit_action = QAction("Выход", self)
        exit_action.triggered.connect(self.exit_application)

        # Добавляем действия в меню "Файл"
        file_menu.addAction(new_action)
        file_menu.addAction(open_action)
        file_menu.addAction(save_action)
        file_menu.addSeparator()  # Разделитель
        file_menu.addAction(exit_action)

        # Можно добавить другие меню (например, "Правка", "Справка" и т.д.)
        edit_menu = menu_bar.addMenu("Правка")
        about_action = QAction("О программе", self)
        about_action.triggered.connect(self.show_about)
        edit_menu.addAction(about_action)

    def new_file(self):
        QMessageBox.information(self, "Информация", "Создать новый файл")

    def open_file(self):
        QMessageBox.information(self, "Информация", "Открыть файл")

    def save_file(self):
        QMessageBox.information(self, "Информация", "Сохранить файл")

    def exit_application(self):
        self.close()

    def show_about(self):
        QMessageBox.information(self, "О программе", "Это простой пример с верхним меню.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
