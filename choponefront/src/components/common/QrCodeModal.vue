<script setup lang="ts">
defineProps<{
  isOpen: boolean;
}>();

defineEmits<{
  close: [];
}>();
</script>

<template>
  <div v-if="isOpen" class="modal-overlay" @click="$emit('close')">
    <div class="modal-content" @click.stop>
      <div class="qr-container">
        <div class="qr-item">
          <div class="temp-qr">
            <div class="inner-square"></div>
          </div>
          <p class="qr-text">二维码</p>
        </div>
        <div class="qr-item">
          <div class="temp-qr">
            <div class="inner-square"></div>
          </div>
          <p class="qr-text">请我一杯奶茶</p>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.7);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.modal-content {
  background: #1e1e1e;
  border-radius: 12px;
  padding: 2rem;
  max-width: 90%;
  width: 500px;
  position: relative;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
  border: 1px solid rgba(255, 255, 255, 0.1);
}

.modal-header {
  text-align: center;
  margin-bottom: 1.5rem;
}

.modal-title {
  color: #e2e8f0;
  font-size: 1.5rem;
  font-weight: 600;
  margin-bottom: 0.5rem;
}

.modal-description {
  color: #94a3b8;
  font-size: 0.9rem;
}

.qr-code {
  background: white;
  padding: 1rem;
  border-radius: 8px;
  margin: 0 auto 1.5rem;
  width: fit-content;
}

.close-btn {
  position: absolute;
  top: 1rem;
  right: 1rem;
  background: none;
  border: none;
  color: #94a3b8;
  font-size: 1.5rem;
  cursor: pointer;
  padding: 0.5rem;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s;
  border-radius: 50%;
}

.close-btn:hover {
  color: #e2e8f0;
  background: rgba(255, 255, 255, 0.1);
}

.qr-container {
  display: flex;
  gap: 2rem;
  justify-content: center;
}

.qr-item {
  text-align: center;
}

.temp-qr {
  width: 180px;
  height: 180px;
  background: #2d3436;
  border: 2px solid #6366f1;
  margin-bottom: 1rem;
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 8px;
}

.inner-square {
  width: 90px;
  height: 90px;
  background: #6366f1;
  opacity: 0.6;
}

.qr-text {
  color: #e2e8f0;
  font-size: 1.1rem;
  margin-top: 0.5rem;
}

/* Mobile Responsive */
@media (max-width: 768px) {
  .qr-container {
    flex-direction: column;
    gap: 1.5rem;
    align-items: center;
  }

  .temp-qr {
    width: 150px;
    height: 150px;
    margin-bottom: 0.8rem;
  }

  .inner-square {
    width: 75px;
    height: 75px;
  }

  .qr-text {
    font-size: 1rem;
  }

  .modal-content {
    padding: 1.5rem;
    margin: 1rem;
  }
}
</style>
