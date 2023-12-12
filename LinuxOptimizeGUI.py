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
            return saida.strip()
        else:
            return f"Erro: {erro.strip()}"
    except Exception as e:
        return f"Erro: {str(e)}"

def otimizar_sistema():
    # Solicitar senha de root
    senha_root = getpass(prompt="Digite a senha de root: ")

    # Selecionar otimizações
    otimizacoes_selecionadas = []
    if check_desabilitar_bluetooth.get():
        otimizacoes_selecionadas.append("sudo systemctl disable bluetooth")

    if check_desabilitar_avahi.get():
        otimizacoes_selecionadas.append("sudo systemctl disable avahi-daemon")

    if check_desabilitar_animacoes.get():
        otimizacoes_selecionadas.append("gsettings set org.gnome.desktop.interface enable-animations false")

    if otimizacoes_selecionadas:
        messagebox.showinfo("Otimizações Selecionadas", "As otimizações foram selecionadas. Clique em OK para continuar.")
        
        # Executar otimizações
        for otimizacao in otimizacoes_selecionadas:
            resultado = executar_comando(otimizacao, senha_root)
            messagebox.showinfo("Resultado", resultado)

        messagebox.showinfo("Concluído", "Otimizações concluídas.")
    else:
        messagebox.showinfo("Nenhuma Otimização Selecionada", "Nenhuma otimização foi selecionada.")

# Criar a janela
root = tk.Tk()
root.title("Otimizador de Sistema Linux")

# Widgets
check_desabilitar_bluetooth = tk.Checkbutton(root, text="Desabilitar Bluetooth")
check_desabilitar_bluetooth.pack(anchor="w")

check_desabilitar_avahi = tk.Checkbutton(root, text="Desabilitar Avahi")
check_desabilitar_avahi.pack(anchor="w")

check_desabilitar_animacoes = tk.Checkbutton(root, text="Desabilitar Animações do GNOME")
check_desabilitar_animacoes.pack(anchor="w")

botao_otimizar = tk.Button(root, text="Otimizar Sistema", command=otimizar_sistema)
botao_otimizar.pack(pady=20)

# Iniciar o loop principal da interface gráfica
root.mainloop()
