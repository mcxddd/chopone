from flask import Flask
from flask_cors import CORS
from config.config import Config
import os
from app.utils.cleanup_utils import start_cleanup_task

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Enable CORS
    CORS(app)
    
    # Ensure upload and download directories exist
    for folder in [app.config['UPLOAD_FOLDER'], app.config['DOWNLOAD_FOLDER']]:
        if not os.path.exists(folder):
            os.makedirs(folder)
    
    # Start the cleanup task
    with app.app_context():
        start_cleanup_task()
    
    # Register blueprints
    from app.routes.utility_routes import utility_bp
    from app.routes.system_routes import system_bp
    
    app.register_blueprint(utility_bp)
    app.register_blueprint(system_bp)
    
    return app 