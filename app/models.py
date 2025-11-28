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
