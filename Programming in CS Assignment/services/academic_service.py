from models.database import get_db_connection
from utils.exceptions import NotFoundError, ValidationError
import pandas as pd
import numpy as np

class AcademicService:
    @staticmethod
    def get_all_academic():
        conn = get_db_connection()
        records = conn.execute('SELECT * FROM academic_records').fetchall()
        conn.close()
        return [dict(x) for x in records]

    @staticmethod
    def get_attendance_report(teacher_id=None, student_id=None):
        conn = get_db_connection()
        query = 'SELECT * FROM academic_records'
        params = []
        
        # If we need filter later, e.g., for teacher's courses, we can join with class_schedule
        if student_id:
            query += ' WHERE StudentID = ?'
            params.append(student_id)
            
        records = conn.execute(query, params).fetchall()
        conn.close()
        
        report = []
        for row in records:
            row_dict = dict(row)
            # Find all weeks
            attendance_cols = [k for k in row_dict.keys() if k.startswith('Week') and row_dict[k] is not None]
            total_weeks = len(attendance_cols)
            if total_weeks == 0:
                continue
                
            present = sum(1 for week in attendance_cols if str(row_dict[week]).strip() == "Present")
            rate = (present / total_weeks) * 100
            status = "OK" if rate >= 80 else "Exam Barred"
            
            # Additional logic for students reporting
            try:
                assess = float(row_dict.get('AssessmentMarks') or 0.0)
            except:
                assess = 0.0
            try:
                final = float(row_dict.get('FinalExamMarks') or 0.0)
            except:
                final = 0.0
                
            total_score = assess + final

            report.append({
                "StudentName": row_dict.get("StudentName", ""),
                "StudentID": row_dict.get("StudentID", ""),
                "CourseID": row_dict.get("CourseID", ""),
                "AttendanceRate": rate,
                "Status": status,
                "ExamStatus": "Allowed" if rate >= 80 else "Barred",
                "TotalScore": total_score,
                "AssessmentMarks": assess,
                "FinalExamMarks": final
            })
        return report

    @staticmethod
    def get_categorical_stats():
        conn = get_db_connection()
        df = pd.read_sql_query('SELECT * FROM academic_records', conn)
        conn.close()

        if df.empty:
            return {}

        df['AssessmentMarks'] = pd.to_numeric(df['AssessmentMarks'], errors='coerce')
        df['FinalExamMarks'] = pd.to_numeric(df['FinalExamMarks'], errors='coerce')
        df['Total'] = df['AssessmentMarks'].fillna(0) + df['FinalExamMarks'].fillna(0)

        stats = {}
        for col in ['AssessmentMarks', 'FinalExamMarks', 'Total']:
            scores = df[col].dropna().values
            if len(scores) == 0:
                continue
            stats[col] = {
                'Average': float(np.mean(scores)),
                'StdDev': float(np.std(scores)),
                'Min': float(np.min(scores)),
                'Max': float(np.max(scores))
            }
        return stats

    @staticmethod
    def get_schedule():
        conn = get_db_connection()
        schedule = conn.execute('SELECT * FROM class_schedule').fetchall()
        conn.close()
        return [dict(ix) for ix in schedule]

    @staticmethod
    def add_schedule(teacher, classroom, course_id, course_name, lecture_time):
        conn = get_db_connection()
        current_courses = conn.execute('SELECT COUNT(*) as count FROM class_schedule WHERE Teacher = ?', (teacher,)).fetchone()
        if dict(current_courses)['count'] >= 2:
            conn.close()
            raise ValidationError(f"{teacher} already has 2 courses assigned.")
            
        conn.execute('''
            INSERT INTO class_schedule (Teacher, Classroom, CourseID, CourseName, LectureTime) 
            VALUES (?, ?, ?, ?, ?)
        ''', (teacher, classroom, course_id, course_name, lecture_time))
        conn.commit()
        conn.close()

    @staticmethod
    def mark_attendance(student_id, course_id, week, status):
        # Only simple column updates
        if not week.startswith('Week'):
            raise ValidationError(f"Invalid week format: {week}")
        conn = get_db_connection()
        record = conn.execute('SELECT * FROM academic_records WHERE StudentID = ? AND CourseID = ?', (student_id, course_id)).fetchone()
        if not record:
            conn.close()
            raise NotFoundError("Record not found for given student and course.")
        
        # update dynamic column
        conn.execute(f"UPDATE academic_records SET {week} = ? WHERE StudentID = ? AND CourseID = ?", (status, student_id, course_id))
        conn.commit()
        conn.close()

    @staticmethod
    def update_marks(student_id, course_id, mark_type, new_value):
        if mark_type not in ['AssessmentMarks', 'FinalExamMarks']:
            raise ValidationError("Invalid mark type.")
        conn = get_db_connection()
        record = conn.execute('SELECT * FROM academic_records WHERE StudentID = ? AND CourseID = ?', (student_id, course_id)).fetchone()
        if not record:
            conn.close()
            raise NotFoundError("Record not found.")

        conn.execute(f"UPDATE academic_records SET {mark_type} = ? WHERE StudentID = ? AND CourseID = ?", (new_value, student_id, course_id))
        conn.commit()
        conn.close()

    @staticmethod
    def input_marks(student_id, course_id, assess, final):
        conn = get_db_connection()
        record = conn.execute('SELECT * FROM academic_records WHERE StudentID = ? AND CourseID = ?', (student_id, course_id)).fetchone()
        if not record:
            conn.close()
            raise NotFoundError("Record not found.")

        conn.execute(f"UPDATE academic_records SET AssessmentMarks = ?, FinalExamMarks = ? WHERE StudentID = ? AND CourseID = ?", (assess, final, student_id, course_id))
        conn.commit()
        conn.close()

    @staticmethod
    def get_lesson_plans(teacher_id):
        conn = get_db_connection()
        plans = conn.execute('SELECT * FROM lesson_plans WHERE TeacherID = ?', (teacher_id,)).fetchall()
        conn.close()
        return [dict(x) for x in plans]

    @staticmethod
    def add_lesson_plan(teacher_id, course_id, topic, objectives, materials):
        conn = get_db_connection()
        conn.execute('''
            INSERT INTO lesson_plans (TeacherID, CourseID, Topic, Objectives, Materials) 
            VALUES (?, ?, ?, ?, ?)
        ''', (teacher_id, course_id, topic, objectives, materials))
        conn.commit()
        conn.close()

