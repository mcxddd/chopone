from flask import Blueprint, send_file, current_app
from app.models.pdf_dto import ApiResponse
import os
from dataclasses import asdict

download_bp = Blueprint('download', __name__)

@download_bp.route('/api/download/<path:filename>', methods=['GET'])
def download_file(filename):
    try:
        # 构建文件路径（从下载目录）
        file_path = os.path.join(current_app.config['DOWNLOAD_FOLDER'], filename)
        
        # 检查文件是否存在
        if not os.path.exists(file_path):
            return asdict(ApiResponse(False, "File not found")), 404
            
        return send_file(file_path, as_attachment=True)
    except Exception as e:
        return asdict(ApiResponse(False, str(e))), 500 