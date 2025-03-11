import psutil
import os

def fechar_outlook():
    # Verifica todos os processos ativos
    for proc in psutil.process_iter(['pid', 'name']):
        # Se o nome do processo for 'OUTLOOK.EXE', fecha-o
        if proc.info['name'].lower() == 'outlook.exe':
            print(f"Fechando Outlook (PID: {proc.info['pid']})...")
            proc.terminate()  # Tenta fechar o processo de forma educada
            try:
                proc.wait(timeout=3)  # Espera por até 3 segundos para o processo fechar
                print("Outlook fechado com sucesso.")
            except psutil.TimeoutExpired:
                print("O Outlook não fechou dentro do tempo esperado. Forçando o fechamento.")
                proc.kill()  # Força o fechamento se não fechar dentro do tempo
            return
    print("Outlook não está aberto.")
'''
if __name__ == "__main__":
    fechar_outlook()'''

fechar_outlook()