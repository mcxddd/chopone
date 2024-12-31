<template>
  <div class="not-found">
    <div class="content">
      <div class="error-code">404</div>
      <div class="error-text">
        <div class="message">抱歉，页面走丢了</div>
        <p class="description">您访问的页面可能已被移除或暂时无法访问</p>
      </div>
      <div class="buttons">
        <button @click="goBack" class="back-btn">
          <span class="icon">←</span>
          <span>返回上一页</span>
        </button>
        <router-link to="/" class="home-btn">
          <span class="icon">⌂</span>
          <span>返回首页</span>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useRouter } from "vue-router";

const router = useRouter();
const goBack = () => router.back();
</script>

<style scoped>
.not-found {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 2rem;
  text-align: center;
  background: linear-gradient(135deg, #1a1a1a 0%, #2d3436 100%);
  font-family: system-ui, -apple-system, sans-serif;
}

.content {
  max-width: 600px;
  padding: 3rem;
  background: rgba(30, 30, 30, 0.95);
  border-radius: 20px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
  animation: fadeIn 0.6s ease-out;
}

.error-code {
  font-size: 8rem;
  font-weight: 700;
  background: linear-gradient(120deg, #6366f1 0%, #a855f7 100%);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  line-height: 1;
  margin-bottom: 1.5rem;
  animation: scaleIn 0.5s ease-out;
}

.error-text {
  margin-bottom: 2rem;
}

.message {
  font-size: 2rem;
  color: #ffffff;
  font-weight: 600;
  margin-bottom: 0.5rem;
}

.description {
  font-size: 1.1rem;
  color: #b3b3b3;
  margin: 0;
}

.buttons {
  display: flex;
  gap: 1rem;
  justify-content: center;
  flex-wrap: wrap;
}

.back-btn,
.home-btn {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.8rem 2rem;
  color: white;
  text-decoration: none;
  border-radius: 50px;
  font-weight: 500;
  transition: all 0.3s ease;
  box-shadow: 0 4px 15px rgba(99, 102, 241, 0.2);
  font-size: 1rem;
}

.back-btn {
  background: linear-gradient(120deg, #3730a3 0%, #6366f1 100%);
  border: none;
  cursor: pointer;
}

.home-btn {
  background: linear-gradient(120deg, #6366f1 0%, #a855f7 100%);
}

.back-btn:hover,
.home-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(99, 102, 241, 0.3);
}

.back-btn:active,
.home-btn:active {
  transform: translateY(0);
}

.icon {
  font-size: 1.2rem;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes scaleIn {
  from {
    transform: scale(0.8);
    opacity: 0;
  }
  to {
    transform: scale(1);
    opacity: 1;
  }
}

/* Mobile Responsive */
@media (max-width: 768px) {
  .content {
    padding: 2rem;
    margin: 1rem;
  }

  .error-code {
    font-size: 6rem;
  }

  .message {
    font-size: 1.5rem;
  }

  .description {
    font-size: 1rem;
  }

  .buttons {
    flex-direction: column;
  }

  .back-btn,
  .home-btn {
    width: 100%;
    justify-content: center;
  }
}
</style>
