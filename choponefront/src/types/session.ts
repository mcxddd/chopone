export interface ChatMessage {
  role: "user" | "assistant";
  content: string;
  timestamp?: string;
}

export interface ChatSession {
  conversation_history: ChatMessage[];
  last_active?: string;
  message_count?: number;
}

export interface UserPreferences {
  theme: "light" | "dark";
  language: "zh" | "en";
}

export interface AppSession {
  chat: ChatSession;
  preferences: UserPreferences;
}
