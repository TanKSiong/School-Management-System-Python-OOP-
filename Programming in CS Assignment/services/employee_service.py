from models.database import get_db_connection
from utils.exceptions import NotFoundError, ValidationError

class EmployeeService:
    @staticmethod
    def get_all_employees():
        conn = get_db_connection()
        employees = conn.execute('SELECT * FROM employees').fetchall()
        conn.close()
        return [dict(ix) for ix in employees]

    @staticmethod
    def add_employee(emp_id, name, contact, position):
        if not emp_id or not name:
            raise ValidationError("Employee ID and Name are required.")
            
        conn = get_db_connection()
        existing = conn.execute('SELECT * FROM employees WHERE ID = ?', (emp_id,)).fetchone()
        if existing:
            conn.close()
            raise ValidationError(f"Employee ID {emp_id} already exists.")

        conn.execute('INSERT INTO employees (ID, Name, Contact, Position) VALUES (?, ?, ?, ?)',
                     (emp_id, name, contact, position))
        conn.commit()
        conn.close()

    @staticmethod
    def update_employee(emp_id, column, new_value):
        valid_columns = ['Name', 'Contact', 'Position']
        if column not in valid_columns:
            raise ValidationError(f"Invalid update column. Must be one of {valid_columns}")
            
        conn = get_db_connection()
        emp = conn.execute('SELECT * FROM employees WHERE ID = ?', (emp_id,)).fetchone()
        if not emp:
            conn.close()
            raise NotFoundError(f"Employee {emp_id} not found.")

        conn.execute(f'UPDATE employees SET {column} = ? WHERE ID = ?', (new_value, emp_id))
        conn.commit()
        conn.close()

    @staticmethod
    def delete_employee(emp_id):
        conn = get_db_connection()
        emp = conn.execute('SELECT * FROM employees WHERE ID = ?', (emp_id,)).fetchone()
        if not emp:
            conn.close()
            raise NotFoundError(f"Employee {emp_id} not found.")

        conn.execute('DELETE FROM employees WHERE ID = ?', (emp_id,))
        conn.commit()
        conn.close()
