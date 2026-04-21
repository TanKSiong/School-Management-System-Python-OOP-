from flask import Blueprint, request, jsonify
from services.employee_service import EmployeeService

employee_bp = Blueprint('employees', __name__)

@employee_bp.route('/', methods=['GET'])
def get_employees():
    employees = EmployeeService.get_all_employees()
    return jsonify(employees)

@employee_bp.route('/', methods=['POST'])
def add_employee():
    data = request.get_json()
    EmployeeService.add_employee(
        data.get('emp_id'),
        data.get('name'),
        data.get('contact'),
        data.get('position')
    )
    return jsonify({"status": "success", "message": "Employee added successfully"})

@employee_bp.route('/<emp_id>', methods=['PUT'])
def update_employee(emp_id):
    data = request.get_json()
    EmployeeService.update_employee(
        emp_id,
        data.get('column'),
        data.get('new_value')
    )
    return jsonify({"status": "success", "message": "Employee updated successfully"})

@employee_bp.route('/<emp_id>', methods=['DELETE'])
def delete_employee(emp_id):
    EmployeeService.delete_employee(emp_id)
    return jsonify({"status": "success", "message": "Employee deleted successfully"})
