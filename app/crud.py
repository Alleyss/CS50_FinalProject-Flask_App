from app import db
from app.models import Student

def add_student(name, mobile_number, address, email, password):
    new_student = Student(name=name, mobile_number=mobile_number, address=address, email=email, password=password)
    db.session.add(new_student)
    db.session.commit()

def get_all_students():
    return Student.query.all()

def get_student_by_id(student_id):
    return Student.query.get(student_id)

def update_student(student_id, **kwargs):
    student = Student.query.get(student_id)
    if student:
        for key, value in kwargs.items():
            setattr(student, key, value)
        db.session.commit()
    return student

def delete_student(student_id):
    student = Student.query.get(student_id)
    if student:
        db.session.delete(student)
        db.session.commit()
    return student
