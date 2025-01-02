from typing import List, Dict, Optional
from datetime import datetime
from flask import session

class SessionService:
    # Session 键的常量定义
    CHAT_KEY = 'chat'
    PREFERENCES_KEY = 'preferences'
    
    @staticmethod
    def get_chat_history() -> List[Dict]:
        """获取聊天历史"""
        chat_data = session.get(SessionService.CHAT_KEY, {})
        return chat_data.get('conversation_history', [])
    
    @staticmethod
    def add_message(role: str, content: str):
        """添加新消息"""
        chat_data = session.get(SessionService.CHAT_KEY, {
            'conversation_history': [],
            'message_count': 0
        })
        
        # 添加消息
        chat_data['conversation_history'].append({
            'role': role,
            'content': content,
            'timestamp': datetime.now().isoformat()
        })
        
        # 更新计数和最后活动时间
        chat_data['message_count'] = len(chat_data['conversation_history'])
        chat_data['last_active'] = datetime.now().isoformat()
        
        # 保存回 session
        session[SessionService.CHAT_KEY] = chat_data
    
    @staticmethod
    def clear_chat_history():
        """清除聊天历史"""
        if SessionService.CHAT_KEY in session:
            del session[SessionService.CHAT_KEY]
    
    @staticmethod
    def get_session_info() -> Dict:
        """获取 session 信息，用于调试"""
        session_data = dict(session)
        stats = {
            'session_keys': list(session_data.keys()),
            'session_size': len(str(session_data))
        }
        
        # 添加聊天统计
        if SessionService.CHAT_KEY in session_data:
            chat_data = session_data[SessionService.CHAT_KEY]
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