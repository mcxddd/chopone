from flask import Flask, current_app
from flask_cors import CORS
from config.config import Config
import os
from app.services.storage_service import StorageService

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # 设置 session secret key
    app.secret_key = os.getenv('SECRET_KEY', 'dev-secret-key')
    
    # Enable CORS with support for credentials
    CORS(app, supports_credentials=True)
    
    # 初始化存储服务
    storage_service = StorageService()
    storage_service.init_app(app)
    app.storage_service = storage_service
    
    # 确保数据目录存在
    os.makedirs(app.config['DATA_DIR'], exist_ok=True)
    storage_service.ensure_directory(app.config['UPLOAD_FOLDER'])
    storage_service.ensure_directory(app.config['DOWNLOAD_FOLDER'])
    
    # Register blueprints
    from app.routes.utility_routes import utility_bp
    from app.routes.system_routes import system_bp
    from app.routes.download_routes import download_bp
    from app.routes.ai_routes import ai_bp
    
    app.register_blueprint(utility_bp)
    app.register_blueprint(system_bp)
    app.register_blueprint(download_bp)
    app.register_blueprint(ai_bp)
    
    return app 