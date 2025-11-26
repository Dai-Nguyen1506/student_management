# app/models.py
from app.connection import get_connection

# File tạo các hàm thao tác với cơ sở dữ liệu liên quan đến sinh viên

def get_all_students():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM student")
    students = cursor.fetchall()
    conn.close()
    return students

def add(name, age, major):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO student (name, age, major) VALUES (%s, %s, %s)", (name, age, major))
    conn.commit()
    conn.close()

def delete(student_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM student WHERE id = %s", (student_id,))
    conn.commit()
    conn.close()

