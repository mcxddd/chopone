<template>
  <div :class="['message', type]">
    {{ content }}
  </div>
</template>

<script setup lang="ts">
defineProps<{
  type: "user" | "ai" | "error" | "loading";
  content: string;
}>();
</script>

<style scoped>
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
</style>
