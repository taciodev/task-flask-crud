from flask import Flask, request, jsonify

from models.task import Task

app = Flask(__name__)

tasks = []


@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    title = data.get('title')
    description = data.get('description')
    new_task = Task(title, description)
    tasks.append(new_task)
    return jsonify({'message': 'task created successfully'}), 201


@app.route('/tasks', methods=['GET'])
def get_tasks():
    task_list = [task.to_dict() for task in tasks]
    total_tasks = len(task_list)
    return jsonify({'tasks': task_list, 'total_tasks': total_tasks})


@app.route('/tasks/<id>', methods=['GET'])
def get_task(id):
    for task in tasks:
        if task.id == id: return jsonify(task.to_dict())
    return jsonify({'message': 'could not find the task'}), 404


if __name__ == "__main__":
    app.run(debug=True)