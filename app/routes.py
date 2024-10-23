
from flask import (Blueprint, flash, redirect, render_template, request,
                   session, url_for)
from app import db
from app.crud import (add_attendance, add_branch, add_course,
                      addcourse_student, add_faculty, add_marks,
                      add_student, delete_attendance, delete_branch,
                      delete_course, delete_faculty, delete_marks,
                      delete_student, get_all_attendance, get_all_branches,
                      get_all_courses, get_all_faculty, get_all_marks,
                      get_all_students, get_attendance_by_coursecode,
                      get_attendance_by_username, get_branch_by_id,
                      get_course_by_id, get_courses_for_student,
                      get_faculty_by_id, get_marks_by_course,
                      get_marks_by_username, get_student_by_id,
                      get_students_for_course, remove_course_from_student,
                      update_attendance, update_branch, update_course,
                      update_faculty, update_marks, update_student,
                      update_student_login)
from app.decorators import admin_login_required, faculty_login_required, admin_or_faculty_login_required
from app.models import (Admin, Attendance, Branch, Course, Faculty, Marks,
                        Student,NotificationStudent,NotificationFaculty)

bp = Blueprint('routes', __name__)
#home page
@bp.route('/')
def index():
    return render_template('index.html')
#student login page
@bp.route('/studentlogin', methods=['GET', 'POST'])
def studentlogin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        student = Student.query.filter_by(username=username).first()
        if student and student.check_password(password):
            session['username']=student.username
            session['role']='student'
            flash("Student login successful! ",'success')
            return redirect(url_for('routes.student'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('studentlogin.html')
#admin login page
@bp.route('/adminlogin', methods=['GET', 'POST'])
def adminlogin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        admin = Admin.query.filter_by(username=username,password=password).first()
        if username == 'admin' and password == 'admin' or admin:
            session['admin_logged_in'] = True
            session['username']='admin'
            flash("Admin login successful! ",'success')
            return redirect(url_for('routes.admin'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('adminlogin.html')
#faculty login page
@bp.route('/facultylogin', methods=['GET', 'POST'])
def facultylogin():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        faculty = Faculty.query.filter_by(email=email,password=password).first()
        if email == 'faculty@gmail.com' and password == 'faculty' or faculty:
            session['faculty_logged_in'] = True
            session['username']=faculty.faculty_code
            session['role']='faculty'
            flash("Faculty login successful! ",'success')
            return redirect(url_for('routes.faculty'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('facultylogin.html')
# student main page
@bp.route('/student')
def student():
    return render_template('student.html')
#faculty main page
@bp.route('/faculty')
@faculty_login_required
def faculty():
    return render_template('faculty.html')
#admin main page
@bp.route('/admin')
@admin_login_required
def admin():
    return render_template('admin.html')
@bp.route('/home/')
def home():
    if session['role']=='student':
        notifications = NotificationStudent.query.filter_by(recipient_username=session['username']).all()
        return render_template('home.html', notifications=notifications)
    if session['role']=='faculty':
        notifications = NotificationFaculty.query.filter_by(recipient_username=session['username']).all()
        return render_template('home.html', notifications=notifications)
    

#CRUD Student C
@bp.route('/addstudent', methods=['GET', 'POST'])
@admin_login_required
def addstudent():
    if request.method == 'POST':
        username=request.form['username']
        email = request.form['email']
        password = request.form['password']
        full_name = request.form['full_name']
        mobile_number = request.form['mobile_number']
        address = request.form['address']
        year_of_joining = request.form['year_of_joining']
        branch_code = request.form['branch_code']
        current_semester = request.form['current_semester']
        cgpa = request.form['cgpa']

        add_student(username, email, password, full_name, mobile_number, address, year_of_joining, branch_code, current_semester, cgpa)
        flash("Student added successfully", "success")
        return redirect(url_for('routes.admin'))
    # Query the database for existing faculties and branch codes
    branches = Branch.query.all()
    return render_template('addstudent.html',branches=branches)

@bp.route('/studentregister', methods=['GET', 'POST'])
def registerstudent():
    if request.method == 'POST':
        username=request.form['username']
        email = request.form['email']
        password = request.form['password']
        full_name = request.form['full_name']
        mobile_number = request.form['mobile_number']
        address = request.form['address']
        year_of_joining = request.form['year_of_joining']
        branch_code = request.form['branch_code']
        current_semester = request.form['current_semester']
        cgpa = request.form['cgpa']

        add_student(username, email, password, full_name, mobile_number, address, year_of_joining, branch_code, current_semester, cgpa)
        flash("Student added successfully", "success")
        return render_template('student.html')
    # Query the database for existing faculties and branch codes
    branches = Branch.query.all()
    return render_template('register.html',branches=branches)
#CRUD Student U
@bp.route('/editstudent/<string:username>', methods=['GET', 'POST'])
@admin_login_required
def editstudent(username):
    student=get_student_by_id(username)
    if request.method == 'POST':
        email=request.form['email']
        full_name=request.form['full_name']
        mobile_number=request.form['mobile_number']
        address=request.form['address']
        year_of_joining=request.form['year_of_joining']
        branch_code=request.form['branch_code']
        current_semester=request.form['current_semester']
        cgpa=request.form['cgpa']
        update_student(username,email,full_name,mobile_number,address,year_of_joining,branch_code,current_semester,cgpa)
        flash("Student details updated successfully", "success")
        return redirect(url_for('routes.managestudent'))
    branches = Branch.query.all()
    return render_template('editstudent.html',student=student,branches=branches)
#CRUD Student U Login
@admin_login_required
@bp.route('/editstudent_login/<string:username>', methods=['GET', 'POST'])
def editstudent_login(username):
    student=get_student_by_id(username)
    if request.method == 'POST':
        password=request.form['password']
        update_student_login(username,password)
        flash("Student login details updated successfully", "success")
        return redirect(url_for('routes.managestudent'))
    return render_template('editstudentlogin.html', student=student)
#CRUD Student D
@bp.route('/admin/deletestudent', methods=['POST'])
@admin_login_required
def deletestudent():
    username = request.form['username']
    delete_student(username)
    flash('Student deleted successfully', 'success')
    return redirect(url_for('routes.managestudent'))
#CRUD Student R
@bp.route('/managestudent', methods=['POST','GET'])
def managestudent():
    students = get_all_students()
    return render_template('viewstudent.html', students=students)
#CRUD Student Search
@bp.route('/searchstudent', methods=['GET','POST'])
def searchstudent():
    if request.method == 'POST':
        username = request.form['username']
        student = get_student_by_id(username)
        if student:
            return render_template('viewstudent.html', students=[student])
        else:
            flash('No student found with that username', 'danger')
            return redirect(url_for('routes.managestudent'))
    return redirect(url_for('routes.managestudent'))
##############################################
#CRUD Course C
@bp.route('/addcourse', methods=['GET', 'POST'])
@admin_login_required
def addcourse():
    if request.method == 'POST':
        course_code = request.form['course_code']
        course_name = request.form['course_name']
        credits = request.form['credits']
        course_instructor_code = request.form['course_instructor_code']
        branch_code = request.form['branch_code']
        add_course(course_code, course_name, credits, course_instructor_code, branch_code)
        flash('Course added successfully', 'success')
        return redirect(url_for('routes.admin'))
    # Query the database for existing faculties and branch codes
    faculties = Faculty.query.all()
    branches = Branch.query.all()
    return render_template('addcourse.html',faculties=faculties,branches=branches)
#CRUD Course U
@bp.route('/editcourse/<string:course_code>', methods=['GET', 'POST'])
@admin_login_required
def editcourse(course_code):
    if request.method == 'POST':
        course_name = request.form['course_name']
        credits = request.form['credits']
        course_instructor_code = request.form['course_instructor_code']
        branch_code = request.form['branch_code']
        update_course(course_code,course_name,credits,course_instructor_code,branch_code)
        flash('Course updated successfully', 'success')
        return redirect(url_for('routes.managecourse'))
    # Query the database for existing faculties and branch codes
    faculties = Faculty.query.all()
    branches = Branch.query.all()
    return render_template('editcourse.html', course_code=course_code,faculties=faculties,branches=branches)

#CRUD Course D
@bp.route('/deletecourse', methods=['POST'])
@admin_login_required
def deletecourse():
    course_code = request.form['course_code']
    delete_course(course_code)
    flash('Course deleted successfully', 'success')
    return redirect(url_for('routes.managecourse'))
#CRUD Course R
@bp.route('/managecourse', methods=['POST','GET'])

def managecourse():
    courses = get_all_courses()
    return render_template('viewcourses.html', courses=courses)
#CRUD Course Search
@bp.route('/searchcourse', methods=['GET','POST'])
def searchcourse():
    if request.method == 'POST':
        course_code = request.form['course_code']
        course = get_course_by_id(course_code)
        if course:
            return render_template('viewcourses.html', courses=[course])
        else:
            flash('No course found with that course code', 'danger')
            return redirect(url_for('managecourse'))
    return redirect(url_for('managecourse'))
################################################################
#CRUD Branch C
@bp.route('/addbranch', methods=['GET','POST'])
@admin_login_required
def addbranch():
    if request.method == 'POST':
        branch_code = request.form['branch_code']
        branch_name = request.form['branch_name']
        add_branch(branch_code, branch_name)
        flash('Branch added successfully', 'success')
        return redirect(url_for('routes.admin'))
    return render_template('addbranch.html')
#CRUD Branch U
@bp.route('/editbranch/<string:branch_code>', methods=['GET', 'POST'])
@admin_login_required
def editbranch(branch_code):
    branch = get_branch_by_id(branch_code)
    if request.method == 'POST':
        branch_name = request.form['branch_name']
        update_branch(branch_code, branch_name)
        flash('Branch updated successfully', 'success')
        return redirect(url_for('routes.managebranch'))
    return render_template('editbranch.html', branch=branch)
#CRUD Branch D
@bp.route('/deletebranch', methods=['POST'])
@admin_login_required
def deletebranch():
    branch_code = request.form['branch_code']
    delete_branch(branch_code)
    flash('Branch deleted successfully', 'success')
    return redirect(url_for('routes.managebranch'))
#CRUD Branch R
@bp.route('/managebranch', methods=['POST','GET'])

def managebranch():
    branches = get_all_branches()
    return render_template('viewbranch.html', branches=branches)
#CRUD Branch Search
@bp.route('/searchbranch', methods=['GET','POST'])

def searchbranch():
    if request.method == 'POST':
        branch_code = request.form['branch_code']
        branch = get_branch_by_id(branch_code)
        if branch:
            return render_template('viewbranch.html', branches=[branch])
        else:
            flash('No branch found with that branch code', 'danger')
            return redirect(url_for('routes.managebranch'))
    return redirect(url_for('routes.managebranch'))
##########################################################
#CRUD Faculty C
@bp.route('/addfaculty', methods=['GET', 'POST'])
@admin_login_required
def addfaculty():
    if request.method == 'POST':
        faculty_code=request.form['faculty_code']
        full_name = request.form['full_name']
        email = request.form['email']
        password = request.form['password']
        cabin_number = request.form['cabin_number']
        specialization = request.form['specialization']
        add_faculty(faculty_code,full_name, email, password, cabin_number, specialization)
        flash("Faculty added successfully", "success")
        return redirect(url_for('routes.admin'))
    return render_template('addfaculty.html')
#CRUD Faculty U
@bp.route('/editfaculty/<string:faculty_code>', methods=['GET', 'POST'])
@admin_login_required
def editfaculty(faculty_code):
    faculty = get_faculty_by_id(faculty_code)
    if request.method == 'POST':
        full_name = request.form['full_name']
        email = request.form['email']

        cabin_number = request.form['cabin_number']
        specialization = request.form['specialization']
        update_faculty(faculty_code, full_name, email, cabin_number, specialization)
        flash('Faculty updated successfully', 'success')
        return redirect(url_for('routes.managefaculty'))
    return render_template('editfaculty.html', faculty=faculty)
#CRUD Faculty D
@bp.route('/deletefaculty', methods=['POST'])
@admin_login_required
def deletefaculty():
    faculty_code = request.form['faculty_code']
    delete_faculty(faculty_code)
    flash('Faculty deleted successfully','success')
    return redirect(url_for('routes.managefaculty'))

@bp.route('/managefaculty', methods=['POST','GET'])
def managefaculty():
    faculties =get_all_faculty()
    return render_template('viewfaculty.html', faculties=faculties)

@bp.route('/searchfaculty', methods=['GET','POST'])

def searchfaculty():
    if request.method == 'POST':
        faculty_code = request.form['faculty_code']
        faculty = get_faculty_by_id(faculty_code)
        if faculty:
            return render_template('viewfaculty.html', faculties=[faculty])
        else:
            flash('No faculty found with that faculty code', 'danger')
            return redirect(url_for('routes.managefaculty'))
    return redirect(url_for('routes.managefaculty'))
########################################################
#Admin Logout
@admin_login_required
@bp.route('/adminlogout')
def adminlogout():
    session.pop('admin_logged_in', None)
    flash('Logged out successfully.', 'success')
    return redirect(url_for('routes.adminlogin'))
#Faculty Logout
@faculty_login_required
@bp.route('/facultylogout')
def facultytlogout():
    session.pop('faculty_logged_in', None)
    flash('Logged out successfully.', 'success')
    return redirect(url_for('routes.facultylogin'))

#Student Logout
@bp.route('/studentlogout')
def studentlogout():
    session.pop('username', None)
    flash('Logged out successfully.', 'success')
    return redirect(url_for('routes.studentlogin'))

######################################################
#Add marks
@admin_or_faculty_login_required
@bp.route('/addmarks',methods=['POST','GET'])
def addmarks():
    if request.method == 'POST':
        username=request.form['username']
        course_code=request.form['course_code']
        ExamType=request.form['ExamType']
        marks_obtained=request.form['marks_obtained']
        max_marks=request.form['max_marks']

        add_marks(username,course_code,ExamType,marks_obtained,max_marks)
        flash('Marks added successfully','success')
        return redirect(url_for('routes.admin'))
    students=get_all_students()
    courses=get_all_courses()
    return render_template('addmarks.html',students=students,courses=courses)

#Update Marks
@admin_or_faculty_login_required
@bp.route('/editmarks/<string:username>/<string:course_code>',methods=['GET','POST'])
def editmarks(username,course_code):
    marks_record = Marks.query.filter_by(username=username, course_code=course_code).first()
    if not marks_record:
        flash('Marks record not found', 'danger')
        return redirect(url_for('routes.admin'))

    if request.method == 'POST':
        ExamType = request.form['ExamType']
        marks_obtained = request.form['marks_obtained']
        max_marks = request.form['max_marks']
        
        # Update marks
        update_marks(username, course_code, ExamType, marks_obtained, max_marks)
        flash('Marks updated successfully', 'success')
        return redirect(url_for('routes.admin'))

    return render_template('editmarks.html', marks=marks_record)
#Delete Marks
@admin_or_faculty_login_required
@bp.route('/deletemarks', methods=['POST'])
def deletemarks():
    username = request.form['username']
    course_code = request.form['course_code']
    # Delete marks
    delete_marks(username, course_code)
    flash('Marks deleted successfully', 'success')
    return redirect(url_for('routes.admin'))
#Manage Marks

@bp.route('/managemarks',methods=['GET','POST'])
def managemarks():
    marks = get_all_marks()
    return render_template('viewmarks.html',marks=marks)
#Search by Username

@bp.route('/searchmarks_by_username',methods=['GET','POST'])
def searchmarks_by_username():
    if request.method == 'POST':
        username = request.form['username']
        new_marks = get_marks_by_username(username)
        if new_marks:
            return render_template('viewmarks.html',marks=new_marks)
        else:
            flash('No marks record for specified username','danger')
            return redirect(url_for('routes.managemarks'))
    return redirect(url_for('routes.managemarks'))
#Search by Course Code

@bp.route('/searchmarks_by_course',methods=['GET','POST'])
def searchmarks_by_coursecode():
    if request.method == 'POST':
        course_code = request.form['course_code']
        new_marks = get_marks_by_course(course_code)
        if new_marks:
            return render_template('viewmarks.html',marks=new_marks)
        else:
            flash('No marks record for specified course code','danger')
            return redirect(url_for('routes.managemarks'))
    return redirect(url_for('routes.managemarks'))
######################################################
#Add Attendance
@admin_or_faculty_login_required
@bp.route('/addattendance',methods=['GET','POST'])
def addattendance():
    if request.method == 'POST':
        username=request.form['username']
        course_code=request.form['course_code']
        attendance=request.form['attendance']
        date=request.form['date']
        add_attendance(username,course_code,attendance,date)
        flash('Attendance added successfully','success')
        return redirect(url_for('routes.admin'))
    students=get_all_students()
    courses=get_all_courses()
    return render_template('addattendance.html',students=students,courses=courses)

#Update Attendance
@admin_or_faculty_login_required
@bp.route('/editattendance/<string:username>/<string:course_code>',methods=['GET','POST'])
def editattendance(username,course_code):
    attendance_record = Attendance.query.filter_by(username=username, course_code=course_code).first()
    if not attendance_record:
        flash('Attendance record not found', 'danger')
        return redirect(url_for('routes.manageattendance'))

    if request.method == 'POST':
        attendance=request.form['attendance']
        date=request.form['date']
        
        # Update attendance
        update_attendance(username, course_code, attendance,date)
        flash('Attendance updated successfully', 'success')
        return redirect(url_for('routes.manageattendance'))

    return render_template('editattendance.html', attendance=attendance_record)
#Delete Attendance
@admin_or_faculty_login_required
@bp.route('/deleteattendance', methods=['POST'])
def deleteattendance():
    username = request.form['username']
    course_code = request.form['course_code']
    # Delete attendance
    delete_attendance(username, course_code)
    flash('Attendance deleted successfully', 'success')
    return redirect(url_for('routes.manageattendance'))
#Manage Marks
@bp.route('/manageattendance',methods=['GET','POST'])
def manageattendance():
    attendance_records = get_all_attendance()
    return render_template('viewattendance.html',attendance_records=attendance_records)
#Search by Username

@bp.route('/searchattendance_by_username',methods=['GET','POST'])
def searchattendance_by_username():
    if request.method == 'POST':
        username = request.form['username']
        new_attendance = get_attendance_by_username(username)
        if new_attendance:
            return render_template('viewattendance.html',attendance_records=new_attendance)
        else:
            flash('No attendance record for specified username','danger')
            return redirect(url_for('routes.manageattendance'))
    return redirect(url_for('routes.manageattendance'))
#Search by Course Code

@bp.route('/searchattendance_by_course',methods=['GET','POST'])
def searchattendance_by_coursecode():
    if request.method == 'POST':
        course_code = request.form['course_code']
        new_attendance = get_attendance_by_coursecode(course_code)
        if new_attendance:
            return render_template('viewattendance.html',attendance_records=new_attendance)
        else:
            flash('No attendance record for specified course code','danger')
            return redirect(url_for('routes.manageattendance'))
    return redirect(url_for('routes.manageattendance'))

#Association table for student course
#Add course
@admin_or_faculty_login_required
@bp.route('/add_course_to_student', methods=['GET', 'POST'])
def add_course_to_student():
    if request.method == 'POST':
        username = request.form['username']
        course_code = request.form['course_code']
        if addcourse_student(username, course_code):
            flash('Course added to student successfully', 'success')
        else:
            flash('Failed to add course to student', 'danger')
        return redirect(url_for('routes.admin'))
    
    students = Student.query.all()
    courses = Course.query.all()
    return render_template('addcourse_to_student.html', students=students, courses=courses)

#Get Course for Student
@bp.route('/student_courses/<string:username>', methods=['GET'])
def get_courses_for_student(username):
    courses = get_courses_for_student(username)
    if courses is None:
        flash('No courses found for the student', 'danger')
        return redirect(url_for('routes.manage_student_course'))
    return render_template('student_courses.html', courses=courses, username=username)
#Get students for Course
@bp.route('/course_students/<string:course_code>', methods=['GET'])

def get_students_for_course(course_code):
    students = get_students_for_course(course_code)
    if students is None:
        flash('No students found for the course', 'danger')
        return redirect(url_for('routes.manage_student_course'))
    return render_template('course_students.html', students=students, course_code=course_code)
#Remove Course from Student
@bp.route('/remove_course_from_student', methods=['POST'])
@admin_or_faculty_login_required
def remove_course_from_student():
    username = request.form['username']
    course_code = request.form['course_code']
    if remove_course_from_student(username, course_code):
        flash('Course removed from student successfully', 'success')
    else:
        flash('Failed to remove course from student', 'danger')
    return redirect(url_for('routes.admin'))



@bp.route('/manage_student_course')
@admin_or_faculty_login_required
def manage_student_course():
    # Retrieve all students and their associated courses
    students = Student.query.all()  # Retrieve all students
    student_courses = []
    
    for student in students:
        for course in student.courses:
            student_courses.append({
                'username': student.username,
                'full_name': student.full_name,
                'course_code': course.course_code,
                'course_name': course.course_name
            })
    
    return render_template('viewstudent-courses.html', student_courses=student_courses)

#################################################
#Notification
@bp.route('/admin/notify_staff', methods=['GET', 'POST'])
@admin_login_required
def notify_staff():
    if request.method == 'POST':
        message = request.form['message']
        date = request.form['date']
        notify_all = 'notify_all' in request.form
        
        if notify_all:
            staff_members = Faculty.query.all()
            for staff in staff_members:
                notification = NotificationFaculty(recipient_username=staff.faculty_code, message=message, date=date)
                db.session.add(notification)
        else:
            recipient_username = request.form['recipient_username']
            notification = NotificationFaculty(recipient_username=recipient_username, message=message, date=date)
            db.session.add(notification)
        
        db.session.commit()
        flash("Notification sent successfully", "success")
        return redirect(url_for('routes.notify_staff'))
    
    staff_members = Faculty.query.all()
    return render_template('notify_staff.html', staff_members=staff_members)

@bp.route('/notify_students', methods=['GET', 'POST'])
@admin_login_required
def notify_students():
    if request.method == 'POST':
        message = request.form['message']
        date = request.form['date']
        notify_all = 'notify_all' in request.form
        
        if notify_all:
            students = Student.query.all()
            for student in students:
                notification = NotificationStudent(recipient_username=student.username, message=message, date=date)
                db.session.add(notification)
        else:
            recipient_username = request.form['recipient_username']
            notification = NotificationStudent(recipient_username=recipient_username, message=message, date=date)
            db.session.add(notification)
        
        db.session.commit()
        flash("Notification sent successfully", "success")
        return redirect(url_for('routes.notify_students'))
    
    students = Student.query.all()
    return render_template('notify_students.html', students=students)