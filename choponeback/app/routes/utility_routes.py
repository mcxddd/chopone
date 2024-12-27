from flask import Blueprint, request, jsonify
from app.services.pdf_service import compress_pdf, CompressionLevel
from app.utils.response_utils import create_response
import os

utility_bp = Blueprint('utility', __name__)

@utility_bp.route('/api/utility/compress-pdf', methods=['POST'])
def compress_pdf_route():
    try:
        if 'file' not in request.files:
            return create_response(False, "No file provided", None), 400
        
        file = request.files['file']
        if file.filename == '':
            return create_response(False, "No file selected", None), 400
            
        if not file.filename.endswith('.pdf'):
            return create_response(False, "File must be a PDF", None), 400
        
        # Get compression level from request
        compression_level_str = request.form.get('compression_level', 'MEDIUM').upper()
        try:
            compression_level = CompressionLevel[compression_level_str]
        except KeyError:
            return create_response(False, "Invalid compression level. Must be one of: VERY_LOW, LOW, MEDIUM, HIGH, VERY_HIGH", None), 400
        
        result = compress_pdf(file, compression_level)
        
        return create_response(True, "PDF compressed successfully", result)
        
    except Exception as e:
        return create_response(False, str(e), None), 500 