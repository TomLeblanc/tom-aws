import unittest
import json
from app import app, employees

class TestEmployeeAPI(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        self.headers = {'Content-Type': 'application/json'}

    def test_get_employees(self):
        response = self.app.get('/api/v1/employees')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), len(employees))

    def test_create_employee(self):
        new_employee = {'firstName': 'Jean', 'lastName': 'Dupont', 'emailId': 'jeandupont@example.com'}
        response = self.app.post('/api/v1/employees', data=json.dumps(new_employee), headers=self.headers)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['firstName'], new_employee['firstName'])
        self.assertEqual(data['lastName'], new_employee['lastName'])
        self.assertEqual(data['emailId'], new_employee['emailId'])
        self.assertEqual(len(employees), 4)

    def test_delete_non_existing_employee(self):
        employee_id = 999
        response = self.app.delete(f'/api/v1/employees/{employee_id}')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['erreur'], f"L'employé avec l'ID {employee_id} n'a pas été trouvé")

    def test_update_non_existing_employee(self):
        employee_id = 999
        new_employee_data = {'firstName': 'Jean-Pierre', 'lastName': 'Bafouille', 'emailId': 'jeanpierrebafouille@example.com'}
        response = self.app.put(f'/api/v1/employees/{employee_id}', data=json.dumps(new_employee_data), headers=self.headers)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['erreur'], f"L'employé avec l'ID {employee_id} n'a pas été trouvé")

if __name__ == '__main__':
    unittest.main()
