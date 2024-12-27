import os
from PyPDF2 import PdfReader, PdfWriter
from werkzeug.utils import secure_filename
from flask import current_app
from enum import Enum

class CompressionLevel(Enum):
    VERY_LOW = 10    # 90% quality
    LOW = 30         # 70% quality
    MEDIUM = 50      # 50% quality
    HIGH = 70        # 30% quality
    VERY_HIGH = 90   # 10% quality

def compress_pdf(file, compression_level=CompressionLevel.MEDIUM):
    """
    Compress PDF file by reducing image quality and optimizing content
    Args:
        file: The uploaded PDF file
        compression_level: CompressionLevel enum (10, 30, 50, 70, 90)
    """
    filename = secure_filename(file.filename)
    
    # Ensure both upload and download directories exist
    if not os.path.exists(current_app.config['UPLOAD_FOLDER']):
        os.makedirs(current_app.config['UPLOAD_FOLDER'])
    if not os.path.exists(current_app.config['DOWNLOAD_FOLDER']):
        os.makedirs(current_app.config['DOWNLOAD_FOLDER'])
        
    # Save uploaded file to upload folder
    input_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
    # Save compressed file to download folder with compression level in filename
    output_filename = f'compressed_{compression_level.value}_{filename}'
    output_path = os.path.join(current_app.config['DOWNLOAD_FOLDER'], output_filename)
    
    file.save(input_path)
    
    reader = PdfReader(input_path)
    writer = PdfWriter()

    # Calculate image quality based on compression level
    image_quality = 100 - compression_level.value

    # Compress each page
    for page in reader.pages:
        # Reduce image quality
        for image in page.images:
            image.quality = image_quality  # Set image quality based on compression level
            image.reduce_size()
        
        # Add compressed page
        writer.add_page(page)
    
    # Set compression parameters
    writer.set_compression(True)  # Enable compression
    writer.compress_streams = True  # Compress stream objects
    
    # Adjust content stream compression based on level
    if compression_level in [CompressionLevel.HIGH, CompressionLevel.VERY_HIGH]:
        writer.compress_content_streams = True
    
    # Write the compressed PDF to download folder
    with open(output_path, 'wb') as output_file:
        writer.write(output_file)
    
    # Clean up the input file from upload folder
    os.remove(input_path)
    
    # Get file sizes for comparison
    original_size = os.path.getsize(input_path) if os.path.exists(input_path) else 0
    compressed_size = os.path.getsize(output_path)
    compression_ratio = ((original_size - compressed_size) / original_size * 100) if original_size > 0 else 0
    
    return {
        'file_path': output_path,
        'original_size': original_size,
        'compressed_size': compressed_size,
        'compression_ratio': f"{compression_ratio:.1f}%",
        'compression_level': compression_level.name,
        'image_quality': f"{image_quality}%"
    } 