import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Убираем стандартную шапку
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setWindowTitle("Запуск аварийной системы самоуничтожения компьютера")
        self.resize(800, 200)

        # Создаём кастомную шапку
        self.header = QWidget(self)  # Виджет для шапки
        self.header.setFixedHeight(50)  # Высота шапки
        self.header.setStyleSheet("""
            background-color: #333333;  /* Темный фон для шапки */
            color: white;
        """)

        # Создаем лейаут для шапки
        header_layout = QHBoxLayout(self.header)
        self.title = QLabel("Запуск аварийной системы самоуничтожения компьютера", self)  # Название в шапке
        self.close_button = QPushButton("X", self)  # Кнопка для закрытия окна
        self.close_button.setFixedSize(30, 30)  # Размер кнопки увеличен

        # Настрйка кнопки для закрытия окна
        self.close_button.clicked.connect(self.close)

        # Добавляем элементы в шапку
        header_layout.addWidget(self.title)
        header_layout.addStretch()  # Растягиваем до конца, чтобы кнопка была справа
        header_layout.addWidget(self.close_button)

        # Создаём кнопку и метку
        self.button = QPushButton("Запуск")
        self.button.setFixedSize(110, 65)

        self.label = QLabel("Внимание!\nВы запустили программу запуска самоуничтожения\nперсонально компьютера")

        # Создаём основной лейаут
        layout = QVBoxLayout(self)
        layout.addWidget(self.header)  # Добавляем шапку в основной лейаут
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        layout.setAlignment(self.button, Qt.AlignmentFlag.AlignHCenter)

        self.setLayout(layout)

        # Подключаем кнопку к методу on_button_click
        self.button.clicked.connect(self.on_button_click)

        # Применяем стили
        self.setStyleSheet("""
            QWidget {
                background-color: #2d2d2d;
                color: white;
                font-family: 'Arial';
            }
            QLabel {
                font-size: 14px;
                text-align: center;
                padding: 10px;
            }
            QPushButton {
                background-color: #ff0000;
                color: white;
                border: none;
                padding: 15px 16px;
                text-align: center;
                font-size: 16px;
                border-radius: 6px;
                margin-top: 20px;
            }
            QPushButton:hover {
                background-color: #ffff00;
                color: black;
            }
            QPushButton:pressed {
                background-color: #3e8e41;
            }
        """)

    def on_button_click(self):
        self.label.setText("Система активирована")


app = QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec())