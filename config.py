import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'pranav'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://postgres:vsp2004@localhost:5432/student_portal_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
