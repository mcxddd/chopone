<script setup lang="ts">
import { useRouter } from "vue-router";

const router = useRouter();

const tools = [
  {
    id: "future-tool-1",
    name: "未来小工具1",
    description: "正在开发中...",
    icon: "🔨",
  },
  {
    id: "future-tool-2",
    name: "未来小工具2",
    description: "正在开发中...",
    icon: "🛠️",
  },
  {
    id: "future-tool-3",
    name: "未来小工具3",
    description: "正在开发中...",
    icon: "⚙️",
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
  padding: 1rem;
  max-width: 800px;
  margin: 0 auto;
}

.tools-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1.5rem;
  width: 100%;
}

.tool-card {
  background: #1e1e1e;
  border-radius: 12px;
  padding: 1.2rem;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
  cursor: pointer;
  transition: all 0.3s;
  position: relative;
  overflow: hidden;
  width: 100%;
  border: 1px solid rgba(255, 255, 255, 0.1);
}

.tool-card::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 4px;
  background: linear-gradient(90deg, #6366f1, #a855f7);
}

.tool-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 6px 24px rgba(99, 102, 241, 0.2);
  border-color: rgba(99, 102, 241, 0.3);
}

.tool-icon {
  font-size: 2.5rem;
  margin-bottom: 1rem;
  color: #6366f1;
}

.tool-card h3 {
  color: #e2e8f0;
  margin-bottom: 0.5rem;
}

.tool-card p {
  color: #94a3b8;
  font-size: 0.9rem;
  line-height: 1.5;
}

/* Mobile Responsive */
@media (max-width: 768px) {
  .tools {
    padding: 0.8rem;
  }

  .tools-grid {
    gap: 0.8rem;
  }

  .tool-card {
    padding: 1rem;
  }

  .tool-icon {
    font-size: 2rem;
    margin-bottom: 0.5rem;
  }

  .tool-card h3 {
    font-size: 0.95rem;
    margin-bottom: 0.3rem;
  }

  .tool-card p {
    font-size: 0.8rem;
    line-height: 1.3;
  }
}

/* Remove the single column layout for extra small devices */
@media (max-width: 360px) {
  .tool-card {
    padding: 0.8rem;
  }

  .tool-icon {
    font-size: 1.8rem;
  }

  .tool-card h3 {
    font-size: 0.9rem;
  }

  .tool-card p {
    font-size: 0.75rem;
  }
}
</style>
