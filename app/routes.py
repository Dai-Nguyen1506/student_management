# app/routes.py
from flask import Blueprint, render_template, request, redirect, url_for
from app.models import get_all_students
from app.models import get_students_by_info
from app.models import del_student

student_bp = Blueprint("students", __name__, url_prefix="/students", template_folder="templates")

# File tạo các route liên quan đến sinh viên, hay gọi là các trang và các hành động CRUD

# Route trang giới thiệu
@student_bp.route("/intro")
def intro():
    return render_template("intro.html")

# Route trang chủ
@student_bp.route("/home")
def home():
    return render_template("home.html")

# Route hiển thị danh sách sinh viên
@student_bp.route("/")
def list_student():
    students = get_all_students()
    return render_template("students.html", students=students)

#Route trang chương trình đào tạo
@student_bp.route("/program")
def program():
    return render_template("program.html")

#Route trang giảng viên
@student_bp.route("/instructors")
def instructors():
    return render_template("instructors.html")

#Route trang khóa học
@student_bp.route("/courses")
def courses():
    return render_template("courses.html")

#Route trang đăng ký học phần
@student_bp.route("/enrollment")
def enrollment():
    return render_template("enrollment.html")

#Route trang học phí
@student_bp.route("/tuition_fee")
def tuition_fee():
    return render_template("tuition_fee.html")

#Route trang thanh toán
@student_bp.route("/payment")
def payment():
    return render_template("payment.html")




# Các route khác liên quan đến sinh viên có thể được thêm vào đây
# Route hiển thị tìm kiếm sinh viên theo ID
@student_bp.route("/search", methods=["GET", "POST"])
def search_student():
    if request.method == "POST":
        student_id = request.form.get("student_id")
        student_name = request.form.get("name")
        student_email = request.form.get("email")
        student_id_program = request.form.get("id_program")
        student_enrollment_year = request.form.get("enrollment_year")

        student = get_students_by_info(student_id, student_name, student_email, student_id_program, student_enrollment_year)
        return render_template("students.html", students=student)
    else:
        students = get_all_students()
        return render_template('students.html', students=students)
    
# Route xóa sinh viên theo ID
@student_bp.route("/delete/<student_id>", methods=["POST"])
def delete_student(student_id):
    del_student(student_id)
    return "", 200
