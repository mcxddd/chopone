from dataclasses import dataclass
from typing import Optional
from enum import Enum

class CompressionLevel(Enum):
    """压缩级别"""
    LOW = 20     # 低压缩，较好质量
    MEDIUM = 5   # 中等压缩，一般质量
    HIGH = 1     # 高压缩，低质量

@dataclass
class PdfCompressionRequest:
    file_name: str
    compression_level: CompressionLevel

@dataclass
class PdfCompressionResult:
    """PDF压缩结果"""
    file_path: str
    original_size: int
    compressed_size: int
    compression_ratio: str

@dataclass
class ApiResponse:
    success: bool
    message: str
    data: Optional[any] = None 