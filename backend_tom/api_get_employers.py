from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/v1', methods=['GET'])
def get_employees():
    employees = [
        {'id': 1, 'firstName': 'Jean', 'lastName': 'Bafouille', 'emailId': 'jeanbafouille@example.com'},
        {'id': 2, 'firstName': 'Jean', 'lastName': 'Neymar', 'emailId': 'jeanneymar@example.com'},
        {'id': 3, 'firstName': 'Pierre-Paul', 'lastName': 'Jack', 'emailId': 'pierrepauljack@example.com'}
    ]
    return jsonify(employees)

if __name__ == '__main__':
    app.run(debug=True, port=8080)