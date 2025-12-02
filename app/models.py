# app/models.py
from app.connection import get_connection

# File tạo các hàm thao tác với cơ sở dữ liệu liên quan đến sinh viên

# Lấy tất cả sinh viên từ cơ sở dữ liệu
def get_all_students():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query =  """
        SELECT 
            s.*,
            p.program_name
        FROM student s
        LEFT JOIN program p ON s.program_id = p.program_id
    """
    cursor.execute(query)
    students = cursor.fetchall()
    conn.close()
    return students

def get_students_by_info(student_id=None, name=None, id_program=None, enrollment_year=None):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
        SELECT 
            s.*, 
            p.program_name
        FROM student s
        LEFT JOIN program p ON s.program_id = p.program_id
        WHERE 1=1
    """

    values = []

    if student_id:
        query += " AND s.student_id = %s"
        values.append(student_id)

    if name:
        query += " AND s.full_name LIKE %s"
        values.append("%" + name + "%")

    if id_program:
        query += " AND s.program_id = %s"
        values.append(id_program)

    if enrollment_year:
        query += " AND s.enrollment_year = %s"
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


def update_student_by_id(student_id, full_name=None, date_of_birth=None, gender=None, email=None,
                        phone_number=None, address=None, enrollment_year=None):
    """Update student fields. Only provided fields will be updated."""
    conn = get_connection()
    cursor = conn.cursor()

    fields = []
    values = []

    if full_name is not None:
        fields.append('full_name = %s')
        values.append(full_name)
    if date_of_birth is not None:
        fields.append('date_of_birth = %s')
        values.append(date_of_birth)
    if gender is not None:
        fields.append('gender = %s')
        values.append(gender)
    if email is not None:
        fields.append('email = %s')
        values.append(email)
    if phone_number is not None:
        fields.append('phone_number = %s')
        values.append(phone_number)
    if address is not None:
        fields.append('address = %s')
        values.append(address)
    if enrollment_year is not None:
        fields.append('enrollment_year = %s')
        values.append(enrollment_year)

    if fields:
        query = 'UPDATE student SET ' + ', '.join(fields) + ' WHERE student_id = %s'
        values.append(student_id)
        cursor.execute(query, tuple(values))
        conn.commit()

    cursor.close()
    conn.close()

def add_student(name, email, program, enrollment_year, birthday, gender, phone, address):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO student(full_name, date_of_birth, gender, email, phone_number, address, program_id, enrollment_year) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
        (name, birthday, gender, email, phone, address, program, enrollment_year)
    )
    conn.commit()
    conn.close()

def is_email_student_exist(email):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM student WHERE email=%s", (email,))
    exists = cursor.fetchone()[0] > 0
    conn.close()
    return exists


# --------------------------------------------------------------------------------------------------------------

def get_instructors():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM instructor")
    instructors = cursor.fetchall()
    conn.close()
    return instructors


def get_instructors_by_info(instructor_id=None, name=None, email=None):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = "SELECT * FROM instructor WHERE 1=1"
    values = []

    if instructor_id:
        query += " AND instructor_id = %s"
        values.append(instructor_id)

    if name:
        query += " AND full_name LIKE %s"
        values.append('%' + name + '%')

    if email:
        query += " AND email = %s"
        values.append(email)

    cursor.execute(query, tuple(values))
    instructors = cursor.fetchall()

    cursor.close()
    conn.close()
    return instructors

# (duplicate removed) get_instructors_by_info already defined above (supports id, name, email)

def del_instructor_by_id(instructor_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM instructor WHERE instructor_id = %s", (instructor_id,))
    conn.commit()
    cursor.close()
    conn.close()


def update_instructor_by_id(instructor_id, full_name=None, email=None, specialization=None, office_location=None):
    """Update instructor fields. Only provided fields will be updated."""
    conn = get_connection()
    cursor = conn.cursor()

    # Build dynamic SET clause based on provided values
    fields = []
    values = []

    if full_name is not None:
        fields.append("full_name = %s")
        values.append(full_name)
    if email is not None:
        fields.append("email = %s")
        values.append(email)
    if specialization is not None:
        fields.append("specialization = %s")
        values.append(specialization)
    if office_location is not None:
        fields.append("office_location = %s")
        values.append(office_location)

    if fields:
        query = "UPDATE instructor SET " + ", ".join(fields) + " WHERE instructor_id = %s"
        values.append(instructor_id)
        cursor.execute(query, tuple(values))
        conn.commit()

    cursor.close()
    conn.close()

def add_instructor(name, email, specialization, office_location):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO instructor(full_name, email, specialization, office_location) VALUES (%s, %s, %s, %s)",
        (name, email, specialization, office_location)
    )
    conn.commit()
    conn.close()

def is_email_instructor_exist(email):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM instructor WHERE email=%s", (email,))
    exists = cursor.fetchone()[0] > 0
    conn.close()
    return exists

# ---------------------------------------------------------------------------------------------------------------------

def get_all_program():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM program")
    all_program = cursor.fetchall()
    conn.close()
    return all_program
