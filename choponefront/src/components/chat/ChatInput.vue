<template>
  <div class="chat-input">
    <input
      v-model="inputValue"
      @keyup.enter="handleSend"
      placeholder="输入消息，按回车发送..."
      type="text"
    />
    <button @click="handleSend" :disabled="isLoading">发送</button>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";

const props = defineProps<{
  isLoading?: boolean;
}>();

const emit = defineEmits<{
  (e: "send", message: string): void;
}>();

const inputValue = ref("");

const handleSend = () => {
  if (!inputValue.value.trim() || props.isLoading) return;
  emit("send", inputValue.value);
  inputValue.value = "";
};
</script>

<style scoped>
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

button:hover:not(:disabled) {
  background: rgba(99, 102, 241, 0.3);
}

button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}
</style>
