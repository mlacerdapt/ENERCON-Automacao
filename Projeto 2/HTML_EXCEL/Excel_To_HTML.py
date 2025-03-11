import pandas as pd

# Caminho do arquivo Excel e imagem
excel_file_path = r"C:\Users\00082300\Downloads\Projeto 2\HTML_EXCEL\Farol_PP.xlsm"  # Substitua pelo caminho do seu arquivo Excel
excel_file_path2 = r"C:\Users\00082300\Downloads\Projeto 2\HTML_EXCEL\BA.xlsm"
output_html_path = r"O:\99-Public\Status de Produção - Primary Parts.html"  # Nome do arquivo HTML de saída


# Lendo os dados do Excel
df = pd.read_excel(excel_file_path, engine="openpyxl")
df2 = pd.read_excel(excel_file_path2, engine="openpyxl")

# Convertendo a tabela do DataFrame em HTML
tabela_html = df.to_html(index=False, classes="tabela-container", border=0)
tabela_html2 = df2.to_html(index=False, classes="tabela-container", border=0)
# Criando o HTML com o layout fornecido
html_content = f"""
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Status de Produção</title>
    <style>
        body {{
            margin: 0;
            padding: 0;
            background-color: #F0F0F0; /* Cor de fundo cinza claro */
            display: flex;
            justify-content: center;
            align-items: center;
            height: 90%;
            font-family: Arial, sans-serif;
        }}

        header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            background-color: #5baaa0; /* Cor de fundo verde */
            color: white;
            padding: 10px 20px;
            font-size: 16px;
            border-radius: 10px 10px 10px 10px;
            height: 90%;

        }}


        .content {{
            width: 90%; /* Largura do conteúdo centralizado */
            height: 90%; /* Altura do conteúdo centralizado */
            background-color: white; /* Fundo branco */
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1); /* Sombra ao redor do conteúdo */
            border-radius: 10px; /* Borda levemente arredondada */
            position: relative;
        }}
        .logo {{
            display: flex;
            align-items: center;
            font-weight: bold;
        }}

        .logo img {{
            height: 40px;
            margin-right: 10px;
        }}

        .titulo {{
            flex-grow: 1;
            text-align: center;
            font-size: 20px;
            font-weight: bold;
        }}

        .data {{
            text-align: right;
            font-size: 18px;
        }}
        .container::after {{
            content: '';
            position: absolute;
            bottom: 0;
            left: 0;
            width: 90%;
            height: 20px;
            background-color: #87C0B1; /* Cor da borda inferior */
            border-radius: 0 0 10px 10px; /* Arredondar cantos inferiores */
        }}
        .content {{
            padding: 20px;
        }}
        .tabela-container {{
            width: 100%;
            max-width: 800px;
            margin: 0 auto;
            border-collapse: collapse;
            border-spacing: 0;
            border: 1px solid #ddd;
            background-color: #fff;
            overflow: hidden;
        }}

        .tabela-container caption {{
            background-color: #5baaa0; /* Verde */
            color: white;
            padding: 10px;
            font-size: 18px;
            font-weight: bold;
            text-align: center;
        }}

        .tabela-container th, .tabela-container td {{
            padding: 10px;
            text-align: left;
            border: 1px solid #ddd;
        }}

        .tabela-container th {{
            background-color: #5baaa0; /* Verde */
            color: white;
            text-transform: uppercase;
        }}

        .tabela-container tbody tr:nth-child(even) {{
            background-color: #f9f9f9;
        }}

        .tabela-container tbody tr:nth-child(odd) {{
            background-color: #ffffff;
        }}

        .containertable {{
            display: grid;
            grid-template-columns: repeat(3, 1fr); /* Divide em 3 colunas iguais */
            gap: 20px;
            max-width: 100%;
        }}

        .button-container {{
            display: grid;
            grid-template-columns: repeat(3, 1fr); /* Divide em 3 colunas iguais */
            gap: 20px;
            width: 100%; 

        }}

        .button {{
            background-color: #5baaa0; /* Cor verde */
            color: white;
            border: none;
            padding: 20px;
            text-align: center;
            text-transform: uppercase;
            font-size: 1.2rem;
            font-weight: bold;
            border-radius: 5px;
            cursor: pointer;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2);
            transition: transform 0.2s ease, box-shadow 0.2s ease;
            display: flex;
            justify-content: center;
            align-items: center;
        }}

        .button:hover {{
            transform: translateY(-2px);
            box-shadow: 0px 6px 10px rgba(0, 0, 0, 0.3);
        }}

        .button:active {{
            transform: translateY(0);
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2);
        }}

        @media (max-width: 768px) {{
            .button-container {{
                grid-template-columns: 1fr; /* Botões empilhados em telas pequenas */
            }}
        }}

        .table-container {{
        
        flex-wrap: wrap; /* Permite quebrar linha em telas menores */
        gap: 20px; /* Espaçamento entre as tabelas */
        width: 100%; /* Limita a largura total do contêiner */
        display: grid;
        grid-template-columns: repeat(1, 1fr); /* Divide em 3 colunas iguais */
            
        }}

        table {{
            border-collapse: collapse;
            width: 100%;
            max-width: 500px; /* Limita a largura de cada tabela */
            background-color: #ffffff;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        }}

        th, td {{
            border: 1px solid #ddd;
            padding: 10px;
            text-align: left;
        }}

        th {{
            background-color: #5baaa0;
            color: white;
            text-transform: uppercase;
        }}

        @media (max-width: 768px) {{
            .table-container {{
                flex-direction: column; /* Empilha tabelas em telas pequenas */
                align-items: center;
            }}

            table {{
                max-width: 100%; /* Ajusta largura para telas pequenas */
            }}
        }}


    </style>
</head>
<body>
    <script>
        // Função para atualizar a data
        function atualizarData() {{
            const dataAtual = new Date();
            const opcoes = {{ day: '2-digit', month: '2-digit', year: 'numeric' }};
            const dataFormatada = dataAtual.toLocaleDateString('pt-BR', opcoes);
            document.getElementById("data-atual").textContent = dataFormatada;
        }}

        // Atualiza a data ao carregar a página
        window.onload = atualizarData;
    </script>
    <div class="content">
        <header>
            <div class="logo">
                <img src="data:image/png;base64,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" alt="Logo"> 
            <div class="titulo">STATUS DE PRODUÇÃO - PP</div>
            <div class="data" id="data-atual"></div>
        </header>
            <BR>
            <div class="button-container">
            <a href="https://srv-sapmep.enercon.de/web-terminal/com/enercon/terminal/WebTerminal.jsp?ACTIVITY_ID=WEBTERMINAL&USE_SITE=PTA0&TERMINAL=PrimaryParts" class="button" target="_blank">Produção</a>
            <a href="https://srv-sapmep.enercon.de/web-terminal/com/enercon/terminal/WebTerminal.jsp?ACTIVITY_ID=WEBTERMINAL&USE_SITE=PTA0&TERMINAL=PreparationAreas" class="button" target="_blank">Preparação</a>
            <button class="button" onclick="location.reload()">Atualizar</button>
            </div>
            <BR>


            <div class="table-container">
            {tabela_html}
            {tabela_html2}
            </div>
       
    </div>
        <div class="table-container">
        </div>

</body>
</html>

"""

# Salvando o conteúdo HTML em um arquivo
with open(output_html_path, "w", encoding="utf-8") as file:
    file.write(html_content)

print(f"Página HTML gerada com sucesso: {output_html_path}")
