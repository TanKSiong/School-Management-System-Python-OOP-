from models.database import get_db_connection
from utils.exceptions import NotFoundError, ValidationError

class StudentService:
    @staticmethod
    def get_all_students():
        conn = get_db_connection()
        students = conn.execute('SELECT * FROM students').fetchall()
        conn.close()
        return [dict(ix) for ix in students]

    @staticmethod
    def get_student_by_id(student_id):
        conn = get_db_connection()
        student = conn.execute('SELECT * FROM students WHERE ID = ?', (student_id,)).fetchone()
        conn.close()
        if not student:
            raise NotFoundError(f"Student with ID {student_id} not found")
        return dict(student)

    @staticmethod
    def add_student(student_id, name, contact, age):
        if not student_id or not name:
            raise ValidationError("Student ID and Name are required.")
            
        conn = get_db_connection()
        existing = conn.execute('SELECT * FROM students WHERE ID = ?', (student_id,)).fetchone()
        if existing:
            conn.close()
            raise ValidationError(f"Student ID {student_id} already exists.")

        conn.execute('INSERT INTO students (ID, Name, Contact, Age) VALUES (?, ?, ?, ?)',
                     (student_id, name, contact, age))
        conn.commit()
        conn.close()

    @staticmethod
    def update_student(student_id, column, new_value):
        valid_columns = ['Name', 'Contact', 'Age']
        if column not in valid_columns:
            raise ValidationError(f"Invalid update column. Must be one of {valid_columns}")
            
        conn = get_db_connection()
        student = conn.execute('SELECT * FROM students WHERE ID = ?', (student_id,)).fetchone()
        if not student:
            conn.close()
            raise NotFoundError(f"Student {student_id} not found.")

        conn.execute(f'UPDATE students SET {column} = ? WHERE ID = ?', (new_value, student_id))
        conn.commit()
        conn.close()

    @staticmethod
    def delete_student(student_id):
        conn = get_db_connection()
        student = conn.execute('SELECT * FROM students WHERE ID = ?', (student_id,)).fetchone()
        if not student:
            conn.close()
            raise NotFoundError(f"Student {student_id} not found.")

        conn.execute('DELETE FROM students WHERE ID = ?', (student_id,))
        conn.commit()
        conn.close()
