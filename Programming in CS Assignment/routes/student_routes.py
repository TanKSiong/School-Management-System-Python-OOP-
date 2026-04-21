from flask import Blueprint, request, jsonify
from services.student_service import StudentService
from utils.exceptions import APIError

student_bp = Blueprint('students', __name__)

@student_bp.route('/', methods=['GET'])
def get_students():
    students = StudentService.get_all_students()
    return jsonify(students)

@student_bp.route('/', methods=['POST'])
def add_student():
    data = request.get_json()
    StudentService.add_student(
        data.get('sid'),
        data.get('name'),
        data.get('contact'),
        data.get('age')
    )
    return jsonify({"status": "success", "message": "Student added successfully"})

@student_bp.route('/<student_id>', methods=['PUT'])
def update_student(student_id):
    data = request.get_json()
    StudentService.update_student(
        student_id,
        data.get('column'),
        data.get('new_value')
    )
    return jsonify({"status": "success", "message": "Student updated successfully"})

@student_bp.route('/<student_id>', methods=['DELETE'])
def delete_student(student_id):
    StudentService.delete_student(student_id)
    return jsonify({"status": "success", "message": "Student deleted successfully"})
