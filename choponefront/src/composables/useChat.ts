import { ref } from "vue";
import type { Message } from "@/types/chat";

export function useChat() {
  const messages = ref<Message[]>([]);
  const isLoading = ref(false);

  const sendMessage = async (message: string) => {
    if (!message.trim()) return;

    // 添加用户消息
    messages.value.push({
      type: "user",
      content: message,
    });

    isLoading.value = true;
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

      // 添加 AI 回复
      messages.value.push({
        type: "ai",
        content: data.data.reply,
      });
    } catch (error) {
      console.error("Error:", error);
      messages.value = messages.value.filter((msg) => msg.type !== "loading");
      messages.value.push({
        type: "error",
        content: "抱歉，发生了错误，请稍后重试。",
      });
    } finally {
      isLoading.value = false;
    }
  };

  const addWelcomeMessage = () => {
    messages.value.push({
      type: "ai",
      content: "你好！我是GPT-4o-mini，有什么我可以帮你的吗？",
    });
  };

  return {
    messages,
    isLoading,
    sendMessage,
    addWelcomeMessage,
  };
}
