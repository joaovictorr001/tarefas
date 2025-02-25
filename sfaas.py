from flask import Flask

app = Flask(__name__)

tarefas = [
    {
        "id": 1,
        "titulo": "Estudar javascript",
        "descrição": "estudar para aprender",
        "status":"em andamento"
    },
    {
        "id": 2,
        "titulo": "estudar flask",
        "descrição": "estudar para aprender ",
        "status":"Nao iniciado"
    }
]
@app.route('/task', methods = ['GET'])
def get_tasks():
    return tarefas

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_tasks_by_id(task_id):
    for tarefa in tarefas:
        if tarefa.get('id') == task_id:
            return tarefa

    return 'Tarefa não encontrada'

if __name__ == '__main__':
    app.run(debug=True)