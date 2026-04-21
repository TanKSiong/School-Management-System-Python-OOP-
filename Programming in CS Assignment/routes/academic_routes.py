from flask import Blueprint, request, jsonify
from services.academic_service import AcademicService

academic_bp = Blueprint('academic', __name__)

@academic_bp.route('/', methods=['GET'])
def get_all_academic():
    records = AcademicService.get_all_academic()
    return jsonify(records)

@academic_bp.route('/attendance', methods=['GET'])
def get_attendance_report():
    report = AcademicService.get_attendance_report()
    return jsonify(report)

@academic_bp.route('/stats', methods=['GET'])
def get_categorical_stats():
    stats = AcademicService.get_categorical_stats()
    return jsonify(stats)

@academic_bp.route('/schedule', methods=['GET'])
def get_schedule():
    schedule = AcademicService.get_schedule()
    return jsonify(schedule)

@academic_bp.route('/schedule', methods=['POST'])
def add_schedule():
    data = request.get_json()
    AcademicService.add_schedule(
        data.get('teacher'),
        data.get('classroom'),
        data.get('course_id'),
        data.get('course_name'),
        data.get('lecture_time')
    )
    return jsonify({"status": "success", "message": "Schedule added successfully"})

@academic_bp.route('/attendance/mark', methods=['PUT'])
def mark_attendance():
    data = request.get_json()
    AcademicService.mark_attendance(
        data.get('sid'),
        data.get('cid'),
        data.get('week'),
        data.get('status')
    )
    return jsonify({"status": "success", "message": "Attendance marked successfully"})

@academic_bp.route('/marks/input', methods=['PUT'])
def input_marks():
    data = request.get_json()
    AcademicService.input_marks(
        data.get('sid'),
        data.get('cid'),
        data.get('assess'),
        data.get('final')
    )
    return jsonify({"status": "success", "message": "Marks inputted successfully"})

@academic_bp.route('/marks/update', methods=['PUT'])
def update_marks():
    data = request.get_json()
    AcademicService.update_marks(
        data.get('sid'),
        data.get('cid'),
        data.get('mark_type'),
        data.get('new_val')
    )
    return jsonify({"status": "success", "message": "Marks updated successfully"})

@academic_bp.route('/lessons/<teacher_id>', methods=['GET'])
def get_lesson_plans(teacher_id):
    plans = AcademicService.get_lesson_plans(teacher_id)
    return jsonify(plans)

@academic_bp.route('/lessons', methods=['POST'])
def add_lesson_plan():
    data = request.get_json()
    AcademicService.add_lesson_plan(
        data.get('teacher_id'),
        data.get('cid'),
        data.get('topic'),
        data.get('objectives'),
        data.get('materials')
    )
    return jsonify({"status": "success", "message": "Lesson plan added successfully"})

@academic_bp.route('/report/<teacher_id>', methods=['GET'])
def teacher_report(teacher_id):
    report = AcademicService.get_attendance_report(teacher_id=teacher_id)
    return jsonify(report)

@academic_bp.route('/report/student/<student_id>', methods=['GET'])
def student_report(student_id):
    report = AcademicService.get_attendance_report(student_id=student_id)
    return jsonify(report)
