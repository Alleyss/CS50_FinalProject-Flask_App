import re
from app import db
from app.models import Student, Attendance, Marks, Course, Branch, Faculty

# Student CRUD
def add_student(username, email, password, full_name, mobile_number, address, year_of_joining, branch_code, current_semester, cgpa):
    new_student_details = Student(username=username, email=email, full_name=full_name, mobile_number=mobile_number, address=address, year_of_joining=year_of_joining, branch_code=branch_code, current_semester=current_semester, cgpa=cgpa)
    new_student_details.set_password(password)
    db.session.add(new_student_details)
    db.session.commit()
#For manage students option
def get_all_students():
    return Student.query.all()
#For search box
def get_student_by_id(username):
    student_details = Student.query.filter_by(username=username).first()
    return student_details
#For Login edit
def update_student_login(username,password):
    student_login=get_student_by_id(username)
    if student_login:
        student_login.set_password(password)
        db.session.commit()
    return student_login
#For edit icon
def update_student(username,email,full_name,mobile_number,address,year_of_joining,branch_code,current_semester,cgpa):
    student_details = Student.query.filter_by(username=username).first()
    if student_details:
        student_details.email=email
        student_details.full_name=full_name
        student_details.mobile_number=mobile_number
        student_details.address=address
        student_details.year_of_joining=year_of_joining
        student_details.branch_code=branch_code
        student_details.current_semester=current_semester
        student_details.cgpa=cgpa
        db.session.commit()
    return student_details

#For delete icon
def delete_student(username):
    student = Student.query.filter_by(username=username).first()
    if student:
        db.session.delete(student)
    db.session.commit()
    return student

#################################################################
#Course CRUD
#Add course option
def add_course(course_code, course_name, credits, course_instructor_code,branch_code):
    new_course = Course(course_code=course_code, course_name=course_name, credits=credits, course_instructor_code=course_instructor_code, branch_code = branch_code)
    db.session.add(new_course)
    db.session.commit()
#Edit button
def update_course(course_code,course_name,credits,course_instructor_code,branch_code):
    course = Course.query.get(course_code)
    if course:
        course.course_name=course_name
        course.credits=credits
        course.course_instructor_code=course_instructor_code
        course.branch_code=branch_code
        db.session.commit()
    return course
#Delete button
def delete_course(course_code):
    course = Course.query.get(course_code)
    if course:
        db.session.delete(course)
        db.session.commit()
    return course
#Search Button
def get_course_by_id(course_code):
    course = Course.query.get(course_code)
    return course
#Manage Courses View
def get_all_courses():
    return Course.query.all()
####################################################
#Faculties CRUD
#Add Faculty Option
def add_faculty(faculty_code,full_name, email, password, cabin_number, specialization):
    new_faculty = Faculty(faculty_code=faculty_code,full_name=full_name, email=email, cabin_number=cabin_number, specialization=specialization)
    new_faculty.set_password(password)
    db.session.add(new_faculty)
    db.session.commit()
#Edit Icon
def update_faculty(faculty_code, name, email, password, cabin_number, specialization):
    faculty = Faculty.query.get(faculty_code)
    if faculty:
        faculty.name = name
        faculty.email = email
        faculty.set_password(password)
        faculty.cabin_number = cabin_number
        faculty.specialization = specialization
        db.session.commit()
    return faculty
#Delete Icon
def delete_faculty(faculty_code):
    faculty = Faculty.query.get(faculty_code)
    if faculty:
        db.session.delete(faculty)
        db.session.commit()
    return faculty
#Search Option
def get_faculty_by_id(faculty_code):
    faculty = Faculty.query.get(faculty_code)
    if faculty:
        return faculty
#Manage Faculty Option
def get_all_faculty():
    return Faculty.query.all()
######################################################
#Marks CRUD
#Add Option
def add_marks(username, course_code, ExamType,marks_obtained,max_marks):
    new_marks = Marks(username=username, course_code=course_code, ExamType=ExamType,marks_obtained=marks_obtained,max_marks=max_marks)
    db.session.add(new_marks)
    db.session.commit()
#Edit icon
def update_marks(username, course_code, ExamType, marks_obtained, max_marks):
    marks_record = Marks.query.filter_by(username=username, course_code=course_code).first()
    if marks_record:
        marks_record.ExamType=ExamType
        marks_record.marks_obtained = marks_obtained
        marks_record.max_marks = max_marks
        db.session.commit()
    return marks_record
#Delete icon
def delete_marks(username, course_code):
    marks_record = Marks.query.filter_by(username=username, course_code=course_code).first()
    if marks_record:
        db.session.delete(marks_record)
        db.session.commit()
    return marks_record
#Search Marks for particular Student
def get_marks_by_username(username):
    marks_record = Marks.query.get(username)
    if marks_record:
        return marks_record
#manage option with course_code input
def get_marks_by_course(course_code):
    marks_record = Marks.query.get(course_code)
    if marks_record:
        return marks_record

def get_all_marks():
    return Marks.query.get.all()
##################################################
# Attendance CRUD Operations
#Add Option
def add_attendance(username, course_code, attendance,date):
    new_attendance = Attendance(username=username, course_code=course_code, attendance=attendance,date=date)
    db.session.add(new_attendance)
    db.session.commit()
#Edit Icon
def update_attendance(username, course_code, attendance,date):
    attendance_record = Attendance.query.filter_by(username=username, course_code=course_code).first()
    if attendance_record:
        attendance_record.attendance = attendance
        attendance_record.date = date
        db.session.commit()
    return attendance_record
#Delete Icon
def delete_attendance(username, course_code):
    attendance_record = Attendance.query.filter_by(username=username, course_code=course_code).first()
    if attendance_record:
        db.session.delete(attendance_record)
        db.session.commit()
    return attendance_record
#Search for User
def get_attendance_by_username(username):
    return Attendance.query.get(username)
#Manage Attendance option with input
def get_attendance_by_coursecode(course_code):
    return Attendance.query.get(course_code)

def get_all_attendance():
    return Attendance.query.get.all()
####################################################
# Branch CRUD Operations
#Add Option
def add_branch(branch_code, branch_name):
    new_branch = Branch(branch_code=branch_code, branch_name=branch_name)
    db.session.add(new_branch)
    db.session.commit()
#Search Option
def get_branch_by_id(branch_code):
    return Branch.query.get(branch_code)
#Edit icon
def update_branch(branch_code, branch_name):
    branch = Branch.query.get(branch_code)
    if branch:
        branch.branch_name = branch_name
        db.session.commit()
    return branch
#Delete Icon
def delete_branch(branch_code):
    branch = Branch.query.get(branch_code)
    if branch:
        db.session.delete(branch)
        db.session.commit()
    return branch
#Manage Option
def get_all_branches():
    return Branch.query.all()
#Association Table CRUD
#CRUD Add a course to student
def add_course_to_student(username, course_code):
    student = get_student_by_id(username)
    course = get_course_by_id(course_code)
    if student and course and course not in student.courses:
        student.courses.append(course)
        db.session.commit()
        return True
    return False
#CRUD R retrieve all courses of student
def get_courses_for_student(username):
    student = get_student_by_id(username)
    if student:
        return student.courses
    return None
#CRUD R retrieve all students of course
def get_students_for_course(course_code):
    course = get_course_by_id(course_code)
    if course:
        return course.students
    return None
#CRUD Remove a course to student
def remove_course_from_student(username, course_code):
    student = get_student_by_id(username)
    course = get_course_by_id(course_code)
    if student and course and course in student.courses:
        student.courses.remove(course)
        db.session.commit()
        return True
    return False
