from flask import Flask, current_app
from flask_cors import CORS
from config.config import Config
import os
import secrets
from datetime import timedelta
from app.services.storage_service import StorageService

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # 生成随机的 secret key
    app.secret_key = secrets.token_hex(32)
    
    # 配置 session
    app.config.update(
        PERMANENT_SESSION_LIFETIME=timedelta(hours=12),  # 12小时后过期
        SESSION_PERMANENT=True  # 启用永久 session
    )
    
    # 启用 CORS，允许跨域请求携带 Cookie
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
    from app.routes.ai_routes import ai_bp
    
    app.register_blueprint(utility_bp)
    app.register_blueprint(system_bp)
    app.register_blueprint(ai_bp)
    
    return app 