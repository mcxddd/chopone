import os
import requests
from app.services.session_service import SessionService
from typing import List, Dict

class AiService:
    # 最大历史记录总字符数（约 16K tokens，考虑到 GPT-4 的上下文窗口大小）
    MAX_HISTORY_CHARS = 65536  # 64KB

    def __init__(self):
        self.api_key = os.getenv('OPENAI_API_KEY')
        if not self.api_key:
            raise ValueError("OpenAI API key not configured")

    def _trim_history_by_length(self, history: List[Dict[str, str]]) -> List[Dict[str, str]]:
        """基于字符长度修剪历史记录，保留最近的消息"""
        total_chars = 0
        trimmed_history = []
        
        # 从最新的消息开始计算
        for message in reversed(history):
            message_chars = len(message['content'])
            if total_chars + message_chars > self.MAX_HISTORY_CHARS:
                break
            total_chars += message_chars
            trimmed_history.insert(0, message)  # 在开头插入，保持顺序
            
        return trimmed_history

    def chat(self, user_message: str) -> str:
        # 添加用户消息到历史
        SessionService.add_message('user', user_message)
        
        # 获取历史记录
        conversation_history = SessionService.get_chat_history()
        
        # 基于字符长度修剪历史记录
        trimmed_history = self._trim_history_by_length(conversation_history)
        
        # 构建完整的消息列表，包括系统消息
        messages = [
            {
                "role": "system",
                "content": "你是一个友好、专业的 AI 助手。你会用简洁、清晰的方式回答问题，并在合适的时候使用 Markdown 格式来组织回答。"
            }
        ] + trimmed_history

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