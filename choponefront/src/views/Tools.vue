<script setup lang="ts">
import ToolsSection from "../components/sections/ToolsSection.vue";
</script>

<template>
  <div class="tools-page">
    <div class="tools-header">
      <h1>小工具</h1>
      <p>实用的在线工具集合</p>
    </div>
    <div class="tools-container">
      <ToolsSection />
    </div>
  </div>
</template>

<style scoped>
.tools-page {
  min-height: calc(100vh - 56px);
  display: flex;
  flex-direction: column;
  background: #f8f9fa;
}

.tools-header {
  background: linear-gradient(120deg, #2c3e50 0%, #3498db 100%);
  padding: 1.2rem;
  text-align: center;
  color: white;
}

.tools-header h1 {
  font-size: 1.5rem;
  margin-bottom: 0.3rem;
}

.tools-header p {
  font-size: 1rem;
  opacity: 0.9;
  margin: 0;
}

.tools-container {
  flex: 1;
  display: flex;
  align-items: flex-start;
  padding: 1rem 0;
}

:deep(.tools) {
  width: 100%;
  margin: 0 auto;
}

/* Mobile Responsive */
@media (max-width: 768px) {
  .tools-header {
    padding: 1rem;
  }

  .tools-header h1 {
    font-size: 1.3rem;
  }

  .tools-header p {
    font-size: 0.9rem;
  }
}
</style>
