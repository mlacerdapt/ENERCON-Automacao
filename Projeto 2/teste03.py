from datetime import datetime, timedelta
import os
from time import sleep
import pyautogui
import pygetwindow as gw
import openpyxl
import schedule
import pyperclip

# Obter a data de inicio e fim do periodo de pesquisa
data_inicio = datetime.now() - timedelta(days=35)
data_fim = datetime.now() + timedelta(days=35)
# Formatar a data e hora em uma string
datainicio = data_inicio.strftime("%d%m%Y")
datafim = data_fim.strftime("%d%m%Y")
