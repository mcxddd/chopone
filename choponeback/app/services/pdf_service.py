import os
import time
from typing import Tuple
from PyPDF2 import PdfReader, PdfWriter
from flask import current_app
from app.models.pdf_dto import CompressionLevel, PdfCompressionResult

class PdfService:
    """PDF处理服务"""
    
    def _process_pdf(self, input_path: str, output_path: str, compression_level: CompressionLevel) -> None:
        """
        处理PDF文件 - 使用基本压缩
        Args:
            input_path: 输入文件路径
            output_path: 输出文件路径
            compression_level: 压缩级别
        """
        try:
            reader = PdfReader(input_path)
            writer = PdfWriter()
            
            # 启用压缩
            writer.compress = True
            
            # 处理每个页面
            for page in reader.pages:
                writer.add_page(page)
            
            # 写入新文件，使用最大压缩
            with open(output_path, 'wb') as output_file:
                writer.write(output_file)
                
        except Exception as e:
            print(f"Error in _process_pdf: {str(e)}")
            raise

    def _handle_file(self, file) -> Tuple[str, str, int]:
        """
        处理文件的上传和保存
        Args:
            file: 上传的文件
        Returns:
            Tuple[str, str, int]: (输入文件路径, 输出文件路径, 原始文件大小)
        """
        storage_service = current_app.storage_service
        
        # 获取原始文件名
        original_filename = file.filename
        name, ext = os.path.splitext(original_filename)
        
        # 生成输入文件名（保持中文）
        input_filename = f"original_{name}{ext}"
        input_path = os.path.join(current_app.config['UPLOAD_FOLDER'], input_filename)
        
        # 如果存在同名文件，先删除
        if os.path.exists(input_path):
            os.remove(input_path)
        
        # 保存上传的文件
        storage_service.save_file(file, input_filename, current_app.config['UPLOAD_FOLDER'])
        original_size = storage_service.get_file_size(input_path)
        
        # 生成输出文件名（保持中文）
        output_filename = f"compressed_{name}{ext}"
        output_path = os.path.join(current_app.config['DOWNLOAD_FOLDER'], output_filename)
        
        # 如果存在同名文件，先删除
        if os.path.exists(output_path):
            os.remove(output_path)
        
        return input_path, output_path, original_size

    def compress_pdf(self, file, compression_level: CompressionLevel = CompressionLevel.MEDIUM) -> PdfCompressionResult:
        """
        处理PDF文件
        Args:
            file: 上传的PDF文件
            compression_level: 压缩级别
        Returns:
            处理结果
        """
        storage_service = current_app.storage_service
        
        try:
            # 处理文件
            input_path, output_path, original_size = self._handle_file(file)
            
            # 处理PDF
            self._process_pdf(input_path, output_path, compression_level)
            
            # 获取文件大小
            compressed_size = storage_service.get_file_size(output_path)
            compression_ratio = ((original_size - compressed_size) / original_size * 100)
            
            return PdfCompressionResult(
                file_path=output_path,
                original_size=original_size,
                compressed_size=compressed_size,
                compression_ratio=f"{compression_ratio:.1f}%"
            )
            
        except Exception as e:
            print(f"Error processing PDF: {str(e)}")
            raise 