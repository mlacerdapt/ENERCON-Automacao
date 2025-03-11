import os
from time import sleep, time
import pyautogui
import schedule
from datetime import datetime
import tkinter as tk

def criar_janela():
    global root, label
    root = tk.Tk()
    root.title("Atualização Power BI")
    root.geometry("400x200")
    label = tk.Label(root, text="Iniciando...", font=("Arial", 12))
    label.pack(pady=20)
    root.update()

def atualizar_mensagem(mensagem):
    label.config(text=mensagem)
    root.update()

def esperar_e_clicar(imagem, descricao="Elemento", timeout=80, clicks=1, duracao=1, intervalo=1):
    tempo_inicial = time()
    while time() - tempo_inicial < timeout:
        try:
            localizacao = pyautogui.locateCenterOnScreen(imagem, confidence=0.95)
            if localizacao:
                atualizar_mensagem(f"{descricao} encontrado! Clicando...")
                pyautogui.click(localizacao, duration=duracao, clicks=clicks)
                return True
        except pyautogui.ImageNotFoundException:
            sleep(intervalo)
    atualizar_mensagem(f"Erro: {descricao} não encontrado!")
    return False

def abrir_powerbi():
    os.startfile(r"\\srv-pt3\groups\02-Blades\02-Process Engineering\9. Projetos\32. Criar PR\Requisição de Compras 2.pbix")
    sleep(10)

def atualizar():
    criar_janela()
    data_hora_atual = datetime.now()
    nomearquivo = data_hora_atual.strftime("%d-%m-%y %H%M%S")
    atualizar_mensagem(f"Iniciando atualização: {nomearquivo}")
    abrir_powerbi()
    sleep(5)
    esperar_e_clicar('PBI_atualizar.png', "Atualizar dados", timeout=120, clicks=1) 
    sleep(20)
    esperar_e_clicar('PBI_publicar.png', "Publicar dados", timeout=120, clicks=1) 
    esperar_e_clicar('PBI_salve.png', "Salvar", timeout=120, clicks=1) 
    esperar_e_clicar('PBI_select.png', "Selecionar local", timeout=120, clicks=1) 
    esperar_e_clicar('PBI_replace.png', "Substituir", timeout=120, clicks=1) 
    esperar_e_clicar('PBI_goit.png', "Ir para", timeout=120, clicks=1) 
    pyautogui.hotkey('alt', 'f4')
    tempo = datetime.now() - data_hora_atual
    atualizar_mensagem(f"Finalizando em: {tempo}")
    root.after(5000, root.destroy)
    root.mainloop()
    print("executado")

schedule.every(30).minutes.do(atualizar)

while True:
    schedule.run_pending()
    sleep(30)
