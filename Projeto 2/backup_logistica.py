#-*- coding: UTF-8 -*-
import os
from time import sleep
import pyautogui
import pygetwindow as gw
import openpyxl
import schedule
import pyperclip
from datetime import datetime, timedelta
import shutil
import pandas as pd
import psutil
from openpyxl import load_workbook
from openpyxl.worksheet.table import Table, TableStyleInfo
from threading import Timer

def copiar_arquivos(pasta_origem, pasta_destino):
    try:
        if not os.path.exists(pasta_destino):
            os.makedirs(pasta_destino)

        arquivos = os.listdir(pasta_origem)
        for arquivo in arquivos:
            caminho_origem = os.path.join(pasta_origem, arquivo)
            caminho_destino = os.path.join(pasta_destino, arquivo)

            if os.path.isfile(caminho_origem):
                shutil.copy2(caminho_origem, caminho_destino)
                print(f"Arquivo {arquivo} copiado e substituído com sucesso!")
        
        print("Cópia concluída!")
    
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

def backup_log():
    pasta_origem = r'\\srv-pt3\groups\02-Blades\05-Warehouse\ARMAZÉM\Fábrica Sul\3. Folhas para Carrinhos - Matéria Prima\4. Material por Peça E103'
    pasta_destino = r'C:\Users\00082300\ENERCON\PT ROTO BCM Share - Priority\Logistica - Armazem\IT-Breakdown MPP'
    copiar_arquivos(pasta_origem, pasta_destino)
    print("Backup realizado com sucesso - 4. Material por Peça E103 - Fábrica Sul")
    pasta_origem = r'\\srv-pt3\groups\02-Blades\05-Warehouse\ARMAZÉM\Fábrica Sul\3. Folhas para Carrinhos - Matéria Prima\5. Material por peça E175'
    pasta_destino = r'C:\Users\00082300\ENERCON\PT ROTO BCM Share - Priority\Logistica - Armazem\IT-Breakdown MPP'
    copiar_arquivos(pasta_origem, pasta_destino)
    print("Backup realizado com sucesso - 5. Material por peça E175 - Fábrica Sul")
    pasta_origem = r'\\srv-pt3\groups\02-Blades\05-Warehouse\ARMAZÉM\Fábrica Norte\2. MPP\MPP 175'
    pasta_destino = r'C:\Users\00082300\ENERCON\PT ROTO BCM Share - Priority\Logistica - Armazem\IT-Breakdown MPP'
    copiar_arquivos(pasta_origem, pasta_destino)
    print("Backup realizado com sucesso - MPP 175 - Fábrica Norte")
    pasta_origem = r'\\srv-pt3\groups\02-Blades\05-Warehouse\ARMAZÉM\Fábrica Norte\2. MPP\MPP103'
    pasta_destino = r'C:\Users\00082300\ENERCON\PT ROTO BCM Share - Priority\Logistica - Armazem\IT-Breakdown MPP'
    copiar_arquivos(pasta_origem, pasta_destino)
    print("Backup realizado com sucesso - MPP103 - Fábrica Norte")



schedule.every().monday.at("05:40").do(backup_log)


while True:
    schedule.run_pending()
    sleep(30)