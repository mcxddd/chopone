from flask import Blueprint
from app.utils.response_utils import create_response
from app.services.session_service import SessionService
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

@system_bp.route('/api/system/debug/session', methods=['GET'])
def debug_session():
    try:
        session_info = SessionService.get_session_info()
        return create_response(True, "Session data retrieved", session_info)
    except Exception as e:
        return create_response(False, str(e)), 500