import subprocess
from getpass import getpass

def executar_comando(comando, senha_root):
    try:
        processo = subprocess.Popen(['sudo', '-S'] + comando.split(), stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        saida, erro = processo.communicate(input=senha_root + '\n', timeout=10)

        if processo.returncode == 0:
            return True, saida.strip()
        else:
            return False, f"Erro: {erro.strip()}"
    except Exception as e:
        return False, f"Erro: {str(e)}"

def exibir_letreiro():
    print("\n╭━━━━━━━━━━━━━━━━━━━━━━━━╮")
    print("│  Linux Optimize GUI      │")
    print("│  por johncaetan0         │")
    print("╰━━━━━━━━━━━━━━━━━━━━━━━━╯\n")

def ajuda():
    print("\nAjuda:")
    print("1. Desabilitar Bluetooth: Desativa o serviço Bluetooth.")
    print("2. Desabilitar Avahi: Desativa o serviço Avahi (descoberta de serviços na rede).")
    print("3. Desabilitar Animações GNOME: Desativa animações visuais no ambiente GNOME.")
    print("4. Limpar Arquivos Temporários: Remove arquivos temporários do sistema.")
    print("5. Reabilitar Configurações")
    print("6. Sair\n")

def otimizar_bluetooth(senha_root, desabilitar=True):
    acao = "disable" if desabilitar else "enable"
    sucesso, mensagem = executar_comando(f"sudo systemctl {acao} bluetooth", senha_root)
    if sucesso:
        status = "desabilitado" if desabilitar else "reativado"
        print(f"\nBluetooth {status} com sucesso.")
    else:
        print(f"\nErro ao {acao} Bluetooth: {mensagem}")

def otimizar_avahi(senha_root, desabilitar=True):
    acao = "disable" if desabilitar else "enable"
    sucesso, mensagem = executar_comando(f"sudo systemctl {acao} avahi-daemon", senha_root)
    if sucesso:
        status = "desabilitado" if desabilitar else "reativado"
        print(f"\nAvahi {status} com sucesso.")
    else:
        print(f"\nErro ao {acao} Avahi: {mensagem}")

def otimizar_animacoes_gnome(senha_root, desabilitar=True):
    acao = "false" if desabilitar else "true"
    sucesso, mensagem = executar_comando(f"gsettings set org.gnome.desktop.interface enable-animations {acao}", senha_root)
    if sucesso:
        status = "desabilitadas" if desabilitar else "reativadas"
        print(f"\nAnimações do GNOME {status} com sucesso.")
    else:
        print(f"\nErro ao {acao} Animações do GNOME: {mensagem}")

def limpar_arquivos_temporarios(senha_root):
    sucesso, mensagem = executar_comando("sudo rm -rf /tmp/*", senha_root)
    if sucesso:
        print("\nArquivos temporários removidos com sucesso.")
    else:
        print(f"\nErro ao remover arquivos temporários: {mensagem}")

def reabilitar_configuracoes(senha_root):
    while True:
        exibir_letreiro()
        print("Opções de Reabilitação:")
        print("1. Reabilitar Bluetooth")
        print("2. Reabilitar Avahi")
        print("3. Reabilitar Animações GNOME")
        print("4. Voltar ao Menu Principal")

        escolha = input("Escolha uma opção (1-4): ")

        if escolha == '1':
            otimizar_bluetooth(senha_root, desabilitar=False)
        elif escolha == '2':
            otimizar_avahi(senha_root, desabilitar=False)
        elif escolha == '3':
            otimizar_animacoes_gnome(senha_root, desabilitar=False)
        elif escolha == '4':
            break
        else:
            print("\nOpção inválida. Tente novamente.")

def otimizar_sistema():
    exibir_letreiro()
    senha_root = getpass(prompt="Digite a senha de root: ")

    while True:
        print("\nMenu:")
        print("1. Desabilitar Bluetooth")
        print("2. Desabilitar Avahi")
        print("3. Desabilitar Animações GNOME")
        print("4. Limpar Arquivos Temporários")
        print("5. Ajuda")
        print("6. Reabilitar Configurações")
        print("7. Sair\n")

        escolha = input("Escolha uma opção (1-7): ")

        if escolha == '1':
            otimizar_bluetooth(senha_root)
        elif escolha == '2':
            otimizar_avahi(senha_root)
        elif escolha == '3':
            otimizar_animacoes_gnome(senha_root)
        elif escolha == '4':
            limpar_arquivos_temporarios(senha_root)
        elif escolha == '5':
            ajuda()
        elif escolha == '6':
            reabilitar_configuracoes(senha_root)
        elif escolha == '7':
            print("\nSaindo do programa. Obrigado!")
            break
        else:
            print("\nOpção inválida. Tente novamente.")

if __name__ == "__main__":
    otimizar_sistema()

