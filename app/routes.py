# app/routes.py
from flask import Blueprint, render_template, request, redirect, url_for, jsonify, flash
from app.models import get_all_students
from app.models import get_students_by_info
from app.models import del_student
from app.models import update_student_by_id
from app.models import add_student
from app.models import get_instructors
from app.models import get_instructors_by_info
from app.models import del_instructor_by_id
from app.models import update_instructor_by_id
from app.models import add_instructor
from app.models import get_all_program
from app.models import is_email_student_exist
from app.models import is_email_instructor_exist

student_bp = Blueprint("students", __name__, url_prefix="/student_management", template_folder="templates")

# File tạo các route liên quan đến sinh viên, hay gọi là các trang và các hành động CRUD

# Route trang giới thiệu
@student_bp.route("/")
def intro():
    return render_template("intro.html")

# Route trang chủ
@student_bp.route("/home")
def home():
    return render_template("home.html")

# Route hiển thị danh sách sinh viên
@student_bp.route("/list_student")
def list_student():
    students = get_all_students()
    programs = get_all_program()
    return render_template("students.html", students=students, programs=programs)

#Route trang chương trình đào tạo
@student_bp.route("/program")
def program():
    return render_template("program.html")

#Route trang giảng viên
@student_bp.route("/instructors")
def instructors():
    instructors = get_instructors()
    return render_template("instructors.html", instructors=instructors)

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

# Route Students -----------------------------------------------------------------------------------------------------------

@student_bp.route("/search", methods=["GET", "POST"])
def search_student():
    if request.method == "POST":
        student_id = request.form.get("student_id")
        student_name = request.form.get("name")
        student_id_program = request.form.get("id_program")
        student_enrollment_year = request.form.get("enrollment_year")

        student = get_students_by_info(student_id, student_name, student_id_program, student_enrollment_year)
        return render_template("students.html", students=student)
    else:
        students = get_all_students()
        return render_template('students.html', students=students)
    
# Route xóa sinh viên theo ID
@student_bp.route("/delete/<student_id>", methods=["POST"])
def delete_student(student_id):
    del_student(student_id)
    return jsonify({"success": True, "message": "Student deleted successfully!"})

# Route update student
@student_bp.route("/update/<student_id>", methods=["POST"])
def update_student(student_id):
    data = request.get_json()
    if not data:
        return jsonify({"success": False, "message": "Missing JSON body"}), 400

    # Map expected fields; keep names consistent with front-end
    full_name = data.get('full_name')
    date_of_birth = data.get('date_of_birth')
    gender = data.get('gender')
    email = data.get('email')
    phone_number = data.get('phone_number')
    address = data.get('address')
    enrollment_year = data.get('enrollment_year')

    update_student_by_id(student_id, full_name, date_of_birth, gender, email, phone_number, address, enrollment_year)

    return jsonify({"success": True, "message": "Student updated successfully!"})

# Route thêm sinh viên
@student_bp.route("/add_student", methods=["GET","POST"])
def add_new_student():
    name = request.form.get("new_sn")
    birth = request.form.get("new_sb")
    gender = request.form.get("new_sg")
    email = request.form.get("new_se")
    phone = request.form.get("new_sp")
    address = request.form.get("new_sa")
    enrollment_year = request.form.get("new_sy")
    program = request.form.get("new_spro")

    if birth == "":
        birth = None

    if phone == "":
        phone = None

    if address == "":
        address = None

        # Kiểm tra email
    if is_email_student_exist(email):
        flash("Email đã tồn tại, vui lòng nhập email khác!", "danger")
        return redirect(url_for('students.list_student'))
    
    try:
        enrollment_year = int(enrollment_year)
    except:
        flash("Yêu cầu nhập đúng thông tin", "danger")
        return redirect(url_for('students.list_student'))

    add_student(name, email, program, enrollment_year, birth, gender = gender, phone = phone, address = address)
    flash("Thêm sinh viên thành công!", "success")
    return redirect(url_for('students.list_student'))

# Route Instructors -----------------------------------------------------------------------------------------------------------

# Route find instructors
@student_bp.route("/search_instructor", methods=["GET", "POST"])
def search_instructors():
    if request.method == "POST":
        instructor_id = request.form.get("instructor_id")
        instructor_name = request.form.get("name")

        instructors = get_instructors_by_info(instructor_id, instructor_name)
        return render_template("instructors.html", instructors = instructors)
    else:
        instructors = get_instructors()
        return render_template('instructors.html', instructors = instructors)

# Route xóa instructors
@student_bp.route("/delete_instructor/<instructor_id>", methods=["POST"])
def delete_instructor(instructor_id):
    del_instructor_by_id(instructor_id)
    return jsonify({"success": True, "message": "Instructor deleted successfully!"})


# Route update instructors
@student_bp.route("/instructors/update/<instructor_id>", methods=["POST"])
def update_instructor(instructor_id):
    data = request.get_json()
    if not data:
        return jsonify({"success": False, "message": "Missing JSON body"}), 400

    full_name = data.get("full_name")
    email = data.get("email")
    specialization = data.get("specialization")
    office_location = data.get("office_location")

    update_instructor_by_id(instructor_id, full_name, email, specialization, office_location)
    return jsonify({"success": True, "message": "Instructor updated successfully!"})

# Route add instructor
@student_bp.route("/add_instructor", methods=["GET","POST"])
def add_new_instructor():
    name = request.form.get("new_in")
    email = request.form.get("new_ie")
    special = request.form.get("new_is")
    locate = request.form.get("new_il")

        # Kiểm tra email
    if is_email_instructor_exist(email):
        flash("Email đã tồn tại, vui lòng nhập email khác!", "danger")
        return redirect(url_for('students.instructors'))

    add_instructor(name, email, special, locate)
    flash("Thêm Instructor thành công!", "success")
    return redirect(url_for('students.instructors'))

# Route Programs  -----------------------------------------------------------------------------------------------------------

