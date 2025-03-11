import pyautogui
import openpyxl
from time import sleep
blank = 'blank'
pa = 'all_PA'
pp = 'all_PP'

# ALL_PP
#abrir o SAP
abrirsap = pyautogui.locateCenterOnScreen('abrir_sap.png', confidence=0.9)
pyautogui.click(abrirsap[0],abrirsap[1], duration=2, clicks=2)
sleep(5)

#login do SAP
loginsap = pyautogui.locateCenterOnScreen('botao_login_SAP.png', confidence=0.9)
pyautogui.click(loginsap[0],loginsap[1], duration=2, clicks=2)
sleep(4)

#Abrir transação COOIS
abrircoois = pyautogui.locateCenterOnScreen('abrir_coois.png', confidence=0.9)
pyautogui.click(abrircoois[0],abrircoois[1], duration=2, clicks=2)
sleep(4)

#abrir variante
pyautogui.hotkey('shift', 'f5')
digvariavel = pyautogui.locateCenterOnScreen('dig_variavel.png', confidence=0.9)
pyautogui.click(digvariavel[0],digvariavel[1], duration=2, clicks=2)
sleep(2)
pyautogui.write(pp)
confvariavel = pyautogui.locateCenterOnScreen('conf_variavel.png', confidence=0.9)
pyautogui.click(confvariavel[0],confvariavel[1], duration=2, clicks=2)
sleep(1)
pyautogui.hotkey('f8')
sleep(10)

#carregar relatorio
pyautogui.click(2270,511, duration=2)
pyautogui.click(1953,122, duration=2)
pyautogui.click(2295,390, duration=2)
sleep(20)
#Exportar relatorio
pyautogui.click(1974,126, duration=1)
pyautogui.click(2338,128, duration=1)
pyautogui.click(2363,156, duration=1)
#Salvar realtorio
all_pp_salve = r'\\srv-pt3\groups\02-Blades\02-Process Engineering\9. Projetos\4. Dashboard\Base de Dados\all_pp.XLSX'
pyautogui.click(2384,286, duration=1)
sleep(3)
pyautogui.write(all_pp_salve)

pyautogui.click(2951,757, duration=1)
sleep(2)

#Retornar

sleep(5)
pyautogui.hotkey(Ctrl,Shift,q)

pyautogui.click(2930,527, duration=1)
sleep(2)
pyautogui.click(2190,49, duration=1)
sleep(2)
pyautogui.click(2190,49, duration=1)



#Sotck PP

#Abrir transação
pyautogui.click(2106,198, duration=5, clicks=2)

#abrir variante
pyautogui.click(1972,124, duration=2)
pyautogui.click(2245,390, duration=2)

pyautogui.write(pp)

#carregar relatorio
pyautogui.click(2270,511, duration=2)
pyautogui.click(1953,122, duration=2)
sleep(10)
#Exportar relatorio
pyautogui.click(2167,120, duration=2)
pyautogui.click(2165,470, duration=2)
pyautogui.click(2165,470, duration=2)
pyautogui.click(2207,340, duration=2)
#Salvar realtorio
all_pp_salve = r'\\srv-pt3\groups\02-Blades\02-Process Engineering\9. Projetos\4. Dashboard\Base de Dados\Stock_all_pp.xlsx'
pyautogui.click(2384,286, duration=1)
sleep(3)
pyautogui.write(all_pp_salve)

pyautogui.click(2951,757, duration=1)
sleep(2)

#Retornar
pyautogui.click(2930,527, duration=1)
sleep(2)
pyautogui.click(2190,49, duration=1)
sleep(2)
pyautogui.click(2190,49, duration=1)