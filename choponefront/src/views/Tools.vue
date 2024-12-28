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
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  position: absolute;
  top: 56px;
  left: 0;
  right: 0;
  bottom: 0;
}

.tools-header {
  background: linear-gradient(120deg, #2c3e50 0%, #3498db 100%);
  padding: 2rem;
  text-align: center;
  color: white;
}

.tools-header h1 {
  font-size: 2rem;
  margin-bottom: 0.5rem;
}

.tools-header p {
  font-size: 1.1rem;
  opacity: 0.9;
  margin: 0;
}

.tools-container {
  flex: 1;
  background: #f8f9fa;
  display: flex;
  align-items: flex-start;
}

:deep(.tools) {
  width: 100%;
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
}

:deep(.tools-grid) {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 2rem;
}
</style>
