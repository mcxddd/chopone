from flask import Blueprint, request, current_app
from app.services.pdf_service import PdfService
from app.models.pdf_dto import CompressionLevel, ApiResponse
import os
from dataclasses import asdict
from urllib.parse import quote

utility_bp = Blueprint('utility', __name__)
pdf_service = PdfService()

@utility_bp.route('/api/utility/compress-pdf', methods=['POST'])
def compress_pdf_route():
    try:
        # 验证请求
        if 'file' not in request.files:
            return asdict(ApiResponse(False, "No file provided")), 400
        
        file = request.files['file']
        if file.filename == '':
            return asdict(ApiResponse(False, "No file selected")), 400
            
        if not file.filename.lower().endswith('.pdf'):
            return asdict(ApiResponse(False, "File must be a PDF")), 400
        
        # 获取压缩级别
        compression_level_str = request.form.get('compression_level', 'MEDIUM').upper()
        try:
            compression_level = CompressionLevel[compression_level_str]
        except KeyError:
            return asdict(ApiResponse(False, "Invalid compression level")), 400
        
        # 执行压缩
        result = pdf_service.compress_pdf(file, compression_level)
        
        # URL编码文件名，确保中文正确显示
        filename = os.path.basename(result.file_path)
        encoded_filename = quote(filename)
        result_dict = asdict(result)
        result_dict['file_path'] = f"/api/download/{encoded_filename}"
        
        return asdict(ApiResponse(True, "PDF compressed successfully", result_dict))
        
    except Exception as e:
        return asdict(ApiResponse(False, str(e))), 500 