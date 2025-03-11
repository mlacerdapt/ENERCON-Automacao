import pygetwindow as gw

def list_open_windows():
    # Obter todas as janelas abertas
    open_windows = gw.getAllTitles()

    # Listar todas as janelas abertas
    for window in open_windows:
        print(window)

# Chamar a função para listar as janelas abertas
list_open_windows()
