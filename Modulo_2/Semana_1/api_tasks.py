from flask import Flask, request, jsonify

import json
import os

app = Flask(__name__)

TASKS_FILE = 'tasks.json'
STATUS = ['To do', 'In Progress', 'Done']

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    try:
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    except (json.JSONDecodeError, IOError):
        return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)



def validate_task(data,existing_tasks):
    errors = []
    if not data.get('id'):
        errors.append('ID is required')
    elif any(task['id'] == data['id'] for task in existing_tasks):
        errors.append('ID already exists')

    if not data.get('title'):
        errors.append('Title is required')

    if not data.get('description'):
        errors.append('Description is required')
    
    status = data.get('status')
    if not status:
        errors.append('Status is required')
    elif status not in STATUS:
        errors.append(f"Status must be one of: {','.join(STATUS)}.")
    return errors

#API Endpoints

#READ
@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = load_tasks()
    status = request.args.get('status')
    if status:
        if status not in STATUS:
            return jsonify({'error': f'Invalid Status'}), 400
        tasks = [task for task in tasks if task['status'] == status]
    return jsonify(tasks), 200

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    tasks = load_tasks()
    task = next((task for task in tasks if task['id'] == task_id), None)
    if not task:
        return jsonify({'error': 'Task not found'}), 404
    return jsonify(task), 200


#CREATE
@app.route('/tasks', methods=['POST'])
def create_task():
    tasks = load_tasks()
    data = request.json
    errors = validate_task(data, tasks)
    if errors:
        return jsonify ({'errors': errors}), 400
    tasks.append(data)
    save_tasks(tasks)
    return jsonify ({'message':'Task created successfully'}), 201

#UPDATE
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    tasks = load_tasks()
    task = next((task for task in tasks if task['id'] == task_id), None)
    if not task:
        return jsonify({'error': 'Task not found'}), 404
    
    data = request.json

    if 'id' in data and data['id'] != task_id:
        return jsonify({'error': 'Cannot modify task ID'}), 400

    if 'status' in data and data['status'] not in STATUS:
        return jsonify({'error': f'Status must be one of: {", ".join(STATUS)}.'}), 400
    
    for field in ['title', 'description', 'status']:
        if field in data and not data[field]:
            return jsonify({'error': f'{field.capitalize()} cannot be empty'}), 400


    task.update(data)
    save_tasks(tasks)
    return jsonify({'message': 'Task updated successfully'}), 200

#DELETE
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    tasks = load_tasks()
    new_list_tasks = [task for task in tasks if task['id'] != task_id]
    
    if len(new_list_tasks) == len(tasks):
        return jsonify({'error': 'Task not found'}), 404
    
    save_tasks(new_list_tasks)
    return jsonify({'message': 'Task deleted successfully'}), 200


@app.route('/')
def index():
    return {'message': 'Welcome to the Task Management API'}, 200



if __name__ == '__main__':
    app.run(host="localhost", debug=True)