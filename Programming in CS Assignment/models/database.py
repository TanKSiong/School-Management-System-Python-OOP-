import sqlite3
import pandas as pd
import os

DB_PATH = 'educore.db'

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Create tables
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            ID TEXT PRIMARY KEY,
            Name TEXT,
            Contact TEXT,
            Age INTEGER,
            Class TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS employees (
            ID TEXT PRIMARY KEY,
            Name TEXT,
            Contact TEXT,
            Position TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS class_schedule (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Teacher TEXT,
            Classroom TEXT,
            CourseID TEXT,
            CourseName TEXT,
            LectureTime TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS academic_records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            StudentID TEXT,
            StudentName TEXT,
            CourseID TEXT,
            AssessmentMarks REAL,
            FinalExamMarks REAL,
            Week1 TEXT, Week2 TEXT, Week3 TEXT, Week4 TEXT, Week5 TEXT,
            Week6 TEXT, Week7 TEXT, Week8 TEXT, Week9 TEXT, Week10 TEXT,
            Week11 TEXT, Week12 TEXT, Week13 TEXT, Week14 TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS lesson_plans (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            TeacherID TEXT,
            CourseID TEXT,
            Topic TEXT,
            Objectives TEXT,
            Materials TEXT
        )
    ''')
    conn.commit()
    conn.close()

def migrate_csv_to_db():
    if os.path.exists(DB_PATH):
        return  # Already migrated or created
    
    print("Migrating CSV to SQLite Database...")
    init_db()
    conn = get_db_connection()

    csv_mapping = {
        'students.csv': 'students',
        'employees.csv': 'employees',
        'class_schedule.csv': 'class_schedule',
        'academic_records.csv': 'academic_records',
        'lesson_plans.csv': 'lesson_plans'
    }

    for csv_file, table_name in csv_mapping.items():
        if os.path.exists(csv_file):
            try:
                df = pd.read_csv(csv_file)
                df.to_sql(table_name, conn, if_exists='append', index=False)
                print(f"Migrated {csv_file} to {table_name}.")
            except Exception as e:
                print(f"Failed to migrate {csv_file}: {e}")

    conn.close()

if __name__ == "__main__":
    migrate_csv_to_db()
