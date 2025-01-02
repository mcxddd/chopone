from typing import List, Dict
from datetime import datetime
from flask import session

class SessionService:
    # session 中存储聊天历史的键名
    CHAT_HISTORY_KEY = 'chat_history'
    
    @staticmethod
    def get_chat_history() -> List[Dict]:
        """获取聊天历史"""
        chat_data = session.get(SessionService.CHAT_HISTORY_KEY, {})
        return chat_data.get('conversation_history', [])
    
    @staticmethod
    def add_message(role: str, content: str):
        """添加新消息"""
        chat_data = session.get(SessionService.CHAT_HISTORY_KEY, {
            'conversation_history': [],
            'message_count': 0
        })
        
        # 创建消息字典
        message = {
            'role': role,
            'content': content,
            'timestamp': datetime.now().isoformat()
        }
        
        # 直接添加字典
        chat_data['conversation_history'].append(message)
        
        # 更新计数和最后活动时间
        chat_data['message_count'] = len(chat_data['conversation_history'])
        chat_data['last_active'] = datetime.now().isoformat()
        
        # 保存回 session
        session[SessionService.CHAT_HISTORY_KEY] = chat_data
    
    @staticmethod
    def clear_chat_history():
        """清除聊天历史"""
        if SessionService.CHAT_HISTORY_KEY in session:
            del session[SessionService.CHAT_HISTORY_KEY]
    
    @staticmethod
    def get_session_info() -> Dict:
        """获取 session 信息，用于调试"""
        session_data = dict(session)
        
        stats = {
            'session_keys': list(session_data.keys()),
            'session_size': len(str(session_data))
        }
        
        # 添加聊天统计
        if SessionService.CHAT_HISTORY_KEY in session_data:
            chat_data = session_data[SessionService.CHAT_HISTORY_KEY]
            history = chat_data.get('conversation_history', [])
            stats['chat'] = {
                'total_messages': len(history),
                'user_messages': sum(1 for msg in history if msg['role'] == 'user'),
                'assistant_messages': sum(1 for msg in history if msg['role'] == 'assistant'),
                'last_active': chat_data.get('last_active')
            }
            
        return {
            'session_data': session_data,
            'stats': stats
        } 