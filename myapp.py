from app import create_app, db
from app.models import Student,Attendance, Marks, Course, Faculty, Branch,Admin

app = create_app()

#if __name__ == '__main__':
#    app.run(debug=True)
