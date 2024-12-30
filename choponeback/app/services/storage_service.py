import os
import time
import threading
from datetime import datetime, timedelta
from werkzeug.utils import secure_filename
from flask import current_app
from typing import BinaryIO, Optional

class StorageService:
    """文件存储服务，处理文件的存储、获取、清理和维护"""
    
    _instance: Optional['StorageService'] = None
    _lock = threading.Lock()
    _cleanup_thread = None
    _stop_cleanup = False
    
    def __new__(cls) -> 'StorageService':
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        """初始化存储服务"""
        pass

    def init_app(self, app):
        """初始化应用实例"""
        if not hasattr(app, 'extensions'):
            app.extensions = {}
        app.extensions['storage_service'] = self

        # 注册清理任务
        def cleanup_files():
            """定期清理文件的后台任务"""
            with app.app_context():
                while not self._stop_cleanup:
                    try:
                        folders = [
                            app.config['UPLOAD_FOLDER'],
                            app.config['DOWNLOAD_FOLDER']
                        ]
                        for folder in folders:
                            self._cleanup_expired_files(folder)
                    except Exception as e:
                        app.logger.error(f"Error in cleanup task: {str(e)}")
                    time.sleep(3600)  # 每小时执行一次

        if not self._cleanup_thread or not self._cleanup_thread.is_alive():
            self._stop_cleanup = False
            self._cleanup_thread = threading.Thread(target=cleanup_files, daemon=True)
            self._cleanup_thread.start()
    
    def save_file(self, file, filename: str, directory: str) -> str:
        """
        保存文件到指定目录
        Args:
            file: 文件对象
            filename: 文件名
            directory: 目标目录
        Returns:
            str: 保存后的文件路径
        """
        if not os.path.exists(directory):
            os.makedirs(directory)
            
        # 确保文件名是字符串类型
        if not isinstance(filename, str):
            filename = str(filename)
            
        # 构建完整的文件路径
        filepath = os.path.join(directory, filename)
        
        # 保存文件
        file.save(filepath)
        
        return filepath
    
    @staticmethod
    def delete_file(file_path: str) -> bool:
        """
        删除文件
        Args:
            file_path: 文件路径
        Returns:
            是否成功删除
        """
        try:
            if os.path.exists(file_path):
                os.remove(file_path)
                return True
            return False
        except Exception:
            return False
    
    @staticmethod
    def get_file_size(file_path: str) -> int:
        """
        获取文件大小
        Args:
            file_path: 文件路径
        Returns:
            文件大小（字节）
        """
        return os.path.getsize(file_path)
    
    @staticmethod
    def ensure_directory(directory: str) -> None:
        """
        确保目录存在
        Args:
            directory: 目录路径
        """
        os.makedirs(directory, exist_ok=True)
    
    @staticmethod
    def is_file_expired(file_path: str, hours: int = 24) -> bool:
        """
        检查文件是否过期
        Args:
            file_path: 文件路径
            hours: 过期时间（小时）
        Returns:
            是否过期
        """
        if not os.path.exists(file_path):
            return False
        
        file_time = os.path.getmtime(file_path)
        file_datetime = datetime.fromtimestamp(file_time)
        return datetime.now() - file_datetime > timedelta(hours=hours)
    
    def _cleanup_expired_files(self, folder: str) -> None:
        """
        清理指定文件夹中的过期文件
        Args:
            folder: 文件夹路径
        """
        if not os.path.exists(folder):
            return
            
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            if self.is_file_expired(file_path):
                try:
                    self.delete_file(file_path)
                    current_app.logger.info(f"Removed expired file: {file_path}")
                except Exception as e:
                    current_app.logger.error(f"Error removing file {file_path}: {str(e)}")

    def stop_cleanup(self):
        """停止清理任务"""
        self._stop_cleanup = True
        if self._cleanup_thread and self._cleanup_thread.is_alive():
            self._cleanup_thread.join(timeout=1) 