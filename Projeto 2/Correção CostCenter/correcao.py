import pandas as pd

# Carrega o arquivo Excel
file_path = 'Correção CostCenter/Livro2.xlsx'  # Substitua pelo caminho correto do seu arquivo
df = pd.read_excel(file_path)

# Converte os valores da coluna "Cost Center" para string
df['Hibe'] = df['Hibe'].astype(str)

# Agrupa por "Material" e junta os valores da coluna "Cost Center"
df_grouped = df.groupby(['Material'])['Hibe'].apply(lambda x: ', '.join(x)).reset_index()

# Salva o resultado em um novo arquivo Excel
df_grouped.to_excel('resultado_agrupado2.xlsx', index=False)

print("As linhas da coluna 'Cost Center' foram unidas com sucesso para cada 'Material'.")

