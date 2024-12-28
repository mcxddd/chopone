from flask import Blueprint
from app.utils.response_utils import create_response
from datetime import datetime

system_bp = Blueprint('system', __name__)

@system_bp.route('/api/system/health', methods=['GET'])
def health_check():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return create_response(True, "Backend is running", {
        "status": "healthy",
        "service": "choponeback",
        "version": "1.0.0",
        "timestamp": current_time
    }) 