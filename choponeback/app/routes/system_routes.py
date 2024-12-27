from flask import Blueprint
from app.utils.response_utils import create_response

system_bp = Blueprint('system', __name__)

@system_bp.route('/api/system/health', methods=['GET'])
def health_check():
    return create_response(True, "Backend is running", {
        "status": "healthy",
        "service": "choponeback",
        "version": "1.0.0"
    }) 