import pygetwindow as gw

# Listar todas as janelas abertas
windows = gw.getAllWindows()

# Exibir o título de cada janela
for window in windows:
    print(window.title)
