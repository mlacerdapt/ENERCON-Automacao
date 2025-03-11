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
from flask import Flask, jsonify, render_template
from threading import Timer


def verificar_imagem_na_tela(imagem_tela, max_tentativas=5, intervalo=5):
    tentativas = 0
    
    while tentativas < max_tentativas:
        try:
            # Tenta localizar a imagem na tela
            localizacao = pyautogui.locateCenterOnScreen(imagem_tela, confidence=0.9)
            
            # Se a imagem for encontrada, retorna a localização e sai do loop
            if localizacao:
                print(f"Imagem {imagem_tela} encontrada na tentativa {tentativas + 1}")
                return localizacao
        
        except pyautogui.ImageNotFoundException:
            pass

        # Incrementa as tentativas e espera o intervalo antes de tentar novamente
        tentativas += 1
        print(f"Tentativa {tentativas}, com a imagem {imagem_tela} falhou, aguardando {intervalo} segundos...")
        sleep(intervalo)


    return None
def abrirsistema():
    # Abrir o aplicativo
    os.startfile(r"https://srv-sapmep.enercon.de/manufacturing/com/sap/me/activity/client/ActivityManager.jsp")
    sleep(10)

    # Tentar encontrar a janela aberta
    windows = gw.getWindowsWithTitle('ENP')

    if windows:
        app_window = windows[0]
        app_window.maximize()
    else:
        print("Janela do aplicativo não encontrada")

def abrir_reimprimir():
    #Abrir transação IQ09 Stock
    imagem = 'Impressao_Etiquetas/reimpressao.png'
    resultado = verificar_imagem_na_tela(imagem)
    if resultado:
        pyautogui.click(resultado[0],resultado[1], duration=1, clicks=2)
    else:
        print(f"Imagem {imagem} não encontrada.")
    sleep(4)

def abrir_selecao():
    #Abrir transação IQ09 Stock
    imagem = 'Impressao_Etiquetas/selecao.png'
    resultado = verificar_imagem_na_tela(imagem)
    if resultado:
        pyautogui.click(resultado[0],resultado[1], duration=1, clicks=2)
    else:
        print(f"Imagem {imagem} não encontrada.")
    sleep(4)
def abrir_texto():
    #Abrir transação IQ09 Stock
    imagem = 'Impressao_Etiquetas\identificacao.png'
    resultado = verificar_imagem_na_tela(imagem)
    if resultado:
        pyautogui.click(resultado[0],resultado[1], duration=1, clicks=2)
    else:
        print(f"Imagem {imagem} não encontrada.")
    sleep(4)

def click_ok():
    #Abrir transação IQ09 Stock
    imagem = 'Impressao_Etiquetas\OK.png'
    resultado = verificar_imagem_na_tela(imagem)
    if resultado:
        pyautogui.click(resultado[0],resultado[1], duration=1, clicks=2)
    else:
        print(f"Imagem {imagem} não encontrada.")
    sleep(4)

def click_chamar():
    #Abrir transação IQ09 Stock
    imagem = 'Impressao_Etiquetas\chamar.png'
    resultado = verificar_imagem_na_tela(imagem)
    if resultado:
        pyautogui.click(resultado[0],resultado[1], duration=1, clicks=2)
    else:
        print(f"Imagem {imagem} não encontrada.")
    sleep(4)
def click_selecao():
    #Abrir transação IQ09 Stock
    imagem = 'Impressao_Etiquetas\select.png'
    resultado = verificar_imagem_na_tela(imagem)
    if resultado:
        pyautogui.click(resultado[0],resultado[1], duration=1, clicks=2)
    else:
        print(f"Imagem {imagem} não encontrada.")
    sleep(4)

def click_imprimir():
    #Abrir transação IQ09 Stock
    imagem = 'Impressao_Etiquetas\print.png'
    resultado = verificar_imagem_na_tela(imagem)
    if resultado:
        pyautogui.click(resultado[0],resultado[1], duration=1, clicks=2)
    else:
        print(f"Imagem {imagem} não encontrada.")
    sleep(4)

def click_encerrar():
    #Abrir transação IQ09 Stock
    imagem = 'Impressao_Etiquetas\encerrar.png'
    resultado = verificar_imagem_na_tela(imagem)
    if resultado:
        pyautogui.click(resultado[0],resultado[1], duration=1, clicks=2)
    else:
        print(f"Imagem {imagem} não encontrada.")
    sleep(4)

def imprimir_numeros():
    while True:
        try:
            # Solicita ao usuário o número SAP
            numero_sap = input("Digite o número SAP (ou 'sair' para encerrar): ").strip()
            if numero_sap.lower() == 'sair':
                print("Finalizando o programa.")
                break

            # Valida se o número SAP é válido (somente números, opcionalmente com tamanho fixo)
            if not numero_sap.isdigit():
                print("O número SAP deve conter apenas dígitos. Tente novamente.")
                continue

            # Solicita ao usuário o número de série inicial
            numero_serie_inicial = input("Digite o número de série inicial: ").strip()
            if not numero_serie_inicial.isdigit():
                print("O número de série inicial deve conter apenas dígitos. Tente novamente.")
                continue

            # Solicita ao usuário o número de série final
            numero_serie_final = input("Digite o número de série final: ").strip()
            if not numero_serie_final.isdigit():
                print("O número de série final deve conter apenas dígitos. Tente novamente.")
                continue

            # Converte os números de série para inteiros
            numero_serie_inicial = int(numero_serie_inicial)
            numero_serie_final = int(numero_serie_final)

            # Verifica se o número de série inicial é menor ou igual ao final
            if numero_serie_inicial > numero_serie_final:
                print("O número de série inicial deve ser menor ou igual ao número de série final. Tente novamente.")
                continue

            # Gera e imprime a sequência de números SAP e série
            print("\nSequência gerada:")
            for serie in range(numero_serie_inicial, numero_serie_final + 1):
                abrirsistema()
                abrir_reimprimir()
                abrir_selecao()
                click_ok()
                abrir_texto()
                click_chamar()
                identificacao = f"{numero_sap}-EVC{serie:04d}"
                pyperclip.copy(identificacao)
                sleep(2)
                pyautogui.hotkey('ctrl', 'v')
                click_selecao()
                click_imprimir()
                click_encerrar()
                pyautogui.hotkey('alt','f4')

            print("\nSequência finalizada. Você pode inserir novos dados ou digitar 'sair' para encerrar.\n")

        except Exception as e:
            print(f"Ocorreu um erro: {e}. Tente novamente.")

# Executa a função
imprimir_numeros()
