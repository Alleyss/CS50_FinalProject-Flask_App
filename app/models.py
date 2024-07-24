from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

# Association table for many-to-many relationship between Student and Course
student_courses = db.Table('student_courses',
    db.Column('username', db.String(20), db.ForeignKey('studentTable.username'), primary_key=True),
    db.Column('course_code', db.String(20), db.ForeignKey('courseTable.course_code'), primary_key=True)
)

class Student(db.Model):
    __tablename__ = 'studentTable'
    
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    username = db.Column(db.String(20), unique=True,nullable=False,primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    mobile_number = db.Column(db.String(15), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    year_of_joining = db.Column(db.Integer, nullable=False)
    branch_code = db.Column(db.String(10), db.ForeignKey('branchTable.branch_code'), nullable=False)
    current_semester = db.Column(db.Integer, nullable=True)
    cgpa = db.Column(db.Float, nullable=True)
    courses = db.relationship('Course', secondary=student_courses, back_populates='students')
class Attendance(db.Model):
    __tablename__ = 'attendanceTable'
    
    username = db.Column(db.String(20), db.ForeignKey('studentTable.username'), nullable=False,primary_key=True)
    course_code = db.Column(db.String(20), db.ForeignKey('courseTable.course_code'),nullable=False,primary_key=True)
    attendance = db.Column(db.String(20))
    date = db.Column(db.Date,nullable = True,primary_key=True)

class Marks(db.Model):
    __tablename__ = 'marksTable'
    
    username = db.Column(db.String(20), db.ForeignKey('studentTable.username'), nullable=False,primary_key=True)
    course_code = db.Column(db.String(20), db.ForeignKey('courseTable.course_code'), nullable=False,primary_key=True)
    ExamType = db.Column(db.String(50),nullable=False,primary_key=True)
    marks_obtained = db.Column(db.Float, nullable=False)
    max_marks = db.Column(db.Float, nullable=False)


class Branch(db.Model):
    __tablename__ = 'branchTable'
    
    branch_code = db.Column(db.String(10),  unique=True,primary_key=True)
    branch_name = db.Column(db.String(100), nullable=False)

class Admin(db.Model):
    __tablename__ = 'adminTable'

    username = db.Column(db.String(100),unique=True,primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

class Course(db.Model):
    __tablename__ = 'courseTable'
    
    course_code = db.Column(db.String(20),unique=True,primary_key=True)
    course_name = db.Column(db.String(100), nullable=False)
    credits = db.Column(db.Integer, nullable=False)
    course_instructor_code = db.Column(db.String(100),db.ForeignKey('facultyTable.faculty_code'), nullable=False)
    branch_code = db.Column(db.String(10),db.ForeignKey('branchTable.branch_code'),nullable=False)
    students = db.relationship('Student', secondary='student_courses', back_populates='courses')
class Faculty(db.Model):
    __tablename__ = 'facultyTable'
    
    faculty_code=db.Column(db.String(10),unique=True,primary_key=True)
    full_name = db.Column(db.String(100), nullable=False,)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    cabin_number = db.Column(db.String(20), nullable=True)
    specialization = db.Column(db.String(100), nullable=False)

class NotificationStudent(db.Model):
    __tablename__ = 'notificationStudentTable'
    
    id = db.Column(db.Integer, primary_key=True)
    recipient_username = db.Column(db.String(20), db.ForeignKey('studentTable.username'), nullable=False)
    message = db.Column(db.Text, nullable=False)
    date = db.Column(db.Date, nullable=False, default=datetime.utcnow)

class NotificationFaculty(db.Model):
    __tablename__ = 'notificationFacultyTable'
    
    id = db.Column(db.Integer, primary_key=True)
    recipient_username = db.Column(db.String(20), db.ForeignKey('facultyTable.faculty_code'), nullable=False)
    message = db.Column(db.Text, nullable=False)
    date = db.Column(db.Date, nullable=False, default=datetime.utcnow)