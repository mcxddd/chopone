import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key-here'
    UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER', '/app/data/uploads')
    DOWNLOAD_FOLDER = os.environ.get('DOWNLOAD_FOLDER', '/app/data/downloads')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size 