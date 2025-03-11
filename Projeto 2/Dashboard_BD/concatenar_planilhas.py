import os
import pandas as pd

pasta = r"Dashboard_BD\All - Por Ano" #armazena o caminho da pasta onde está salvo os arquivos
arquivos = [os.path.join(pasta,arquivo) for arquivo in os.listdir(pasta)] #lista com todos os arquivos dentro da pasta

tabela_final = pd.DataFrame()
for arquivo in arquivos:
    df = pd.read_excel(arquivo, index_col=0) # lê o arquivo em excel
    tabela_final = pd.concat([tabela_final, df]) #junta informações deste arquivo na tabela

#exportar tabela para uma planilha excel.
tabela_final.to_excel(r"Dashboard_BD\all.xlsx")
print("Importação e concatenização concluida com sucesso!")