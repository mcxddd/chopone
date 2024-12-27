<template>
  <footer class="footer">
    <router-link to="/404">文档</router-link>
    <a href="mailto:contact@chopone.com">联系我们</a>
    <span>&copy; 2023 Chopone</span>
  </footer>
</template>

<style scoped>
.footer {
  background-color: #1a237e;
  padding: 1rem;
  display: flex;
  justify-content: center;
  gap: 2rem;
  color: white;
}

a {
  color: white;
  text-decoration: none;
}

a:hover {
  color: #90caf9;
}
</style>
