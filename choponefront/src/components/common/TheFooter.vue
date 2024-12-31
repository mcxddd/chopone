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
  padding: 0.8rem;
  color: white;
}

.footer-content {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 1.5rem;
}

.footer-link {
  color: white;
  text-decoration: none;
  position: relative;
  padding: 0.3rem 0;
  font-size: 0.85rem;
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

/* Mobile Responsive */
@media (max-width: 768px) {
  .footer {
    padding: 1rem;
  }

  .footer-content {
    gap: 1.5rem;
  }

  .footer-link {
    font-size: 0.85rem;
    padding: 0.3rem 0;
  }
}
</style>
