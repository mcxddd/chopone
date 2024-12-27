<script setup lang="ts">
import { ref } from "vue";

const features = ref([
  {
    title: "高效数据处理",
    description: "先进的数据处理算法，快速处理海量数据",
    icon: "⚡",
  },
  {
    title: "智能分析",
    description: "强大的分析工具，深入洞察数据价值",
    icon: "📊",
  },
  {
    title: "安全可靠",
    description: "企业级安全保障，确保数据安全",
    icon: "🔒",
  },
]);
</script>

<template>
  <div class="home">
    <!-- Hero Section -->
    <section class="hero">
      <div class="hero-content">
        <h1>Chopone</h1>
        <p class="hero-subtitle">专业的数据处理与分析平台</p>
        <div class="hero-actions">
          <button class="btn primary">开始使用</button>
          <button class="btn secondary">了解更多</button>
        </div>
      </div>
    </section>

    <!-- Features Section -->
    <section class="features">
      <h2>核心功能</h2>
      <div class="features-grid">
        <div
          v-for="feature in features"
          :key="feature.title"
          class="feature-card"
        >
          <div class="feature-icon">{{ feature.icon }}</div>
          <h3>{{ feature.title }}</h3>
          <p>{{ feature.description }}</p>
        </div>
      </div>
    </section>

    <!-- Call to Action -->
    <section class="cta">
      <div class="cta-content">
        <h2>准备好开始了吗？</h2>
        <p>立即体验Chopone的强大功能</p>
        <button class="btn primary">免费试用</button>
      </div>
    </section>
  </div>
</template>

<style scoped>
.home {
  padding-top: 56px; /* 修正为header的实际高度 */
  color: #333;
}

.hero {
  background: linear-gradient(135deg, #1a237e, #0d47a1);
  color: white;
  padding: 6rem 2rem;
  text-align: center;
}

.hero-content {
  max-width: 800px;
  margin: 0 auto;
}

.hero h1 {
  font-size: 3.5rem;
  margin-bottom: 1rem;
}

.hero-subtitle {
  font-size: 1.5rem;
  margin-bottom: 2rem;
  opacity: 0.9;
}

.hero-actions {
  display: flex;
  gap: 1rem;
  justify-content: center;
}

.btn {
  padding: 0.8rem 2rem;
  border-radius: 4px;
  font-size: 1.1rem;
  cursor: pointer;
  transition: all 0.3s;
  border: none;
}

.btn.primary {
  background-color: #1a237e;
  color: white;
}

.btn.primary:hover {
  background-color: #0d47a1;
  transform: translateY(-2px);
}

.btn.secondary {
  background-color: transparent;
  border: 2px solid #1a237e;
  color: #1a237e;
}

.btn.secondary:hover {
  background-color: rgba(26, 35, 126, 0.1);
  transform: translateY(-2px);
}

.features {
  padding: 4rem 2rem;
  background-color: #fff;
}

.features h2 {
  text-align: center;
  color: #1a237e;
  margin-bottom: 3rem;
  font-size: 2.5rem;
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 2rem;
  max-width: 1200px;
  margin: 0 auto;
}

.feature-card {
  background: white;
  padding: 2rem;
  border-radius: 8px;
  text-align: center;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s;
  border: 1px solid #eee;
}

.feature-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 12px rgba(0, 0, 0, 0.15);
}

.feature-icon {
  font-size: 2.5rem;
  margin-bottom: 1rem;
  color: #1a237e;
}

.feature-card h3 {
  color: #1a237e;
  margin-bottom: 1rem;
}

.feature-card p {
  color: #666;
}

.cta {
  padding: 6rem 2rem;
  text-align: center;
  background: #f5f5f5;
  color: #333;
}

.cta-content {
  max-width: 600px;
  margin: 0 auto;
}

.cta h2 {
  font-size: 2.5rem;
  margin-bottom: 1rem;
  color: #1a237e;
}

.cta p {
  font-size: 1.2rem;
  margin-bottom: 2rem;
  color: #666;
}
</style>
