<template>
  <div :class="['message', type]">
    {{ content }}
    <button
      v-if="type === 'ai'"
      :class="['copy-btn', { 'copy-success': copySuccess }]"
      @click="copyContent"
      title="复制内容"
    >
      <span class="copy-icon" v-if="!copySuccess"></span>
      <span class="check-icon" v-else>✓</span>
    </button>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";

const props = defineProps<{
  type: "user" | "ai" | "error" | "loading" | "system";
  content: string;
}>();

const copySuccess = ref(false);

const copyContent = async (event: MouseEvent) => {
  event.stopPropagation();
  try {
    await navigator.clipboard.writeText(props.content);
    copySuccess.value = true;
    setTimeout(() => {
      copySuccess.value = false;
    }, 2000);
  } catch (err) {
    console.error("复制失败:", err);
  }
};
</script>

<style scoped>
.message {
  position: relative;
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

.copy-btn {
  position: absolute;
  bottom: 8px;
  right: 8px;
  background: transparent;
  border: none;
  width: 20px;
  height: 20px;
  cursor: pointer;
  opacity: 0;
  transition: all 0.3s;
  padding: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  color: rgba(255, 255, 255, 0.7);
}

.message:hover .copy-btn {
  opacity: 0.5;
}

.copy-btn:hover {
  opacity: 0.8 !important;
}

.copy-icon {
  position: relative;
  width: 12px;
  height: 12px;
}

.copy-icon::before {
  content: "";
  position: absolute;
  left: 0;
  right: 0;
  top: 5px;
  height: 1.5px;
  background: currentColor;
  box-shadow: 0 -4px 0 currentColor, 0 4px 0 currentColor;
  transition: all 0.3s;
}

.check-icon {
  color: #22c55e;
  font-size: 14px;
  font-weight: bold;
  animation: scale-in 0.2s ease-out;
}

@keyframes scale-in {
  0% {
    transform: scale(0);
  }
  50% {
    transform: scale(1.2);
  }
  100% {
    transform: scale(1);
  }
}

.system {
  background: rgba(147, 197, 253, 0.2);
  color: #bfdbfe;
  margin-right: auto;
  border: 1px solid rgba(147, 197, 253, 0.3);
  font-style: italic;
}
</style>
