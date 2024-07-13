from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from app import db
from app.models import Student
from app.crud import add_student, get_all_students, get_student_by_id, update_student, delete_student
from app.decorators import admin_login_required

bp = Blueprint('routes', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/studentlogin', methods=['GET', 'POST'])
def studentlogin():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        student = Student.query.filter_by(email=email, password=password).first()
        if student:
            return redirect(url_for('routes.user'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('studentlogin.html')

@bp.route('/adminlogin', methods=['GET', 'POST'])
def adminlogin():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if email == 'admin@gmail.com' and password == 'admin':
            session['admin_logged_in'] = True
            flash("Admin login successful! ",'success')
            return redirect(url_for('routes.admin'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('adminlogin.html')

@bp.route('/user')
def user():
    return render_template('user.html')

@bp.route('/myprofile')
def myprofile():
    return render_template('myprofile.html')

@bp.route('/mycredits')
def mycredits():
    return render_template('mycredits.html')

@bp.route('/mycurriculum')
def mycurriculum():
    return render_template('mycurriculum.html')

@bp.route('/myattendance')
def myattendance():
    return render_template('myattendance.html')

@bp.route('/admin')
@admin_login_required
def admin():
    students = get_all_students()
    return render_template('admin.html', students=students)

@bp.route('/admin/addstudent', methods=['GET', 'POST'])
@admin_login_required
def addstudent():
    if request.method == 'POST':
        name = request.form['name']
        mobile_number = request.form['mobile_number']
        address = request.form['address']
        email = request.form['email']
        password = request.form['password']
        add_student(name, mobile_number, address, email, password)
        flash("Student added successfully","success")
        return redirect(url_for('routes.admin'))
    return render_template('addstudent.html')

@bp.route('/admin/editstudent/<int:student_id>', methods=['GET', 'POST'])
@admin_login_required
def editstudent(student_id):
    student = get_student_by_id(student_id)
    if request.method == 'POST':
        name = request.form['name']
        mobile_number = request.form['mobile_number']
        address = request.form['address']
        email = request.form['email']
        password = request.form['password']
        update_student(student_id, name=name, mobile_number=mobile_number, address=address, email=email, password=password)
        return redirect(url_for('routes.admin'))
    return render_template('editstudent.html', student=student)

@bp.route('/admin/deletestudent/<int:student_id>', methods=['POST'])
@admin_login_required
def deletestudent(student_id):
    delete_student(student_id)
    return redirect(url_for('routes.admin'))

@bp.route('/adminlogout')
def adminlogout():
    session.pop('admin_logged_in', None)
    flash('Logged out successfully.', 'success')
    return redirect(url_for('routes.adminlogin'))
