<script setup lang="ts">
import { useToast } from "@/composables/useToast";

const { showToast } = useToast();

const showSuccessToast = () => {
  showToast("这是一条成功消息", "success");
};

const showErrorToast = () => {
  showToast("这是一条错误消息", "error");
};
</script>

<template>
  <section class="intro">
    <div class="intro-content">
      <h1>Chopone</h1>
      <p class="description">一个小工具集合</p>
      <p class="status">其他功能正在开发中...</p>
      <div class="test-buttons">
        <button class="test-btn success" @click="showSuccessToast">
          测试成功通知
        </button>
        <button class="test-btn error" @click="showErrorToast">
          测试错误通知
        </button>
      </div>
    </div>
  </section>
</template>

<style scoped>
.intro {
  background: linear-gradient(120deg, #1a1a1a 0%, #2d3436 100%);
  min-height: calc(100vh - 56px - 52px); /* viewport height - header - footer */
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 2rem;
  text-align: center;
  color: #e2e8f0;
  position: relative;
  overflow: hidden;
}

.intro::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: radial-gradient(
    circle at 50% 50%,
    rgba(99, 102, 241, 0.15) 0%,
    transparent 50%
  );
  pointer-events: none;
}

.intro-content {
  max-width: 600px;
  position: relative;
  z-index: 1;
}

h1 {
  font-size: 3.5rem;
  margin-bottom: 1.5rem;
  font-weight: 600;
  background: linear-gradient(120deg, #6366f1 0%, #a855f7 100%);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}

.description {
  font-size: 1.5rem;
  margin-bottom: 1rem;
  color: #e2e8f0;
  opacity: 0.9;
}

.status {
  font-size: 1.1rem;
  color: #94a3b8;
  opacity: 0.9;
}

.test-buttons {
  display: flex;
  gap: 1rem;
  justify-content: center;
  margin-top: 2rem;
}

.test-btn {
  padding: 0.8rem 1.5rem;
  border-radius: 8px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.3s;
  border: none;
  color: #e2e8f0;
  font-size: 0.9rem;
}

.test-btn.success {
  background: rgba(16, 185, 129, 0.2);
  border: 1px solid rgba(16, 185, 129, 0.3);
}

.test-btn.success:hover {
  background: rgba(16, 185, 129, 0.3);
}

.test-btn.error {
  background: rgba(239, 68, 68, 0.2);
  border: 1px solid rgba(239, 68, 68, 0.3);
}

.test-btn.error:hover {
  background: rgba(239, 68, 68, 0.3);
}

@media (max-width: 768px) {
  h1 {
    font-size: 2.5rem;
  }

  .description {
    font-size: 1.2rem;
  }

  .status {
    font-size: 1rem;
  }

  .test-buttons {
    flex-direction: column;
    gap: 0.8rem;
  }

  .test-btn {
    width: 100%;
    padding: 0.7rem 1rem;
  }
}
</style>
