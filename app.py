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


if __name__ == "__main__":
    app.run(debug=True)