<!-- AI Chat 界面 -->
<template>
  <div class="ai-chat">
    <div class="action-buttons">
      <button @click="restartChat" class="action-btn">
        <i class="fas fa-redo"></i>
        重新开始
      </button>
      <button class="action-btn disabled">
        <i class="fas fa-exchange-alt"></i>
        开发中
      </button>
      <button class="action-btn disabled">
        <i class="fas fa-tools"></i>
        开发中
      </button>
    </div>
    <div class="chat-container">
      <div class="chat-messages" ref="messagesContainer">
        <TransitionGroup name="message-fade">
          <ChatMessage
            v-for="(msg, index) in messages"
            :key="index"
            :type="msg.type"
            :content="msg.content"
          />
        </TransitionGroup>
      </div>
      <div class="chat-input">
        <input
          v-model="userInput"
          @keyup.enter="sendMessage"
          placeholder="输入消息，按回车发送..."
          type="text"
        />
        <button @click="sendMessage">发送</button>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, nextTick, TransitionGroup } from "vue";
import type { Message } from "@/types/chat";
import ChatMessage from "@/components/chat/ChatMessage.vue";

const userInput = ref("");
const messages = ref<Message[]>([]);
const messagesContainer = ref<HTMLElement | null>(null);

const sendMessage = async () => {
  if (!userInput.value.trim()) return;

  // 添加用户消息到本地显示
  messages.value.push({
    type: "user",
    content: userInput.value,
  });

  const message = userInput.value;
  userInput.value = "";

  // 添加加载状态消息
  messages.value.push({
    type: "loading",
    content: "正在思考",
  });

  try {
    const response = await fetch("/api/ai/chat", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      credentials: "include",
      body: JSON.stringify({ message }),
    });

    if (!response.ok) {
      throw new Error("Network response was not ok");
    }

    const data = await response.json();

    // 移除加载状态消息
    messages.value = messages.value.filter((msg) => msg.type !== "loading");

    // 添加 AI 回复到本地显示
    messages.value.push({
      type: "ai",
      content: data.data.reply,
    });

    // 滚动到底部
    await nextTick();
    if (messagesContainer.value) {
      messagesContainer.value.scrollTop = messagesContainer.value.scrollHeight;
    }
  } catch (error) {
    console.error("Error:", error);
    // 移除加载状态消息
    messages.value = messages.value.filter((msg) => msg.type !== "loading");
    messages.value.push({
      type: "error",
      content: "抱歉，发生了错误，请稍后重试。",
    });
  }
};

// 添加欢迎消息
onMounted(() => {
  messages.value.push({
    type: "ai",
    content: "你好！我是GPT-4o-mini，有什么我可以帮你的吗？",
  });
});

// 重新开始对话
const restartChat = async () => {
  try {
    // 先清空消息，触发淡出动画
    messages.value = [];

    const response = await fetch("/api/ai/restart", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      credentials: "include",
    });

    if (!response.ok) {
      throw new Error("Network response was not ok");
    }

    const data = await response.json();

    // 短暂延迟后添加欢迎消息，让动画效果更明显
    setTimeout(() => {
      messages.value = [
        {
          type: "ai",
          content: data.data.welcome_message,
        },
      ];
    }, 300);
  } catch (error) {
    console.error("Error:", error);
    messages.value.push({
      type: "error",
      content: "重新开始对话失败，请稍后重试。",
    });
  }
};
</script>

<style scoped>
.ai-chat {
  max-width: 800px;
  margin: 20px auto;
  padding: 20px;
  min-height: calc(100vh - 56px - 40px);
  display: flex;
  flex-direction: column;
}

.chat-container {
  background: linear-gradient(120deg, #1a1a1a 0%, #2d3436 100%);
  border-radius: 8px;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.3);
  height: calc(100vh - 116px);
  display: flex;
  flex-direction: column;
  border: 1px solid rgba(255, 255, 255, 0.1);
}

.chat-messages {
  flex: 1;
  overflow-y: auto;
  padding: 20px;
}

.message {
  margin: 10px 0;
  padding: 12px 16px;
  border-radius: 8px;
  max-width: 80%;
  color: #e2e8f0;
}

.user {
  background: rgba(99, 102, 241, 0.2);
  margin-left: auto;
  border: 1px solid rgba(99, 102, 241, 0.3);
}

.ai {
  background: rgba(255, 255, 255, 0.1);
  margin-right: auto;
  border: 1px solid rgba(255, 255, 255, 0.2);
}

.error {
  background: rgba(239, 68, 68, 0.2);
  color: #fecaca;
  margin-right: auto;
  border: 1px solid rgba(239, 68, 68, 0.3);
}

.loading {
  background: rgba(255, 255, 255, 0.1);
  margin-right: auto;
  border: 1px solid rgba(255, 255, 255, 0.2);
  position: relative;
  overflow: hidden;
}

.loading::before {
  content: "...";
  animation: dots 2s infinite;
  letter-spacing: 2px;
}

.loading::after {
  content: "";
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 2px;
  background: linear-gradient(
    90deg,
    transparent 0%,
    #6366f1 50%,
    transparent 100%
  );
  animation: loading-line 1.5s ease-in-out infinite;
}

@keyframes dots {
  0%,
  20% {
    content: ".";
  }
  40%,
  60% {
    content: "..";
  }
  80%,
  100% {
    content: "...";
  }
}

@keyframes loading-line {
  0% {
    transform: translateX(-100%);
  }
  50% {
    transform: translateX(100%);
  }
  100% {
    transform: translateX(-100%);
  }
}

.chat-input {
  display: flex;
  padding: 20px;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  background: rgba(0, 0, 0, 0.2);
  border-radius: 0 0 8px 8px;
}

input {
  flex: 1;
  padding: 12px;
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 4px;
  margin-right: 10px;
  font-size: 14px;
  background: rgba(255, 255, 255, 0.1);
  color: #e2e8f0;
  transition: all 0.3s;
}

input::placeholder {
  color: rgba(255, 255, 255, 0.5);
}

input:focus {
  outline: none;
  border-color: rgba(99, 102, 241, 0.5);
  background: rgba(255, 255, 255, 0.15);
}

button {
  padding: 12px 24px;
  background: rgba(99, 102, 241, 0.2);
  color: #e2e8f0;
  border: 1px solid rgba(99, 102, 241, 0.3);
  border-radius: 4px;
  cursor: pointer;
  font-size: 14px;
  transition: all 0.3s;
}

button:hover {
  background: rgba(99, 102, 241, 0.3);
  transform: translateY(-1px);
}

/* 滚动条样式 */
.chat-messages::-webkit-scrollbar {
  width: 6px;
}

.chat-messages::-webkit-scrollbar-track {
  background: rgba(255, 255, 255, 0.1);
}

.chat-messages::-webkit-scrollbar-thumb {
  background: rgba(255, 255, 255, 0.2);
  border-radius: 3px;
}

.chat-messages::-webkit-scrollbar-thumb:hover {
  background: rgba(255, 255, 255, 0.3);
}

.action-buttons {
  display: flex;
  gap: 12px;
  margin-bottom: 16px;
  justify-content: center;
}

.action-btn {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 10px 20px;
  background: rgba(99, 102, 241, 0.1);
  color: #e2e8f0;
  border: 1px solid rgba(99, 102, 241, 0.2);
  border-radius: 6px;
  cursor: pointer;
  font-size: 14px;
  transition: all 0.3s ease;
}

.action-btn:hover {
  background: rgba(99, 102, 241, 0.2);
  transform: translateY(-2px);
  box-shadow: 0 2px 8px rgba(99, 102, 241, 0.2);
}

.action-btn i {
  font-size: 16px;
}

.action-btn.disabled {
  opacity: 0.5;
  cursor: not-allowed;
  pointer-events: none;
}

.action-btn.disabled:hover {
  transform: none;
  box-shadow: none;
}

.system {
  background: rgba(147, 197, 253, 0.2);
  color: #bfdbfe;
  margin-right: auto;
  border: 1px solid rgba(147, 197, 253, 0.3);
  font-style: italic;
}

.message-fade-enter-active,
.message-fade-leave-active {
  transition: all 0.3s ease;
}

.message-fade-enter-from {
  opacity: 0;
  transform: translateY(20px);
}

.message-fade-leave-to {
  opacity: 0;
  transform: translateY(-20px);
}

.message-fade-move {
  transition: transform 0.3s ease;
}
</style>
