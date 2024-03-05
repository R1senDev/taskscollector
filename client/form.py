import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit

class TaskSubmissionApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Установка заголовка и фиксированного размера окна
        self.setWindowTitle('Отправка задания')
        self.setFixedSize(150, 100)

        # Создание вертикального слоя для размещения виджетов
        vbox = QVBoxLayout()

        # Создание горизонтального слоя для текстовых полей
        hbox_task = QHBoxLayout()
        self.task_input = QLineEdit()
        self.task_input.setPlaceholderText('Номер задания')
        hbox_task.addWidget(self.task_input)
        vbox.addLayout(hbox_task)

        # Создание горизонтального слоя для текстового поля ответа
        hbox_answer = QHBoxLayout()
        self.answer_input = QLineEdit()
        self.answer_input.setPlaceholderText('Ответ на задание')
        hbox_answer.addWidget(self.answer_input)
        vbox.addLayout(hbox_answer)

        # Создание кнопки и добавление ее в вертикальный слой
        self.submit_button = QPushButton('Отправить')
        self.submit_button.clicked.connect(self.submit_task)
        vbox.addWidget(self.submit_button)

        # Установка главного слоя окна
        self.setLayout(vbox)

    def submit_task(self):
        task_number = self.task_input.text()
        answer = self.answer_input.text()
        # Здесь можно добавить код для отправки задания на сервер или обработки ответа
        print(f'Задание {task_number} отправлено с ответом: {answer}')

def main():
    app = QApplication(sys.argv)
    ex = TaskSubmissionApp()
    ex.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
