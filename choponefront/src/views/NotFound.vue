<template>
  <div class="not-found">
    <div class="content">
      <h1>404</h1>
      <p>抱歉，您访问的页面不存在</p>
      <router-link to="/" class="btn">返回首页</router-link>
    </div>
  </div>
</template>

<style scoped>
.not-found {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 2rem;
  text-align: center;
  background-color: #f5f5f5;
}

.content {
  max-width: 600px;
}

h1 {
  font-size: 6rem;
  color: #1a237e;
  margin-bottom: 1rem;
}

p {
  font-size: 1.5rem;
  color: #666;
  margin-bottom: 2rem;
}

.btn {
  display: inline-block;
  padding: 0.8rem 2rem;
  background-color: #1a237e;
  color: white;
  text-decoration: none;
  border-radius: 4px;
  transition: all 0.3s;
}

.btn:hover {
  background-color: #0d47a1;
  transform: translateY(-2px);
}
</style>
