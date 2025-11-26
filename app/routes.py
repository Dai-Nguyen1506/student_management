# app/routes.py
from flask import Blueprint, render_template, request, redirect, url_for
from app.models import get_all_students
from app.models import add

student_bp = Blueprint("students", __name__, url_prefix="/students", template_folder="templates")

# File tạo các route liên quan đến sinh viên, hay gọi là các trang và các hành động CRUD

# Route trang chủ
@student_bp.route("/home")
def home():
    return render_template("index.html")

# Route hiển thị danh sách sinh viên
@student_bp.route("/")
def list_student():
    students = get_all_students()
    return render_template("students.html", students=students)

# Route hiển thị form + xử lý POST
@student_bp.route("/add", methods=["GET", "POST"])
def add_student():
    if request.method == "POST":
        name = request.form["name"]
        age = request.form["age"]
        major = request.form["major"]

        add(name, age, major)

        return redirect(url_for("students.list_student"))
    
    return render_template("add_student.html")