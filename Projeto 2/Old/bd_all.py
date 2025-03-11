#-*- coding: UTF-8 -*-
import pyautogui
import openpyxl
from time import sleep
import schedule
import pyperclip

blank = 'blank'
pa = 'all_PA'
pp = 'all_PP'
sa1 = 'stock_alerta'
sa2 = 'stock_alerta2'
sa3 = 'stock_alerta3'
mb52 = 'mb52'
me2n = 'me2n'
zmb52 ='zmb52'


pyautogui.hotkey('win','r')
sleep(2)
BD = r'\\srv-pt3\groups\02-Blades\02-Process Engineering\9. Projetos\4. Dashboard\Base de Dados\BD_2024_dashboard.xlsm'
pyperclip.copy(BD)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('enter')
sleep(30)
pyautogui.hotkey('ctrl', 'alt','f5')
pyautogui.hotkey('left')
pyautogui.hotkey('enter')
sleep(300)
pyautogui.hotkey('ctrl', 'q')
sleep(350)
pyautogui.hotkey('alt', 'f4')
print('teste finalizado')