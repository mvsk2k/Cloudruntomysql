from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Cloud SQL connection parameters (Use environment variables for security)
"""
DB_USER = os.environ.get('DB_USER', 'your_user')
DB_PASSWORD = os.environ.get('DB_PASSWORD', 'your_password')
DB_NAME = os.environ.get('DB_NAME', 'your_database')
DB_CONNECTION_NAME = os.environ.get('DB_CONNECTION_NAME', 'your-project:your-region:your-instance')
"""
DB_USER = 'root'
DB_PASSWORD = 'siva12345'
DB_NAME = 'supersimple'

#'DB_CONNECTION_NAME', 'your-project:your-region:your-instance'
DB_CONNECTION_NAME = 'myownproject241124:us-central1:supermysql'

"""
# SQLAlchemy configuration (Using Cloud SQL Unix Socket)
app.config['SQLALCHEMY_DATABASE_URI'] = (
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@/{DB_NAME}"
    f"?unix_socket=/cloudsql/{DB_CONNECTION_NAME}"
)
"""
#os.environ.get('DB_HOST', 'your-public-ip')
DB_HOST = '34.68.151.103'
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define model corresponding to the existing table
class Employee(db.Model):
    __tablename__ = 'employees'  # Ensure this matches your MySQL table name
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    department = db.Column(db.String(100), nullable=False)
    salary = db.Column(db.Integer, nullable=False)

# Route to read all employees (READ)
@app.route('/employees', methods=['GET'])
def get_employees():
    employees = Employee.query.all()
    result = [{'id': emp.id, 'name': emp.name, 'department': emp.department, 'salary': emp.salary} for emp in employees]
    return jsonify(result), 200

# Route to get a single employee by ID (READ)
@app.route('/employee/<int:emp_id>', methods=['GET'])
def get_employee(emp_id):
    employee = Employee.query.get(emp_id)
    if employee:
        return jsonify({'id': employee.id, 'name': employee.name, 'department': employee.department, 'salary': employee.salary})
    return jsonify({'error': 'Employee not found'}), 404

"""

# Route to add a new employee (CREATE)
@app.route('/employee', methods=['POST'])
def add_employee():
    data = request.get_json()
    new_employee = Employee(name=data['name'], department=data['department'], salary=data['salary'])
    db.session.add(new_employee)
    db.session.commit()
    return jsonify({'message': 'Employee added successfully!'}), 201

# Route to update an existing employee (UPDATE)
@app.route('/employee/<int:emp_id>', methods=['PUT'])
def update_employee(emp_id):
    employee = Employee.query.get(emp_id)
    if employee:
        data = request.get_json()
        employee.name = data.get('name', employee.name)
        employee.department = data.get('department', employee.department)
        employee.salary = data.get('salary', employee.salary)
        db.session.commit()
        return jsonify({'message': 'Employee updated successfully!'}), 200
    return jsonify({'error': 'Employee not found'}), 404

# Route to delete an employee (DELETE)
@app.route('/employee/<int:emp_id>', methods=['DELETE'])
def delete_employee(emp_id):
    employee = Employee.query.get(emp_id)
    if employee:
        db.session.delete(employee)
        db.session.commit()
        return jsonify({'message': 'Employee deleted successfully!'}), 200
    return jsonify({'error': 'Employee not found'}), 404
"""

# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
