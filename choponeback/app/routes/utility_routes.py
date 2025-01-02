from flask import Blueprint, request, current_app, send_file
from app.utils.response_utils import create_response

utility_bp = Blueprint('utility', __name__)

@utility_bp.route('/api/utility/upload', methods=['POST'])
def upload_file():
    try:
        if 'file' not in request.files:
            return create_response(False, "No file provided"), 400
            
        file = request.files['file']
        if file.filename == '':
            return create_response(False, "No file selected"), 400
            
        # 获取允许的文件类型（如果在请求中指定）
        allowed_extensions = set(request.form.get('allowed_extensions', '').split(','))
        if not allowed_extensions:
            allowed_extensions = None
            
        # 使用存储服务上传文件
        success, message, filepath = current_app.storage_service.upload_file(file, allowed_extensions)
        
        if not success:
            return create_response(False, message), 400
            
        return create_response(True, message, {
            'filepath': filepath,
            'filename': file.filename
        })
        
    except Exception as e:
        return create_response(False, str(e)), 500

@utility_bp.route('/api/utility/download/<path:filename>', methods=['GET'])
def download_file(filename):
    try:
        # 构建文件路径
        filepath = f"{current_app.config['DOWNLOAD_FOLDER']}/{filename}"
        
        # 使用存储服务检查文件
        success, message, file_path = current_app.storage_service.download_file(filepath)
        
        if not success:
            return create_response(False, message), 404
            
        return send_file(file_path, as_attachment=True)
        
    except Exception as e:
        return create_response(False, str(e)), 500 