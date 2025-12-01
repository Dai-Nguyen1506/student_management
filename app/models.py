# app/models.py
from app.connection import get_connection

# File tạo các hàm thao tác với cơ sở dữ liệu liên quan đến sinh viên

# Lấy tất cả sinh viên từ cơ sở dữ liệu
def get_all_students():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM student")
    students = cursor.fetchall()
    conn.close()
    return students

def get_students_by_info(student_id=None, name=None, email=None, id_program=None, enrollment_year=None):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = "SELECT * FROM student WHERE 1=1"
    values = []

    if student_id:
        query += " AND student_id = %s"
        values.append(student_id)

    if name:
        query += " AND full_name LIKE %s"
        values.append("%" + name + "%")

    if email:
        query += " AND email = %s"
        values.append(email)

    if id_program:
        query += " AND program_id = %s"
        values.append(id_program)

    if enrollment_year:
        query += " AND enrollment_year = %s"
        values.append(enrollment_year)

    cursor.execute(query, tuple(values))
    students = cursor.fetchall()

    cursor.close()
    conn.close()
    return students


def del_student(student_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM student WHERE student_id = %s", (student_id,))
    conn.commit()
    cursor.close()
    conn.close()