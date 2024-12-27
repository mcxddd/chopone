<template>
  <footer class="footer">
    <div class="footer-content">
      <div class="footer-sections">
        <div class="footer-section">
          <h3>联系我们</h3>
          <p>地址：中国上海</p>
          <p>邮箱：contact@chopone.com</p>
        </div>
        <div class="footer-section">
          <h3>快速链接</h3>
          <ul>
            <li><router-link to="/docs">文档</router-link></li>
            <li><router-link to="/support">技术支持</router-link></li>
            <li><router-link to="/privacy">隐私政策</router-link></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; 2023 Chopone - 专业的数据处理与分析平台</p>
      </div>
    </div>
  </footer>
</template>

<style scoped>
.footer {
  background: linear-gradient(135deg, #1a237e, #0d47a1);
  padding: 3rem 0 1.5rem;
  margin-top: auto;
  color: white;
}

.footer-content {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 2rem;
}

.footer-sections {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 2rem;
  margin-bottom: 2rem;
}

.footer-section h3 {
  color: white;
  margin-bottom: 1rem;
  font-size: 1.2rem;
}

.footer-section p {
  color: rgba(255, 255, 255, 0.8);
  margin: 0.5rem 0;
}

.footer-section ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.footer-section ul li {
  margin: 0.5rem 0;
}

.footer-section a {
  color: rgba(255, 255, 255, 0.8);
  text-decoration: none;
  transition: color 0.3s;
}

.footer-section a:hover {
  color: white;
}

.footer-bottom {
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  padding-top: 1.5rem;
  text-align: center;
  color: rgba(255, 255, 255, 0.8);
}
</style>
