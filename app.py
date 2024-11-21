from flask import Flask, request
from models.task import Task

app = Flask(__name__)

tasks = []

@app.route('/tasks', method=['POST'])
def create_task():
    ...

if __name__ == "__main__":
    app.run(debug=True)