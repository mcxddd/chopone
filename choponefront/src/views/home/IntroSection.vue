<template>
  <section class="intro">
    <div class="intro-content">
      <h1>Chopone</h1>
      <p class="description">一个小工具集合</p>
      <p class="status">其他功能正在开发中...</p>
    </div>
  </section>
</template>

<style scoped>
.intro {
  background: linear-gradient(120deg, #1a1a1a 0%, #2d3436 100%);
  min-height: calc(100vh - 56px - 52px); /* viewport height - header - footer */
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 2rem;
  text-align: center;
  color: #e2e8f0;
  position: relative;
  overflow: hidden;
}

.intro::before {
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

.intro-content {
  max-width: 600px;
  position: relative;
  z-index: 1;
}

h1 {
  font-size: 3.5rem;
  margin-bottom: 1.5rem;
  font-weight: 600;
  background: linear-gradient(120deg, #6366f1 0%, #a855f7 100%);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}

.description {
  font-size: 1.5rem;
  margin-bottom: 1rem;
  color: #e2e8f0;
  opacity: 0.9;
}

.status {
  font-size: 1.1rem;
  color: #94a3b8;
  opacity: 0.9;
}

@media (max-width: 768px) {
  h1 {
    font-size: 2.5rem;
  }

  .description {
    font-size: 1.2rem;
  }

  .status {
    font-size: 1rem;
  }
}
</style>
