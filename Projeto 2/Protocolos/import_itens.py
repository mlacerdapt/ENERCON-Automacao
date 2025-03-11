import pyautogui
import time
import pandas as pd
 
# Read the DataFrame from the Excel file
df = pd.read_excel(r'C:\Users\00082300\Downloads\ModeloScriptQuantitativa (LPS E-175).xlsx')
 
print(f"{df}")
 
 
time.sleep(5)
 
# Iterate over the DataFrame and fill out the autofill form
for row in df.itertuples():
    # Type "GORO"
    pyautogui.write("GORO")
    time.sleep(5)
 
    # Press TAB
    pyautogui.press("tab")
    # Write the CODE value
    pyautogui.write(row.CODE)
    time.sleep(2)
 
    # Press enter
    pyautogui.press("enter")
    time.sleep(2)
    # Press TAB
    pyautogui.press('tab')
    time.sleep(2)
 
    # Press space
    pyautogui.press('space')
    time.sleep(2)
 
    # Press 2x TAB
    pyautogui.press('tab')
    time.sleep(2)
    pyautogui.press('tab')
    time.sleep(2)
 
    # Press Right
    pyautogui.press('right')
    time.sleep(2)
 
    # Press TAB
    pyautogui.press('tab')
    time.sleep(2)
 
    # Press 5x Right
    pyautogui.press('right')
    pyautogui.press('right')
    pyautogui.press('right')
    pyautogui.press('right')
    pyautogui.press('right')
    time.sleep(2)
 
    # Press TAB
    pyautogui.press('tab')
    time.sleep(5)
    # Copy and paste the Descricao_PT value
    descricao_pt = row.Descricao_PT
    pyautogui.write(row.Descricao_PT)
    pyautogui.press('tab')
    time.sleep(2)
    pyautogui.press('tab')
 
    # Copy and paste the Descricao
    CampoPesquisa = row.CampoPesquisa
    pyautogui.write(row.CampoPesquisa)
    pyautogui.press('enter')
 
    #Codigo de Controle - Valor inferior
    time.sleep(5)
    pyautogui.press('tab')
    time.sleep(2)
    pyautogui.press('space')
    time.sleep(2)
 
    # Valor Superior
    pyautogui.press('tab')
    time.sleep(2)
    pyautogui.press('space')
    time.sleep(2)
 
    pyautogui.press('tab')
    pyautogui.press('tab')
    time.sleep(3)
    pyautogui.press('space')
    time.sleep(3)
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    time.sleep(2)
    pyautogui.press('down')
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(2)
 
    pyautogui.write("0")
    time.sleep(2)
 
    pyautogui.press('tab')
    #pyautogui.write('mm')
    #pyautogui.press('alt+234')
    pyautogui.press('tab')
    pyautogui.press('tab')
    time.sleep(2)
 
    #Copy and paste the MinTol Value
    #mintol = str(row.MinTol)
    #pyautogui.write(row.MinTol)
    #Copy and paste the MinTol Value
    mintol_str = str(row.MinTol)
    print(mintol_str)
    mintol_str_formatted = mintol_str.replace('.', ',')
    print(mintol_str_formatted)
    pyautogui.write(mintol_str_formatted)
 
        
    #pyautogui.write("0,5")
    #pyautogui.press('tab')
    #time.sleep(2)
    #maxtol = str(row.MaxTol)
    #pyautogui.write(row.MaxTol)
 
    pyautogui.press('tab')
    time.sleep(2)
    maxtol_str = str(row.MaxTol)
    maxtol_str_formatted = maxtol_str.replace('.', ',')
    print(maxtol_str_formatted)
    pyautogui.write(maxtol_str_formatted)
    #pyautogui.write("10")
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(2)
 
    #Escrever FullPT
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(10)
    pyautogui.hotkey('ctrl', 'down')
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.press('enter')
    FullPT = row.FullPT
    pyautogui.write(row.FullPT)
    time.sleep(5)
    #Click on the point
    pyautogui.click(288, 51)
    time.sleep(5)

    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(2)
 
    pyautogui.write("EN")
    pyautogui.press('tab')
    #Copy and paste the Descricao_EN value
    descricao_en = row.Descricao_EN
    pyautogui.write(descricao_en)
    time.sleep(2)
 
    pyautogui.press('F9')
    time.sleep(10)
    pyautogui.hotkey('ctrl' , 'down')
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.press('enter')        
 
    FullEN = row.FullEN
    pyautogui.write(FullEN)
    time.sleep(5)
 
    #Click on the point (288, 51)
    pyautogui.click(288, 51)
    time.sleep(8)
    pyautogui.press('enter')
    time.sleep(5)
    #Save the form
    pyautogui.hotkey('ctrl', 's')
    time.sleep(5)