import os
import requests
from app.services.session_service import SessionService

class AiService:
    # 最大保留的对话轮数
    MAX_CONVERSATION_TURNS = 40

    def __init__(self):
        self.api_key = os.getenv('OPENAI_API_KEY')
        if not self.api_key:
            raise ValueError("OpenAI API key not configured")

    def chat(self, user_message: str) -> str:
        # 添加用户消息到历史
        SessionService.add_message('user', user_message)
        
        # 获取历史记录
        conversation_history = SessionService.get_chat_history()
        
        # 构建完整的消息列表，包括系统消息
        messages = [
            {
                "role": "system",
                "content": "你是一个友好、专业的 AI 助手。你会用简洁、清晰的方式回答问题，并在合适的时候使用 Markdown 格式来组织回答。"
            }
        ] + conversation_history[-self.MAX_CONVERSATION_TURNS:]  # 只保留最近的对话

        # 设置请求头和数据
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.api_key}'
        }
        
        payload = {
            "model": "gpt-4o-mini",
            "messages": messages,
            "temperature": 0.8,
            "max_tokens": 1000
        }

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
        SessionService.add_message('assistant', reply)

        return reply 