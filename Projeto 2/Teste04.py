import os
from time import sleep
import pygetwindow as gw

# Abrir o aplicativo
os.startfile(r"C:\Users\00082300\Downloads\Projeto 2\atalhos\mm_utr.SAP")
sleep(10)

# Tentar encontrar a janela aberta
windows = gw.getWindowsWithTitle('ENP')

if windows:
    app_window = windows[0]
    app_window.maximize()
else:
    print("Janela do aplicativo não encontrada")