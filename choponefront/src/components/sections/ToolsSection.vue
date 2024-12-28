<script setup lang="ts">
import { useRouter } from "vue-router";

const router = useRouter();

const tools = [
  {
    id: "pdf-compress",
    name: "PDF压缩",
    description: "在线压缩PDF文件，快速且保持质量",
    icon: "📄",
  },
];
</script>

<template>
  <section class="tools">
    <div class="tools-grid">
      <div
        v-for="tool in tools"
        :key="tool.id"
        class="tool-card"
        @click="router.push(`/tools/${tool.id}`)"
      >
        <div class="tool-icon">{{ tool.icon }}</div>
        <h3>{{ tool.name }}</h3>
        <p>{{ tool.description }}</p>
      </div>
    </div>
  </section>
</template>

<style scoped>
.tools {
  padding: 2rem;
  max-width: 1200px;
  margin: 0 auto;
}

.tools-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 2rem;
}

.tool-card {
  background: white;
  border-radius: 12px;
  padding: 2rem;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
  cursor: pointer;
  transition: all 0.3s;
  position: relative;
  overflow: hidden;
}

.tool-card::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 4px;
  background: linear-gradient(90deg, #3498db, #2c3e50);
}

.tool-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 6px 24px rgba(0, 0, 0, 0.1);
}

.tool-icon {
  font-size: 2.5rem;
  margin-bottom: 1rem;
}

.tool-card h3 {
  color: #2c3e50;
  margin-bottom: 0.5rem;
}

.tool-card p {
  color: #666;
  font-size: 0.9rem;
  line-height: 1.5;
}
</style>
