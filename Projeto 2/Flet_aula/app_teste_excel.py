import flet as ft
import pandas as pd
import os

# Configuração do caminho do arquivo Excel
excel_path = r"C:\Users\00082300\Downloads\base_dados.xlsx"

# Verificar se o arquivo existe, caso contrário criar uma base inicial
if not os.path.exists(excel_path):
    df_initial = pd.DataFrame({
        "ID": [1, 2, 3],
        "Nome": ["Produto A", "Produto B", "Produto C"],
        "Quantidade": [10, 5, 8],
        "Cor": ["Amarelo", "Vermelho", "Azul"]
    })
    df_initial.to_excel(excel_path, index=False, engine='openpyxl')

# Função para carregar dados do Excel
def carregar_dados():
    return pd.read_excel(excel_path, engine='openpyxl')

# Função para salvar dados no Excel
def salvar_dados(dataframe):
    dataframe.to_excel(excel_path, index=False, engine='openpyxl')

def main(page: ft.Page):
    page.title = "Sistema de Gerenciamento"
    page.bgcolor = ft.colors.BLACK
    page.scroll = ft.ScrollMode.AUTO

    # Inicializa os dados carregados do Excel
    df = carregar_dados()

    # Container para lista de produtos (precisa ser adicionado antes de usar)
    lista_produtos = ft.Column()

    # Função para atualizar a lista na interface
    def atualizar_lista():
        lista_produtos.controls.clear()
        for _, row in df.iterrows():
            lista_produtos.controls.append(
                ft.Text(
                    f"ID: {row['ID']}, Nome: {row['Nome']}, Quantidade: {row['Quantidade']}, Cor: {row['Cor']}",
                    color=ft.colors.WHITE
                )
            )
        lista_produtos.update()

    # Função para recarregar dados do Excel e atualizar a interface
    def recarregar_dados(e=None):
        nonlocal df
        df = carregar_dados()  # Recarrega do Excel
        atualizar_lista()
        page.snack_bar = ft.SnackBar(
            content=ft.Text("Dados atualizados do Excel com sucesso!")
        )
        page.snack_bar.open = True

    # Função para adicionar um produto
    def adicionar_produto(e):
        nonlocal df
        recarregar_dados()  # Garante que temos os dados mais recentes

        novo_nome = input_nome.value
        nova_quantidade = int(input_quantidade.value)
        nova_cor = dropdown_cor.value

        # Adicionar o novo produto à base de dados
        novo_id = df["ID"].max() + 1 if not df.empty else 1
        novo_produto = {"ID": novo_id, "Nome": novo_nome, "Quantidade": nova_quantidade, "Cor": nova_cor}
        df = pd.concat([df, pd.DataFrame([novo_produto])], ignore_index=True)
        salvar_dados(df)  # Salvar alterações no Excel

        # Atualizar a lista exibida
        atualizar_lista()
        page.snack_bar = ft.SnackBar(
            content=ft.Text("Produto adicionado com sucesso!")
        )
        page.snack_bar.open = True

    # Campos de entrada
    input_nome = ft.TextField(label="Nome do Produto", width=300)
    input_quantidade = ft.TextField(label="Quantidade", width=300, keyboard_type=ft.KeyboardType.NUMBER)
    dropdown_cor = ft.Dropdown(
        label="Cor",
        width=300,
        options=[
            ft.dropdown.Option("Amarelo"),
            ft.dropdown.Option("Vermelho"),
            ft.dropdown.Option("Azul")
        ]
    )

    # Botões para ações
    btn_adicionar = ft.ElevatedButton(
        text="Adicionar Produto",
        on_click=adicionar_produto
    )

    btn_atualizar = ft.ElevatedButton(
        text="Atualizar Dados",
        on_click=recarregar_dados
    )

    # Layout principal
    page.add(
        ft.Column(
            controls=[
                ft.Text("Gerenciamento de Produtos", size=20, color=ft.colors.WHITE),
                input_nome,
                input_quantidade,
                dropdown_cor,
                btn_adicionar,
                btn_atualizar,
                ft.Divider(),
                lista_produtos  # Adiciona `lista_produtos` ao layout
            ],
            spacing=10
        )
    )

    # Atualizar a lista na inicialização
    atualizar_lista()

if __name__ == '__main__':
    ft.app(target=main)
