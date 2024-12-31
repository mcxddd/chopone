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
  background: rgba(0, 0, 0, 0.2);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.modal-content {
  background: white;
  padding: 2rem;
  border-radius: 12px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
}

.qr-container {
  display: flex;
  gap: 2rem;
}

.qr-item {
  text-align: center;
}

.temp-qr {
  width: 180px;
  height: 180px;
  background: #f0f2f5;
  border: 2px solid #3498db;
  margin-bottom: 1rem;
  display: flex;
  justify-content: center;
  align-items: center;
}

.inner-square {
  width: 90px;
  height: 90px;
  background: #3498db;
  opacity: 0.6;
}

.qr-text {
  color: #2c3e50;
  font-size: 1.1rem;
}
</style>
