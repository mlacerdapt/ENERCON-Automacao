import pandas as pd
import requests
import tabula

def pdf_para_dataframe(arquivo):
    tabelas = tabula.read_pdf(arquivo, pages ="all")
    dataframe_combinado = pd.DataFrame()
    for tabela in tabelas:
        df = tabela.copy()
        dataframe_combinado = pd.concat([dataframe_combinado, df], ignore_index=True)
    return dataframe_combinado

arquivo = "Leitura desenho/E115 EP3-RB-03/DF-1153-03 Longarina LP - PS spar boom Rev0.1 (1).pdf"
dataframe_combinado2 = pdf_para_dataframe(arquivo)
dataframe_combinado2.to_csv("Leitura desenho/DF-1153-03 Longarina LP - PS spar boom Rev0.1 (1).csv", index=False)