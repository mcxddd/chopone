<script setup lang="ts">
import ToolsSection from "./tools/ToolsSection.vue";
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
  background: #1a1a1a;
}

.tools-header {
  background: linear-gradient(120deg, #1e1e1e 0%, #2d3436 100%);
  padding: 1.2rem;
  text-align: center;
  color: #e2e8f0;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  position: relative;
  overflow: hidden;
}

.tools-header::before {
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

.tools-header h1 {
  font-size: 1.5rem;
  margin-bottom: 0.3rem;
  background: linear-gradient(120deg, #6366f1 0%, #a855f7 100%);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  position: relative;
}

.tools-header p {
  font-size: 1rem;
  opacity: 0.9;
  margin: 0;
  color: #94a3b8;
  position: relative;
}

.tools-container {
  flex: 1;
  display: flex;
  align-items: flex-start;
  padding: 1rem 0;
  background: #1a1a1a;
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
