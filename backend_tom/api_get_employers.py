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

if __name__ == '__main__':
    app.run(debug=True, port=8080)