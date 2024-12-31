import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

class Config:
    # 获取项目根目录路径
    BASE_DIR = Path(__file__).parent.parent.parent
    
    # 密钥配置
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key-here'
    
    # 文件存储路径配置
    # Docker环境下使用 /app/data，本地开发使用项目根目录下的 data
    DATA_DIR = os.environ.get('DATA_DIR') or os.path.join(BASE_DIR, 'data')
    UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER') or os.path.join(DATA_DIR, 'uploads')
    DOWNLOAD_FOLDER = os.environ.get('DOWNLOAD_FOLDER') or os.path.join(DATA_DIR, 'downloads')
    
    # 文件大小限制：16MB
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size 