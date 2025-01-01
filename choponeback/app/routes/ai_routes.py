from flask import Blueprint, request, session
from app.utils.response_utils import create_response
import requests
import os
import json

ai_bp = Blueprint('ai', __name__)

# 最大保留的对话轮数
MAX_CONVERSATION_TURNS = 10

@ai_bp.route('/api/ai/chat', methods=['POST'])
def chat():
    try:
        # 获取请求数据
        data = request.get_json()
        if not data or 'message' not in data:
            return create_response(False, "Message is required"), 400

        # 获取 API key
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            return create_response(False, "OpenAI API key not configured"), 500

        # 获取或初始化会话历史
        conversation_history = session.get('conversation_history', [])

        # 添加用户消息到历史
        conversation_history.append({
            "role": "user",
            "content": data['message']
        })

        # 构建完整的消息列表，包括系统消息
        messages = [
            {
                "role": "system",
                "content": "你是一个友好、专业的 AI 助手。你会用简洁、清晰的方式回答问题，并在合适的时候使用 Markdown 格式来组织回答。"
            }
        ] + conversation_history[-MAX_CONVERSATION_TURNS:]  # 只保留最近的对话

        # 设置请求头和数据
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {api_key}'
        }
        
        payload = {
            "model": "gpt-4o-mini",
            "messages": messages,
            "temperature": 0.7,
            "max_tokens": 1000
        }

        try:
            # 发送请求
            response = requests.post(
                'https://api.gptsapi.net/v1/chat/completions',
                headers=headers,
                json=payload
            )
            
            # 检查响应状态
            response.raise_for_status()
            result = response.json()

            # 获取回复
            reply = result['choices'][0]['message']['content']

            # 添加助手回复到历史
            conversation_history.append({
                "role": "assistant",
                "content": reply
            })

            # 更新会话历史
            session['conversation_history'] = conversation_history

            # 返回结果
            return create_response(True, "Success", {
                "reply": reply
            })
        except Exception as api_error:
            error_msg = str(api_error)
            print(f"API Error: {error_msg}")
            return create_response(False, f"API Error: {error_msg}"), 500

    except Exception as e:
        error_msg = str(e)
        print(f"General Error: {error_msg}")
        return create_response(False, error_msg), 500 