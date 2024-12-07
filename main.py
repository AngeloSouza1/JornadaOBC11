import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox, QHBoxLayout
)
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt, QTimer
from modulo_sequencia import sequencia_dos_anciaos


class KnightSequenceApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("A Jornada do Cavaleiro de Código 🏰")
        self.setGeometry(100, 100, 600, 400)
        self.init_ui()

    def init_ui(self):
        # Background
        self.background_label = QLabel(self)
        self.background_label.setPixmap(QPixmap("assets/knight_background.png"))
        self.background_label.setScaledContents(True)
        self.background_label.setGeometry(0, 0, 600, 400)

        # Layout principal
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        self.main_layout = QVBoxLayout(central_widget)
        self.main_layout.setAlignment(Qt.AlignCenter)

        # Widgets ocultos inicialmente
        self.widgets_container = QWidget(self)
        self.widgets_layout = QVBoxLayout(self.widgets_container)
        self.widgets_layout.setAlignment(Qt.AlignCenter)

        # Espaço flexível acima dos widgets para centralização vertical
        self.widgets_layout.addStretch()

        # Label de instrução
        self.input_label = QLabel("Digite a posição n e a dupla inicial a e b (ex: n=5, a=2, b=3):")
        self.input_label.setFont(QFont("Helvetica", 14))
        self.input_label.setStyleSheet("color: #FFD700; background-color: #000000; padding: 10px; border-radius: 10px;")
        self.widgets_layout.addWidget(self.input_label, alignment=Qt.AlignCenter)

        # Caixa de texto para entrada da posição n
        self.n_input = QLineEdit(self)
        self.n_input.setFont(QFont("Helvetica", 14))
        self.n_input.setPlaceholderText("Digite n (ex: 5)")
        self.n_input.setFixedWidth(300)
        self.n_input.setStyleSheet(
            "padding: 5px; border: 2px solid #0078d7; border-radius: 10px; background-color: #f4f4f4; color: #333;"
        )
        self.widgets_layout.addWidget(self.n_input, alignment=Qt.AlignCenter)

        # Caixa de texto para entrada da dupla inicial a e b
        self.ab_input = QLineEdit(self)
        self.ab_input.setFont(QFont("Helvetica", 14))
        self.ab_input.setPlaceholderText("Digite a e b separados por espaço (ex: 2 3)")
        self.ab_input.setFixedWidth(300)
        self.ab_input.setStyleSheet(
            "padding: 5px; border: 2px solid #0078d7; border-radius: 10px; background-color: #f4f4f4; color: #333;"
        )
        self.widgets_layout.addWidget(self.ab_input, alignment=Qt.AlignCenter)

        # Botão de calcular com efeito hover
        self.calculate_button = QPushButton("Calcular Sequência", self)
        self.calculate_button.setFont(QFont("Helvetica", 14, QFont.Bold))
        self.calculate_button.setFixedSize(200, 50)
        self.calculate_button.setStyleSheet(
            """
            QPushButton {
                background-color: transparent;
                color: white;
                border: 2px solid #28a745;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #000000;
                color: #28a745;
            }
            """
        )
        self.calculate_button.clicked.connect(self.calculate_sequence)
        self.widgets_layout.addWidget(self.calculate_button, alignment=Qt.AlignCenter)

        # Espaço flexível abaixo dos widgets para centralização vertical
        self.widgets_layout.addStretch()

        self.main_layout.addWidget(self.widgets_container, alignment=Qt.AlignCenter)

        # Label de resultado oculto inicialmente
        self.result_label = QLabel("", self)
        self.result_label.setFont(QFont("Helvetica", 16, QFont.Bold))
        self.result_label.setStyleSheet("color: #00FF00; background-color: #000000; padding: 10px; border-radius: 10px;")
        self.result_label.setAlignment(Qt.AlignCenter)
        self.result_label.hide()
        self.main_layout.addWidget(self.result_label, alignment=Qt.AlignCenter)

        # Botão Iniciar no rodapé com efeito hover
        self.start_button = QPushButton("Iniciar", self)
        self.start_button.setFont(QFont("Helvetica", 14, QFont.Bold))
        self.start_button.setFixedSize(200, 50)
        self.start_button.setStyleSheet(
            """
            QPushButton {
                background-color: transparent;
                color: white;
                border: 2px solid #28a745;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #000000;
                color: #28a745;
            }
            """
        )
        self.start_button.clicked.connect(self.mostrar_widgets)
        self.main_layout.addStretch()
        self.main_layout.addWidget(self.start_button, alignment=Qt.AlignCenter)

        # Inicialmente, esconder todos os widgets
        self.widgets_container.hide()

    def mostrar_widgets(self):
        """Mostra os widgets e esconde o botão Iniciar."""
        self.start_button.hide()
        self.result_label.hide()
        self.widgets_container.show()
        self.result_label.setText("")

    def calculate_sequence(self):
        try:
            n = int(self.n_input.text())
            a, b = map(int, self.ab_input.text().split())

            if n <= 0 or a <= 0 or b <= 0:
                self.show_error_message("Todos os valores devem ser números inteiros positivos.")
                return

            resultado = sequencia_dos_anciaos(n, a, b)
            self.result_label.setText(f"O {n}-ésimo número da sequência é: {resultado}")
            self.result_label.show()

            # Timer para resetar a tela após 5 segundos
            QTimer.singleShot(5000, self.resetar_para_iniciar)

        except ValueError:
            self.show_error_message("Entrada inválida! Insira números inteiros válidos para n, a e b.")

    def resetar_para_iniciar(self):
        """Esconde os widgets, reseta os campos de entrada e mostra o botão Iniciar novamente."""
        self.widgets_container.hide()
        self.result_label.hide()
        self.n_input.clear()
        self.ab_input.clear()
        self.start_button.show()

    def show_error_message(self, message):
        """Exibe uma mensagem de erro personalizada."""
        msg = QMessageBox(self)
        msg.setWindowTitle("🚨 Erro")
        msg.setText(message)
        msg.setIcon(QMessageBox.Warning)
        msg.setStyleSheet("""
            QMessageBox {
                background-color: #000000;
                color: #FFD700;
                font-size: 14px;
                font-family: Helvetica;
            }
            QMessageBox QLabel {
                color: #FFD700;
            }
            QMessageBox QPushButton {
                background-color: transparent;
                color: #FFD700;
                border: 2px solid #FF4500;
                border-radius: 10px;
                padding: 5px 15px;
            }
            QMessageBox QPushButton:hover {
                background-color: #FF4500;
                color: white;
            }
        """)
        msg.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = KnightSequenceApp()
    window.show()
    sys.exit(app.exec_())
