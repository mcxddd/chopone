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
  background: linear-gradient(120deg, #2c3e50 0%, #3498db 100%);
  min-height: calc(100vh - 56px - 52px); /* viewport height - header - footer */
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 2rem;
  text-align: center;
  color: white;
}

.intro-content {
  max-width: 600px;
}

h1 {
  font-size: 3.5rem;
  margin-bottom: 1.5rem;
  font-weight: 600;
}

.description {
  font-size: 1.5rem;
  margin-bottom: 1rem;
  opacity: 0.9;
}

.status {
  font-size: 1.1rem;
  opacity: 0.7;
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
