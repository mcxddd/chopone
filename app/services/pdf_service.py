import os
from PyPDF2 import PdfReader, PdfWriter
from werkzeug.utils import secure_filename
from flask import current_app

def compress_pdf(file):
    """Compress PDF file by reducing image quality and optimizing content"""
    filename = secure_filename(file.filename)
    
    # Ensure both upload and download directories exist
    if not os.path.exists(current_app.config['UPLOAD_FOLDER']):
        os.makedirs(current_app.config['UPLOAD_FOLDER'])
    if not os.path.exists(current_app.config['DOWNLOAD_FOLDER']):
        os.makedirs(current_app.config['DOWNLOAD_FOLDER'])
        
    # Save uploaded file to upload folder
    input_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
    # Save compressed file to download folder
    output_path = os.path.join(current_app.config['DOWNLOAD_FOLDER'], f'compressed_{filename}')
    
    file.save(input_path)
    
    reader = PdfReader(input_path)
    writer = PdfWriter()

    # Compress each page
    for page in reader.pages:
        # Reduce image quality
        for image in page.images:
            image.quality = 50  # Reduce image quality to 50%
            image.reduce_size()
        
        # Add compressed page
        writer.add_page(page)
    
    # Set compression parameters
    writer.set_compression(True)  # Enable compression
    writer.compress_streams = True  # Compress stream objects
    writer.compress_content_streams = True  # Compress content streams
    
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
        'compression_ratio': f"{compression_ratio:.1f}%"
    } 