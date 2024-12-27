import os
import time
from datetime import datetime, timedelta
from flask import current_app
import threading

def is_file_expired(file_path, hours=24):
    """Check if a file is older than specified hours"""
    if not os.path.exists(file_path):
        return False
    
    file_time = os.path.getmtime(file_path)
    file_datetime = datetime.fromtimestamp(file_time)
    return datetime.now() - file_datetime > timedelta(hours=hours)

def delete_expired_files(folder):
    """Delete expired files from a specific folder"""
    if not os.path.exists(folder):
        return
        
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        if is_file_expired(file_path):
            try:
                os.remove(file_path)
                print(f"Removed expired file: {file_path}")
            except Exception as e:
                print(f"Error removing file {file_path}: {str(e)}")

def cleanup_files():
    """Clean up files older than 24 hours in both upload and download folders"""
    while True:
        try:
            folders = [
                current_app.config['UPLOAD_FOLDER'],
                current_app.config['DOWNLOAD_FOLDER']
            ]
            for folder in folders:
                delete_expired_files(folder)
        except Exception as e:
            print(f"Error in cleanup task: {str(e)}")
        time.sleep(3600)

def start_cleanup_task():
    """Start the cleanup task in a background thread"""
    cleanup_thread = threading.Thread(target=cleanup_files, daemon=True)
    cleanup_thread.start() 