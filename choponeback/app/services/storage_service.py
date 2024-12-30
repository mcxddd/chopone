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
    _app = None
    
    def __new__(cls) -> 'StorageService':
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super().__new__(cls)
                    cls._instance.cleanup_thread = None
        return cls._instance
    
    def __init__(self):
        """初始化存储服务"""
        # __new__ 已经处理了单例逻辑，这里不需要重复初始化
        pass
    
    def init_app(self, app):
        """初始化应用实例"""
        self._app = app
    
    def start_cleanup_task(self):
        """启动清理任务"""
        if not self.cleanup_thread or not self.cleanup_thread.is_alive():
            self.cleanup_thread = threading.Thread(target=self._cleanup_task, daemon=True)
            self.cleanup_thread.start()
    
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
                    print(f"Removed expired file: {file_path}")
                except Exception as e:
                    print(f"Error removing file {file_path}: {str(e)}")
    
    def _cleanup_task(self) -> None:
        """清理任务的主循环"""
        while True:
            try:
                with self._app.app_context():
                    folders = [
                        current_app.config['UPLOAD_FOLDER'],
                        current_app.config['DOWNLOAD_FOLDER']
                    ]
                    for folder in folders:
                        self._cleanup_expired_files(folder)
            except Exception as e:
                print(f"Error in cleanup task: {str(e)}")
            time.sleep(3600)  # 每小时执行一次 