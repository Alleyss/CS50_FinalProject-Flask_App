import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'pranav'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://schooldb_khj2_user:VwFQq2QYRRPuadc55Vvam1mWWGohRaCj@dpg-crdg5qd2ng1s73fuirkg-a.oregon-postgres.render.com/schooldb_khj2'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
