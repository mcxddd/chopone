from flask import Blueprint, request
from app.utils.response_utils import create_response
from app.services.ai_service import AiService
from app.services.session_service import SessionService

ai_bp = Blueprint('ai', __name__)
ai_service = AiService()

@ai_bp.route('/api/ai/chat', methods=['POST'])
def chat():
    try:
        # 获取请求数据
        data = request.get_json()
        if not data or 'message' not in data:
            return create_response(False, "Message is required"), 400

        # 调用服务处理聊天
        reply = ai_service.chat(data['message'])

        # 返回结果
        return create_response(True, "Success", {
            "reply": reply
        })

    except ValueError as ve:
        error_msg = str(ve)
        return create_response(False, error_msg), 500
        
    except Exception as e:
        error_msg = str(e)
        return create_response(False, error_msg), 500 

@ai_bp.route('/api/ai/restart', methods=['POST'])
def restart_chat():
    try:
        # 清除聊天历史
        SessionService.clear_chat_history()
        # 添加欢迎消息
        welcome_message = "你好！我是GPT-4o-mini，有什么我可以帮你的吗？"
        SessionService.add_message('assistant', welcome_message)
        return create_response(True, "Chat restarted successfully", {
            "welcome_message": welcome_message
        })
    except Exception as e:
        return create_response(False, str(e)), 500 