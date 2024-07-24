import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'pranav'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://school_k16a_user:6kn90FWVuX5yv8rLfZpf4RtWA6Nv4CxS@dpg-cqfvftt6l47c73bmq9gg-a:5432/school_k16a'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
