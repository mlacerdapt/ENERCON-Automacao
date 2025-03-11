import pyautogui
import openpyxl
from time import sleep
import schedule
import pyperclip
import os

os.startfile(r'\\srv-pt3\groups\02-Blades\02-Process Engineering\9. Projetos\4. Dashboard\Base de Dados\BD_2024_dashboard.xlsm')
sleep(30)
pyautogui.hotkey('ctrl', 'alt','f5')
pyautogui.hotkey('left')
pyautogui.hotkey('enter')
print('Atualizando powerquery')
sleep(300)
print('Finalizado o prazo de atualização PowerQuery')
pyautogui.hotkey('ctrl', 'q')
print('Atualizando Macro')
sleep(350)
print('Finalziado a atualização da Macro')
pyautogui.hotkey('alt', 'f4')