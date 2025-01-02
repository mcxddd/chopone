import os
import time
import threading
from datetime import datetime, timedelta
from werkzeug.utils import secure_filename
from flask import current_app, send_file
from typing import BinaryIO, Optional, Tuple

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
    
    def upload_file(self, file: BinaryIO, allowed_extensions: set = None) -> Tuple[bool, str, str]:
        """
        上传文件
        Args:
            file: 文件对象
            allowed_extensions: 允许的文件扩展名集合
        Returns:
            (成功标志, 消息, 文件路径)
        """
        try:
            if not file:
                return False, "No file provided", ""
                
            if not hasattr(file, 'filename') or not file.filename:
                return False, "Invalid file object", ""
                
            filename = secure_filename(file.filename)
            if not filename:
                return False, "Invalid filename", ""
                
            # 检查文件扩展名
            if allowed_extensions:
                ext = os.path.splitext(filename)[1].lower()[1:]
                if ext not in allowed_extensions:
                    return False, f"File type not allowed. Allowed types: {', '.join(allowed_extensions)}", ""
            
            try:
                # 保存文件
                filepath = self.save_file(file, filename, current_app.config['UPLOAD_FOLDER'])
                return True, "File uploaded successfully", filepath
            except OSError as e:
                return False, f"Failed to save file: {str(e)}", ""
            except Exception as e:
                return False, f"Unexpected error while saving file: {str(e)}", ""
            
        except Exception as e:
            return False, f"Upload failed: {str(e)}", ""
    
    def download_file(self, filename: str) -> Tuple[bool, str, Optional[str]]:
        """
        下载文件
        Args:
            filename: 文件名
        Returns:
            (成功标志, 消息, 文件路径或None)
        """
        try:
            if not filename:
                return False, "No filename provided", None
                
            # 构建完整路径
            filepath = os.path.join(current_app.config['DOWNLOAD_FOLDER'], filename)
            
            if not os.path.exists(filepath):
                return False, "File not found", None
                
            if not os.path.isfile(filepath):
                return False, "Path exists but is not a file", None
                
            try:
                # 检查文件是否可读
                with open(filepath, 'rb'):
                    pass
            except IOError:
                return False, "File exists but is not accessible", None
                
            return True, "File ready for download", filepath
            
        except Exception as e:
            return False, f"Download failed: {str(e)}", None
    
    def save_file(self, file: BinaryIO, filename: str, directory: str) -> str:
        """
        保存文件到指定目录
        Args:
            file: 文件对象
            filename: 文件名
            directory: 目标目录
        Returns:
            str: 保存后的文件路径
        Raises:
            OSError: 当创建目录或保存文件失败时
        """
        if not os.path.exists(directory):
            os.makedirs(directory)
            
        if not isinstance(filename, str):
            filename = str(filename)
            
        filepath = os.path.join(directory, filename)
        
        # 如果文件已存在，先删除
        if os.path.exists(filepath):
            os.remove(filepath)
            
        file.save(filepath)
        return filepath
    
    @staticmethod
    def delete_file(file_path: str) -> bool:
        """删除文件"""
        try:
            if os.path.exists(file_path):
                os.remove(file_path)
                return True
            return False
        except Exception:
            return False
    
    @staticmethod
    def get_file_size(file_path: str) -> int:
        """获取文件大小"""
        return os.path.getsize(file_path)
    
    @staticmethod
    def ensure_directory(directory: str) -> None:
        """确保目录存在"""
        os.makedirs(directory, exist_ok=True)
    
    @staticmethod
    def is_file_expired(file_path: str, hours: int = 24) -> bool:
        """检查文件是否过期"""
        if not os.path.exists(file_path):
            return False
        
        file_time = os.path.getmtime(file_path)
        file_datetime = datetime.fromtimestamp(file_time)
        return datetime.now() - file_datetime > timedelta(hours=hours)
    
    def _cleanup_expired_files(self, folder: str) -> None:
        """清理指定文件夹中的过期文件"""
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