from flask import Flask, current_app
from flask_cors import CORS
from config.config import Config
import os
from app.services.storage_service import StorageService

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Enable CORS
    CORS(app)
    
    # 配置上传和下载目录
    app.config['UPLOAD_FOLDER'] = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'uploads')
    app.config['DOWNLOAD_FOLDER'] = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'downloads')
    
    # 初始化存储服务
    storage_service = StorageService()
    app.storage_service = storage_service  # 将存储服务添加到 app 实例
    
    # 确保目录存在
    storage_service.ensure_directory(app.config['UPLOAD_FOLDER'])
    storage_service.ensure_directory(app.config['DOWNLOAD_FOLDER'])
    
    # 启动清理任务
    with app.app_context():
        storage_service.start_cleanup_task()
    
    # Register blueprints
    from app.routes.utility_routes import utility_bp
    from app.routes.system_routes import system_bp
    from app.routes.download_routes import download_bp
    
    app.register_blueprint(utility_bp)
    app.register_blueprint(system_bp)
    app.register_blueprint(download_bp)
    
    return app 