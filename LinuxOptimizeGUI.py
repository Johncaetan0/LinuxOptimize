import tkinter as tk
from tkinter import messagebox
import subprocess
from getpass import getpass

def executar_comando(comando, senha_root):
    try:
        # Adicionar 'sudo' ao comando e passar senha para prompt de senha
        processo = subprocess.Popen(['sudo', '-S'] + comando.split(), stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        saida, erro = processo.communicate(input=senha_root + '\n', timeout=10)

        # Verificar a saída e o erro
        if processo.returncode == 0:
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QCheckBox, QLineEdit, QMessageBox
from PyQt5.QtCore import Qt
import subprocess

class OtimizadorSistema(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.label = QLabel('Digite a senha de root:')
        layout.addWidget(self.label)

        self.senha_input = QLineEdit(self)
        self.senha_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.senha_input)

        self.checkbox_bluetooth = QCheckBox('Desabilitar Bluetooth', self)
        layout.addWidget(self.checkbox_bluetooth)

        self.checkbox_avahi = QCheckBox('Desabilitar Avahi', self)
        layout.addWidget(self.checkbox_avahi)

        self.checkbox_animacoes = QCheckBox('Desabilitar Animações do GNOME', self)
        layout.addWidget(self.checkbox_animacoes)

        self.botao_otimizar = QPushButton('Otimizar Sistema', self)
        self.botao_otimizar.clicked.connect(self.otimizar_sistema)
        layout.addWidget(self.botao_otimizar)

        self.setLayout(layout)

        self.show()

    def otimizar_sistema(self):
        senha_root = self.senha_input.text()

        otimizacoes_selecionadas = []
        if self.checkbox_bluetooth.isChecked():
            otimizacoes_selecionadas.append("sudo systemctl disable bluetooth")

        if self.checkbox_avahi.isChecked():
            otimizacoes_selecionadas.append("sudo systemctl disable avahi-daemon")

        if self.checkbox_animacoes.isChecked():
            otimizacoes_selecionadas.append("gsettings set org.gnome.desktop.interface enable-animations false")

        if otimizacoes_selecionadas:
            QMessageBox.information(self, 'Otimizações Selecionadas', 'As otimizações foram selecionadas. Clique em OK para continuar.')

            for otimizacao in otimizacoes_selecionadas:
                resultado = self.executar_comando(otimizacao, senha_root)
                QMessageBox.information(self, 'Resultado', resultado)

            QMessageBox.information(self, 'Concluído', 'Otimizações concluídas.')
        else:
            QMessageBox.information(self, 'Nenhuma Otimização Selecionada', 'Nenhuma otimização foi selecionada.')

    def executar_comando(self, comando, senha_root):
        try:
            processo = subprocess.Popen(['sudo', '-S'] + comando.split(), stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            saida, erro = processo.communicate(input=senha_root + '\n', timeout=10)

            if processo.returncode == 0:
                return saida.strip()
            else:
                return f"Erro: {erro.strip()}"
        except Exception as e:
            return f"Erro: {str(e)}"

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = OtimizadorSistema()
    sys.exit(app.exec_())
