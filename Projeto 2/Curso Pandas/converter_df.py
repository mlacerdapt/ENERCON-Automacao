import pandas as pd
data = pd.read_excel(r'O:\02-Blades\17-Warehouse-Operators\Levantamento de Material em Armazém\Material Adicional\EXCEL\Historico.xlsm', index_col=0)
data.to_excel(r"O:\02-Blades\17-Warehouse-Operators\Levantamento de Material em Armazém\Material Adicional\EXCEL\historico_base.xlsx")
