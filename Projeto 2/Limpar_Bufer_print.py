import ctypes
import sys
import subprocess

def is_admin():
    """Verifica se o script está rodando como administrador"""
    return ctypes.windll.shell32.IsUserAnAdmin() != 0

def disable_print_spooler():
    try:
        subprocess.run("sc stop Spooler", shell=True, check=True)
        subprocess.run("sc config Spooler start= disabled", shell=True, check=True)
        print("Print Spooler desativado com sucesso.")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao desativar o Print Spooler: {e}")

if is_admin():
    disable_print_spooler()
else:
    print("Reiniciando script com permissões de administrador...")
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
