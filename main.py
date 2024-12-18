import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from main_design import Ui_MainWindow  # Импортируем UI из сгенерированного файла
import pandas as pd

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Подключаем UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Привязываем функционал к кнопкам
        self.ui.push_to_csv.clicked.connect(self.write_to_csv)
        self.ui.but_hist.clicked.connect(self.show_history)
        self.ui.but_anal.clicked.connect(self.analyze_data)


    def write_to_csv(self):
        df = pd.read_csv("history.csv")
        operation = self.ui.list_widget.currentText()
        money_value = self.ui.input_field.text()
        date = self.ui.date_edit.date().toString("dd.MM.yyyy")
        df.loc[-1] = [money_value, date, operation]
        df.to_csv("history.csv", index=False)

    def show_history(self):
        """
        Функция для отображения истории записей.
        """
        QMessageBox.information(self, "История", "Функция истории записей пока не реализована.")

    def analyze_data(self):
        """
        Функция для анализа данных.
        """
        QMessageBox.information(self, "Анализ", "Функция анализа данных пока не реализована.")

# Точка входа в приложение
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
