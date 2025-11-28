# app/routes.py
from flask import Blueprint, render_template, request, redirect, url_for
from app.models import get_all_students

student_bp = Blueprint("students", __name__, url_prefix="/students", template_folder="templates")

# File tạo các route liên quan đến sinh viên, hay gọi là các trang và các hành động CRUD

# Route trang chủ
@student_bp.route("/home")
def home():
    return render_template("home.html")

# Route hiển thị danh sách sinh viên
@student_bp.route("/")
def list_student():
    students = get_all_students()
    return render_template("students.html", students=students)
