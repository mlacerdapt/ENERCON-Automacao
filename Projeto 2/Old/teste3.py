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

def abrirsap():
    # ALL_PP
    #abrir o SAP
    abrirsap = pyautogui.locateCenterOnScreen('abrir_sap.png', confidence=0.9)
    pyautogui.click(abrirsap[0],abrirsap[1], duration=1, clicks=2)
    sleep(6)
def logarsap():
    #login do SAP
    loginsap = pyautogui.locateCenterOnScreen('botao_login_SAP.png', confidence=0.9)
    pyautogui.click(loginsap[0],loginsap[1], duration=1, clicks=2)
    sleep(4)
def abrircoois():
    #Abrir transação COOIS
    abrircoois = pyautogui.locateCenterOnScreen('abrir_coois.png', confidence=0.9)
    pyautogui.click(abrircoois[0],abrircoois[1], duration=1, clicks=2)
    sleep(4)
def variantepp():
    #abrir variante(pp)
    pyautogui.hotkey('shift', 'f5')
    sleep(1)
    digvariavel = pyautogui.locateCenterOnScreen('dig_variavel.png', confidence=0.9)
    pyautogui.click(digvariavel[0],digvariavel[1], duration=1, clicks=2)
    sleep(2)
    pyautogui.write(pp)
    confvariavel = pyautogui.locateCenterOnScreen('conf_variavel.png', confidence=0.9)
    pyautogui.click(confvariavel[0],confvariavel[1], duration=1, clicks=2)
    sleep(1)
def abrirrelat():
    #Abrir relatório
    pyautogui.hotkey('f8')
    sleep(15)
def exportexcel():
    #abrir menu export
    abrirmenu = pyautogui.locateCenterOnScreen('abrir_menu_export.png', confidence=0.9)
    pyautogui.click(abrirmenu[0],abrirmenu[1], duration=2, clicks=1)
    sleep(1)

    #Exportar para excel
    exportexcel = pyautogui.locateCenterOnScreen('export_excel.png', confidence=0.9)
    pyautogui.click(exportexcel[0],exportexcel[1], duration=1)
    sleep(1)

    exportexcelmenu = pyautogui.locateCenterOnScreen('export_excel_menu.png', confidence=0.9)
    pyautogui.click(exportexcelmenu[0],exportexcelmenu[1], duration=1)
    sleep(2)

    confexport = pyautogui.locateCenterOnScreen('conf_export.png', confidence=0.9)
    pyautogui.click(confexport[0],confexport[1], duration=2)
    sleep(10)
def salvarexcelpp():
    #Salvar a planilha
    all_pp_salve = r'\\srv-pt3\groups\02-Blades\02-Process Engineering\9. Projetos\4. Dashboard\Base de Dados\all_pp.XLSX'
    pyautogui.write(all_pp_salve)
    pyautogui.hotkey('enter')
    sleep(4)
    pyautogui.hotkey('y')
    sleep(4)
    pyautogui.hotkey('alt','f4')
    sleep(2)
def sairtransacao():
    #sair transação
    pyautogui.hotkey('esc')
    sleep(3)
def variantepa():
    #abrir variante (PA)
    pyautogui.hotkey('shift', 'f5')
    sleep(1)
    digvariavel = pyautogui.locateCenterOnScreen('dig_variavel.png', confidence=0.9)
    pyautogui.click(digvariavel[0],digvariavel[1], duration=1, clicks=2)
    sleep(2)
    pyautogui.write(pa)
    confvariavel = pyautogui.locateCenterOnScreen('conf_variavel.png', confidence=0.9)
    pyautogui.click(confvariavel[0],confvariavel[1], duration=1, clicks=2)
    sleep(1)
def clicarno():
    #clicar no botão no para muitas linhas(superior a 5mil linhas)
    botaono = pyautogui.locateCenterOnScreen('botao_no.png', confidence=0.9)
    pyautogui.click(botaono[0],botaono[1], duration=1, clicks=1)
    sleep(240)
def salvarexcelpa():
    #Salvar a planilha
    sleep(60)
    all_pa_salve = r'\\srv-pt3\groups\02-Blades\02-Process Engineering\9. Projetos\4. Dashboard\Base de Dados\All - Por Ano\All_2024_1.XLSX'
    pyautogui.write(all_pa_salve)
    sleep(2)
    pyautogui.hotkey('enter')
    sleep(4)
    pyautogui.hotkey('y')
    sleep(100)
    pyautogui.hotkey('alt','f4')
    sleep(5)
def abririq09():
    #Abrir transação IQ09 Stock
    abririq09 = pyautogui.locateCenterOnScreen('abrir_iq09.png', confidence=0.9)
    pyautogui.click(abririq09[0],abririq09[1], duration=1, clicks=2)
    sleep(4)

    #abrir variante(pp)
    pyautogui.hotkey('shift', 'f5')
    sleep(1)
    digvariavel = pyautogui.locateCenterOnScreen('dig_variavel.png', confidence=0.9)
    pyautogui.click(digvariavel[0],digvariavel[1], duration=1, clicks=2)
    sleep(4)
    pyautogui.write(pp)
    confvariavel = pyautogui.locateCenterOnScreen('conf_variavel.png', confidence=0.9)
    pyautogui.click(confvariavel[0],confvariavel[1], duration=1, clicks=2)
    sleep(3)
    pyautogui.hotkey('f8')
    sleep(4)
def exportexceliq09():
    #Exportar excel
    exportiq09 = pyautogui.locateCenterOnScreen('export_iq09.png', confidence=0.9)
    pyautogui.click(exportiq09[0],exportiq09[1], duration=1, clicks=2)
    sleep(2)
    export_conf1 = pyautogui.locateCenterOnScreen('export_conf1.png', confidence=0.9)
    pyautogui.click(export_conf1[0],export_conf1[1], duration=1)
    sleep(3)
    pyautogui.hotkey('up')
    sleep(2)
    export_conf1 = pyautogui.locateCenterOnScreen('export_conf1.png', confidence=0.9)
    pyautogui.click(export_conf1[0],export_conf1[1], duration=1)
    sleep(2)
    export_conf1 = pyautogui.locateCenterOnScreen('export_conf1.png', confidence=0.9)
    pyautogui.click(export_conf1[0],export_conf1[1], duration=1)
    sleep(20)
    #Salvar excel
    salvetable = pyautogui.locateCenterOnScreen('salve_table.png', confidence=0.9)
    pyautogui.click(salvetable[0],salvetable[1], duration=1)
    sleep(2)
    pyautogui.hotkey('f12')
    sleep(3)
    all_pa_salve = r'\\srv-pt3\groups\02-Blades\02-Process Engineering\9. Projetos\4. Dashboard\Base de Dados\Stock_all_pp.xlsx'
    pyautogui.hotkey('backspace')
    sleep(3)
    pyautogui.hotkey('alt','n')
    sleep(3)
    pyautogui.write(all_pa_salve)
    pyautogui.hotkey('enter')
    sleep(1)
    pyautogui.hotkey('left')
    pyautogui.hotkey('enter')
    sleep(5)
    pyautogui.hotkey('alt','f4')
    sleep(1)
def fecharsap():
    #sair transação
    pyautogui.hotkey('alt','f4')
    sleep(1)
    sairyes = pyautogui.locateCenterOnScreen('yes_sair.png', confidence=0.9)
    pyautogui.click(sairyes[0],sairyes[1], duration=1, clicks=1)
    pyautogui.hotkey('enter')
    sleep(1)
    #fechar o SAP
    sair_x = pyautogui.locateCenterOnScreen('sair_x.png', confidence=0.9)
    pyautogui.click(sair_x[0],sair_x[1], duration=1, clicks=2)
def abrirtrans():
    #Abrir transação COOIS
    abrir_trans = pyautogui.locateCenterOnScreen('digitar_trans.png', confidence=0.9)
    pyautogui.click(abrir_trans[0],abrir_trans[1], duration=1, clicks=1)
    sleep(1)
def abrirmb52():
    pyautogui.write(mb52)
    pyautogui.hotkey('enter')
    sleep(2)
    #abrir variante(sa1)
    pyautogui.hotkey('shift', 'f5')
    sleep(1)
    digvariavel = pyautogui.locateCenterOnScreen('dig_variavel.png', confidence=0.9)
    pyautogui.click(digvariavel[0],digvariavel[1], duration=1, clicks=1)
    sleep(4)
    pyautogui.write(sa1)
    confvariavel = pyautogui.locateCenterOnScreen('conf_variavel.png', confidence=0.9)
    pyautogui.click(confvariavel[0],confvariavel[1], duration=1, clicks=2)
    sleep(3)
    pyautogui.hotkey('f8')
    sleep(4)
def abrirme2n():
    pyautogui.write(me2n)
    pyautogui.hotkey('enter')
    sleep(2)
    #abrir variante(sa1)
    pyautogui.hotkey('shift', 'f5')
    sleep(1)
    digvariavel = pyautogui.locateCenterOnScreen('dig_variavel.png', confidence=0.9)
    pyautogui.click(digvariavel[0],digvariavel[1], duration=1, clicks=1)
    sleep(4)
    pyautogui.write(sa2)
    confvariavel = pyautogui.locateCenterOnScreen('conf_variavel.png', confidence=0.9)
    pyautogui.click(confvariavel[0],confvariavel[1], duration=1, clicks=1)
    sleep(3)
    abrirvariante = pyautogui.locateCenterOnScreen('acesso_variante.png', confidence=0.9)
    pyautogui.click(abrirvariante[0],abrirvariante[1], duration=1, clicks=1)
    sleep(3)
    confalt = pyautogui.locateCenterOnScreen('Conf_alteracao.png', confidence=0.9)
    pyautogui.click(confalt[0],confalt[1], duration=1, clicks=1)
    sleep(3)

    pyautogui.hotkey('f8')
    sleep(30)
def abrirzmb52():
    pyautogui.write(zmb52)
    pyautogui.hotkey('enter')
    sleep(2)
    #abrir variante(sa1)
    pyautogui.hotkey('shift', 'f5')
    sleep(1)
    digvariavel = pyautogui.locateCenterOnScreen('dig_variavel.png', confidence=0.9)
    pyautogui.click(digvariavel[0],digvariavel[1], duration=1, clicks=1)
    sleep(4)
    pyautogui.write(sa3)
    confvariavel = pyautogui.locateCenterOnScreen('conf_variavel.png', confidence=0.9)
    pyautogui.click(confvariavel[0],confvariavel[1], duration=1, clicks=2)
    sleep(3)
    pyautogui.hotkey('f8')
    sleep(60)
def trans_blank():
    #abrir transação
    mb51_serial = pyautogui.locateCenterOnScreen('mb51_serial.png', confidence=0.9)
    pyautogui.click(mb51_serial[0],mb51_serial[1], duration=1, clicks=2)
    sleep(2)

    #abrir variante(blank)
    pyautogui.hotkey('shift', 'f5')
    sleep(2)
    janelaexportar = pyautogui.locateCenterOnScreen('janelaexportar.png', confidence=0.9)
    pyautogui.click(janelaexportar[0],janelaexportar[1], duration=1, clicks=2)
    sleep(2)
    pyautogui.write(blank)
    confvariavel = pyautogui.locateCenterOnScreen('conf_variavel.png', confidence=0.9)
    pyautogui.click(confvariavel[0],confvariavel[1], duration=1, clicks=2)
    sleep(3)
    pyautogui.hotkey('f8')
    sleep(240)
def export_menu():
    menu_export= pyautogui.locateCenterOnScreen('menu-list.png', confidence=0.9)
    pyautogui.click(menu_export[0],menu_export[1], duration=1)
    sleep(1)
    menu_export2= pyautogui.locateCenterOnScreen('menu-export.png', confidence=0.9)
    pyautogui.click(menu_export2[0],menu_export2[1], duration=1)
    sleep(1)
    menusheet= pyautogui.locateCenterOnScreen('menu_sheet.png', confidence=0.9)
    pyautogui.click(menusheet[0],menusheet[1], duration=1)
    sleep(1)
    confexport = pyautogui.locateCenterOnScreen('conf_export.png', confidence=0.9)
    pyautogui.click(confexport[0],confexport[1], duration=2)
    sleep(30)
def export_blank():
    #Salvar a planilha
    all_blank = r'\\srv-pt3\groups\02-Blades\02-Process Engineering\9. Projetos\4. Dashboard\Base de Dados\Serialnumber_blank.xlsx'
    pyautogui.write(all_blank)
    pyautogui.hotkey('enter')
    sleep(10)
    pyautogui.hotkey('y')
    sleep(20)
    pyautogui.hotkey('alt','f4')
    sleep(2)
def export_mb52SA():
    #Salvar a planilha
    mb52SA = r'\\srv-pt3\groups\02-Blades\05-Warehouse\08. Análise semanal de níveis de stock\Base de Dados\SAP\MB52_All.XLSX'
    pyperclip.copy(mb52SA)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.hotkey('enter')
    sleep(4)
    pyautogui.hotkey('y')
    sleep(60)
    pyautogui.hotkey('alt','f4')
    sleep(2)
def export_me2nSA():
    abrirdatas = pyautogui.locateCenterOnScreen('abrirdatas.png', confidence=0.9)
    pyautogui.click(abrirdatas[0],abrirdatas[1], duration=1, clicks=2)
    sleep(6)
    delivdate = pyautogui.locateCenterOnScreen('devildate.png', confidence=0.9)
    pyautogui.click(delivdate[0],delivdate[1], duration=1, clicks=1, button='right')
    sleep(1)
    acendente = pyautogui.locateCenterOnScreen('acendente.png', confidence=0.9)
    pyautogui.click(acendente[0],acendente[1], duration=1, clicks=1)
    sleep(1)
    exportsheet = pyautogui.locateCenterOnScreen('export_iq09.png', confidence=0.9)
    pyautogui.click(exportsheet[0],exportsheet[1], duration=1, clicks=1)
    sleep(2)
    confexport = pyautogui.locateCenterOnScreen('conf_export.png', confidence=0.9)
    pyautogui.click(confexport[0],confexport[1], duration=2)
    sleep(6)
    #Salvar a planilha
    me2nSA = r'\\srv-pt3\groups\02-Blades\05-Warehouse\08. Análise semanal de níveis de stock\Base de Dados\SAP\ME2N_All.XLSX'
    pyperclip.copy(me2nSA)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.hotkey('enter')
    sleep(4)
    pyautogui.hotkey('y')
    sleep(60)
    pyautogui.hotkey('alt','f4')
    sleep(2)
def export_zmb52SA():
    pyautogui.hotkey('ctrl','shift','f7')
    sleep(2)
    confexport = pyautogui.locateCenterOnScreen('conf_export.png', confidence=0.9)
    pyautogui.click(confexport[0],confexport[1], duration=2)
    sleep(6)

    #Salvar a planilha
    zmb52SA = r'\\srv-pt3\groups\02-Blades\05-Warehouse\08. Análise semanal de níveis de stock\Base de Dados\SAP\ZMB52_All.XLSX'
    pyperclip.copy(zmb52SA)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.hotkey('enter')
    sleep(4)
    pyautogui.hotkey('y')
    sleep(60)
    pyautogui.hotkey('alt','f4')
    sleep(2)
def controle_corte():
    pyautogui.hotkey('win','r')
    sleep(2)
    corte = r'\\srv-pt3\groups\02-Blades\02-Process Engineering\9. Projetos\4. Dashboard\Base de Dados\CONTROLE CORTE.xlsm'
    pyperclip.copy(corte)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.hotkey('enter')
    sleep(40)
    pyautogui.hotkey('alt', 'f4')
    sleep(2)
    pyautogui.hotkey('g')
    print('Controle de Corte atualizado!')

abrirsap()
logarsap()

abrirtrans()
abrirme2n()
export_me2nSA()
sairtransacao()
sairtransacao()
print('Primeiro arquivo gerado! Transação: ME2N')

abrirtrans()
abrirmb52()
export_menu()
export_mb52SA()
sairtransacao()
sairtransacao()
print('Segundo arquivo gerado! Transação: MB52')

abrirtrans()
abrirzmb52()
export_zmb52SA()
sairtransacao()
sairtransacao()
print('Terceiro arquivo gerado! Transação: ZMB52')

fecharsap()
print('**************BD Stock Alerta realizado com sucesso!*************')