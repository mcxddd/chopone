<script setup lang="ts">
import { ref } from "vue";
import QrCodeModal from "../ui/QrCodeModal.vue";

const isQrModalOpen = ref(false);
</script>

<template>
  <footer class="footer">
    <div class="footer-content">
      <a class="footer-link" @click="isQrModalOpen = true">联系我</a>
      <span class="footer-link">&copy; 2024 Chopone</span>
    </div>
    <QrCodeModal :is-open="isQrModalOpen" @close="isQrModalOpen = false" />
  </footer>
</template>

<style scoped>
.footer {
  background: linear-gradient(120deg, #2c3e50 0%, #3498db 100%);
  padding: 1.5rem;
  color: white;
}

.footer-content {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 2rem;
}

.footer-link {
  color: white;
  text-decoration: none;
  position: relative;
  padding: 0.5rem 0;
  font-size: 0.9rem;
  line-height: 1;
}

a.footer-link {
  cursor: pointer;
}

a.footer-link::after {
  content: "";
  position: absolute;
  bottom: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 0;
  height: 2px;
  background: white;
  transition: width 0.3s;
}

a.footer-link:hover::after {
  width: 100%;
}
</style>
