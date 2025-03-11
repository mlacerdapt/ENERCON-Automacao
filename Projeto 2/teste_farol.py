import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd

# Dados
data = {
    "Order": ["800003472003", "800003472004", "800003472005", "800003472006", "800003474121", "800003474122", "800003474123", "800003474124", "800003474125"],
    "Material": ["623095"] * 9,
    "Material Description": ["rbl shell PF spar boom E103EP2RB01"] * 9,
    "Serialnumber": ["EVC0448", "EVC0449", "EVC0450", "EVC0451", "EVC0452", "EVC0453", "EVC0454", "EVC0455", "EVC0456"],
    "Status": [5, 3, 3, 3, 0, 0, 0, 0, 0],
    "BD_STATUS.Area": ["Q - Insp. Final", "Q - Ultrassom", "Q - Ultrassom", "Q - Ultrassom", "Não Iniciado", "Não Iniciado", "Não Iniciado", "Não Iniciado", "Não Iniciado"],
    "Stock_Status": ["Bloqueio QA", "", "", "", "Não Iniciado", "Não Iniciado", "Não Iniciado", "Não Iniciado", "Não Iniciado"],
    "Proxima Etapa": ["Q - Insp. Final", "P - Prep. Fabr. Sul", "P - Prep. Fabr. Sul", "P - Prep. Fabr. Sul", "P - Construção", "P - Construção", "P - Construção", "P - Construção", "P - Construção"]
}

df = pd.DataFrame(data)

# Inicializar o app Dash
app = dash.Dash(__name__)

# Layout do dashboard
app.layout = html.Div([
    dcc.Dropdown(
        id='status-dropdown',
        options=[{'label': status, 'value': status} for status in df['Status'].unique()],
        value=df['Status'].unique()[0],
        placeholder="Selecione um status"
    ),
    html.Div(id='table-container')
])

# Callback para atualizar a tabela
@app.callback(
    Output('table-container', 'children'),
    [Input('status-dropdown', 'value')]
)
def update_table(selected_status):
    filtered_df = df[df['Status'] == selected_status]
    return html.Table([
        html.Thead(html.Tr([html.Th(col) for col in filtered_df.columns])),
        html.Tbody([
            html.Tr([html.Td(filtered_df.iloc[i][col]) for col in filtered_df.columns]) for i in range(len(filtered_df))
        ])
    ])

# Rodar o app
if __name__ == '__main__':
    app.run_server(debug=True)