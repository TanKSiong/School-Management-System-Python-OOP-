import os
from flask import Flask, render_template, request, jsonify
from utils.exceptions import APIError
from models.database import migrate_csv_to_db

from routes.student_routes import student_bp
from routes.employee_routes import employee_bp
from routes.academic_routes import academic_bp

# Run database migration/initialization first
migrate_csv_to_db()

# Tell Flask to use 'web_ui' folder for HTML and CSS
app = Flask(__name__, template_folder='web_ui', static_folder='web_ui', static_url_path='')

# Registering blueprints for RESTful architecture
app.register_blueprint(student_bp, url_prefix='/api/students')
app.register_blueprint(employee_bp, url_prefix='/api/employees')
app.register_blueprint(academic_bp, url_prefix='/api/academic')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/admin.html')
def admin_portal():
    return render_template('admin.html')

@app.route('/teacher.html')
def teacher_portal():
    return render_template('teacher.html')

@app.route('/student.html')
def student_portal():
    return render_template('student.html')

# Global error handler for structured API responses
@app.errorhandler(APIError)
def handle_api_error(error):
    response = jsonify({"status": "error", "message": error.message})
    response.status_code = error.status_code
    return response

@app.errorhandler(Exception)
def handle_generic_error(error):
    response = jsonify({"status": "error", "message": "An internal server error occurred."})
    response.status_code = 500
    print(f"Server Error: {error}")
    return response

if __name__ == '__main__':
    print("🚀 Starting EduCore Web Server! Open http://127.0.0.1:5000 in your browser.")
    app.run(debug=True, port=5000)
