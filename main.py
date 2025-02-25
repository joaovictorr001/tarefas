from flask import Flask, request


app = Flask(__name__)


tarefas = [
    {

        'id':1,
        'titulo': "Lavar Louca",
        'descricao': "Lavar os pratos",
        'status': "Nao iniciado",
        'dataInicio':"segunda feira",
        'dataEntrega': "terca feira",
        'dificuldade': "media"

    },
    {
            'id':2,
            'titulo': "Estudar",
            'descricao': "Estudar ",
            'status': "Nao iniciado",
            'dataInicio':"quarta feira",
            'dataEntrega': "quinta feira",
            'dificuldade': "dificil"
    }
]

@app.route('/task', methods = ['GET'])
def get_tasks():
    return tarefas

@app.route('/task/<int:task_id>', methods = ['GET'])
def get_tasks_by_id(task_id):
    for tarefa in tarefas:
        if tarefa.get('id') == task_id:
            return tarefa

    return 'Tarefa nao encontrada'

@app.route('/tasks', methods=['POST'])
def crate_task():
    task = request.json
    ultimo_id = tarefas[-1]. get('id') + 1
    task['id'] = ultimo_id
    tarefas.append(task)
    return task

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task_search = None

    for tarefa in tarefas:
        if tarefa.get('id') == task_id:
            task_search = tarefa

    task_body = request.json
    task_search['titilo'] = task_body.get('titulo')
    task_search['descricao'] = task_body.get('descricao')
    task_search['status'] = task_body.get('status')
    task_search['dataInicio'] = task_body.get('dataInicio')
    task_search['dataEntrega'] = task_body.get('dataEntrega')
    task_search['dificuldade'] = task_body.get('dificuldade')

    return task_search

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    for tarefa in tarefas:
        if tarefa.get('id') == task_id:
            tarefas.remove(tarefa)
    return 'A tarefa foi removida com sucesso'

if __name__ == '__main__':
    app.run(debug=True)