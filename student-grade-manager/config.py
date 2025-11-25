import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key-here'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://user:password@localhost/dbname'  # Railway sẽ cung cấp DATABASE_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False