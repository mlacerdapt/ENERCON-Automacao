import pandas as pd

venda = {'data': ["15/02/2021","16/02/2021"],'valor': ["500","300"],'produto': ["feijão","arroz"],'qtde': ["50","70"], }

vendas_df = pd.DataFrame(venda)

vendas_df = pd.read_excel("Pandas/All_2024_1.XLSX")

#print(vendas_df.head())
#print(vendas_df.shape)
#print(vendas_df.describe())

#produtos = vendas_df[["Material","Plant"]]
#print(produtos)

# pega uma linha especifica
# print(vendas_df.loc[1])

#pegar linhas que correspondem a um condição

print(vendas_df.loc[vendas_df["Work Center"] == "E103_SP"])


