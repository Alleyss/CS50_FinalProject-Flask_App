from app import db
from werkzeug.security import generate_password_hash, check_password_hash

# Association table for many-to-many relationship between Student and Course
student_courses = db.Table('student_courses',
    db.Column('username', db.String(20), db.ForeignKey('studentTable.username'), primary_key=True),
    db.Column('course_code', db.String(20), db.ForeignKey('courseTable.course_code'), primary_key=True)
)

class Student(db.Model):
    __tablename__ = 'studentTable'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False,primary_key=True)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    username = db.Column(db.String(20), primary_key=True,nullable=False)
    full_name = db.Column(db.String(100), nullable=False)
    mobile_number = db.Column(db.String(15), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    year_of_joining = db.Column(db.Integer, nullable=False)
    branch_code = db.Column(db.String(10), db.ForeignKey('branchTable.branch_code'), nullable=False)
    current_semester = db.Column(db.Integer, nullable=True)
    cgpa = db.Column(db.Float, nullable=True)

class Attendance(db.Model):
    __tablename__ = 'attendanceTable'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), db.ForeignKey('studentTable.username'), nullable=False,primary_key=True)
    course_code = db.Column(db.String(20), db.ForeignKey('coursesTable.course_code'), primary_key=True,nullable=False)
    attendance = db.Column(db.String(20))
    date = db.Column(db.Date,nullable = True)

class Marks(db.Model):
    __tablename__ = 'marksTable'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), db.ForeignKey('studentTable.username'), nullable=False,primary_key=True)
    course_code = db.Column(db.String(20), db.ForeignKey('courseTable.course_code'), nullable=False)
    ExamType = db.Column(db.String(50),nullable=False)
    marks_obtained = db.Column(db.Float, nullable=False)
    max_marks = db.Column(db.Float, nullable=False)


class Branch(db.Model):
    __tablename__ = 'branchTable'
    id=db.Column(db.Integer,primary_key=True)
    branch_code = db.Column(db.String(10), primary_key=True, unique=True)
    branch_name = db.Column(db.String(100), nullable=False)

class Admin(db.Model):
    __tablename__ = 'adminTable'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100),primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

class Course(db.Model):
    __tablename__ = 'courseTable'
    id = db.Column(db.Integer, primary_key=True)
    course_code = db.Column(db.String(20), primary_key=True)
    course_name = db.Column(db.String(100), nullable=False)
    credits = db.Column(db.Integer, nullable=False)
    course_instructor_code = db.Column(db.String(100),db.ForeignKey('facultyTable.faculty_code'), nullable=False)
    branch_code = db.Column(db.String(10),db.ForeignKey('branchTable.branch_code'),nullable=False)

class Faculty(db.Model):
    __tablename__ = 'facultyTable'
    id = db.Column(db.Integer, primary_key=True)
    faculty_code=db.Column(db.String(10),primary_key=True)
    full_name = db.Column(db.String(100), nullable=False,)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    cabin_number = db.Column(db.String(20), nullable=True)
    specialization = db.Column(db.String(100), nullable=False)
