from flask import Flask, jsonify, request

app = Flask(__name__)

employees = [
    {'id': 1, 'firstName': 'Jean', 'lastName': 'Bafouille', 'emailId': 'jeanbafouille@example.com'},
    {'id': 2, 'firstName': 'Jean', 'lastName': 'Neymar', 'emailId': 'jeanneymar@example.com'},
    {'id': 3, 'firstName': 'Pierre-Paul', 'lastName': 'Jack', 'emailId': 'pierrepauljack@example.com'}
]

employee_id_counter = len(employees) + 1

@app.route('/api/v1/employees', methods=['GET'])
def get_employees():
    return jsonify(employees)

@app.route('/api/v1/employees', methods=['POST'])
def create_employee():
    global employee_id_counter
    employee = request.json
    employee['id'] = employee_id_counter
    employees.append(employee)
    employee_id_counter += 1
    return jsonify(employee)

@app.route('/api/v1/employees/<int:employee_id>', methods=['DELETE'])
def delete_employee(employee_id):
    global employees
    employee_to_delete = None
    for employee in employees:
        if employee['id'] == employee_id:
            employee_to_delete = employee
            break
    if employee_to_delete:
        employees.remove(employee_to_delete)
        return jsonify({'message': f"L'employé avec l'ID {employee_id} a été supprimé"})
    else:
        return jsonify({'erreur': f"L'employé avec l'ID {employee_id} n'a pas été trouvé"}), 404

@app.route('/api/v1/employees/<int:employee_id>', methods=['PUT'])
def update_employee(employee_id):
    global employees
    employee_to_update = None
    for employee in employees:
        if employee['id'] == employee_id:
            employee_to_update = employee
            break
    if employee_to_update:
        employee_data = request.get_json()
        employee_to_update.update(employee_data)
        return jsonify(employee_to_update)
    else:
        return jsonify({'erreur': f"L'employé avec l'ID {employee_id} n'a pas été trouvé"}), 404

if __name__ == '__main__':
    app.run(debug=True, port=8080)