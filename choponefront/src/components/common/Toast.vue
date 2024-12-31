<template>
  <Teleport to="body">
    <div class="toast-container">
      <TransitionGroup name="toast">
        <div
          v-for="toast in toasts"
          :key="toast.id"
          class="toast"
          :class="toast.type"
        >
          <span class="toast-icon">{{
            toast.type === "success" ? "✓" : "✕"
          }}</span>
          <span>{{ toast.message }}</span>
        </div>
      </TransitionGroup>
    </div>
  </Teleport>
</template>

<script setup lang="ts">
import { useToast } from "@/composables/useToast";

const { toasts } = useToast();
</script>

<style scoped>
.toast-container {
  position: fixed;
  bottom: 2rem;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  z-index: 9999;
  padding: 0 1rem;
  width: 100%;
  pointer-events: none;
}

.toast {
  padding: 0.8rem 1.5rem;
  border-radius: 8px;
  background: #1e1e1e;
  color: #e2e8f0;
  font-size: 0.9rem;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
  border: 1px solid rgba(255, 255, 255, 0.1);
  display: flex;
  align-items: center;
  gap: 0.5rem;
  min-width: 300px;
  max-width: 90vw;
  margin: 0 auto;
  pointer-events: auto;
}

.toast.success {
  border-color: rgba(16, 185, 129, 0.3);
  background: rgba(16, 185, 129, 0.1);
}

.toast.error {
  border-color: rgba(239, 68, 68, 0.3);
  background: rgba(239, 68, 68, 0.1);
}

.toast-icon {
  font-size: 1.2rem;
  line-height: 1;
}

.toast.success .toast-icon {
  color: #10b981;
}

.toast.error .toast-icon {
  color: #ef4444;
}

/* 过渡动画 */
.toast-enter-active,
.toast-leave-active {
  transition: all 0.3s ease;
}

.toast-enter-from,
.toast-leave-to {
  opacity: 0;
  transform: translateY(20px);
}

/* Mobile Responsive */
@media (max-width: 768px) {
  .toast-container {
    bottom: 1rem;
  }

  .toast {
    min-width: unset;
    width: 100%;
    padding: 0.7rem 1rem;
    font-size: 0.85rem;
  }

  .toast-icon {
    font-size: 1.1rem;
  }

  .toast-enter-from,
  .toast-leave-to {
    transform: translateY(10px);
  }
}
</style>
