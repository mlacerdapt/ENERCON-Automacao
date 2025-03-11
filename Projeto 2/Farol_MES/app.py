from flask import Flask, jsonify, render_template
from threading import Timer
import time
import json
import os

app = Flask(__name__)

# Dados simulados - lista de tarefas
data_file = "tasks.json"

# Função para criar o arquivo JSON se não existir
def init_data_file():
    if not os.path.exists(data_file):
        tasks = [
            {"id": 1, "task": "Analisar relatórios", "status": "Pendente"},
            {"id": 2, "task": "Enviar e-mails de follow-up", "status": "Concluído"},
            {"id": 3, "task": "Atualizar planilha de vendas", "status": "Em andamento"}
        ]
        with open(data_file, "w") as f:
            json.dump(tasks, f)

# Carregar dados do arquivo JSON
def load_tasks():
    with open(data_file, "r") as f:
        return json.load(f)

# Atualizar dados no arquivo JSON periodicamente
def update_tasks():
    tasks = load_tasks()
    # Simulação de atualização de status das tarefas
    for task in tasks:
        if task["status"] == "Pendente":
            task["status"] = "Em andamento"
        elif task["status"] == "Em andamento":
            task["status"] = "Concluído"
    
    # Salvar atualizações no arquivo
    with open(data_file, "w") as f:
        json.dump(tasks, f)
    
    # Agendar próxima atualização em 30 minutos (1800 segundos)
    Timer(1800, update_tasks).start()

# Rota para fornecer os dados das tarefas
@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    tasks = load_tasks()
    return jsonify(tasks)

# Rota para a página HTML
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    init_data_file()  # Inicializar o arquivo JSON
    update_tasks()  # Iniciar o processo de atualização periódica
    app.run(host='192.168.221.32', port=5000, debug=True)  # Tornar acessível na rede
