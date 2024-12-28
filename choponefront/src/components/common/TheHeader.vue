<script setup lang="ts">
import { ref } from "vue";

const menuItems = ref([
  { name: "首页", path: "/" },
  { name: "小工具", path: "/tools" },
  { name: "关于我们", path: "/404" },
]);
</script>

<template>
  <header class="header">
    <div class="header-content">
      <div class="logo-container">
        <router-link to="/" class="logo">CHOPONE</router-link>
      </div>
      <nav class="navigation">
        <ul class="nav-list">
          <li v-for="item in menuItems" :key="item.path" class="nav-item">
            <router-link :to="item.path" class="nav-link">{{
              item.name
            }}</router-link>
          </li>
        </ul>
      </nav>
    </div>
  </header>
</template>

<style scoped>
.header {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  height: 56px;
  z-index: 100;
  background: linear-gradient(120deg, #2c3e50 0%, #3498db 100%);
}

.header-content {
  height: 100%;
  padding: 0 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  position: relative;
}

.logo-container {
  height: 100%;
  display: flex;
  align-items: center;
}

.logo {
  color: white;
  font-size: 1.5rem;
  font-weight: 700;
  letter-spacing: 2px;
  text-decoration: none;
  padding: 0.5rem;
  border-radius: 4px;
  transition: all 0.3s;
}

.logo:hover {
  background: rgba(255, 255, 255, 0.1);
}

.nav-list {
  display: flex;
  gap: 2rem;
  list-style: none;
}

.nav-link {
  color: white;
  font-size: 1rem;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  transition: all 0.3s;
  position: relative;
}

.nav-link::after {
  content: "";
  position: absolute;
  bottom: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 0;
  height: 2px;
  background: white;
  transition: width 0.3s;
}

.nav-link:hover::after {
  width: 80%;
}

.router-link-active::after {
  width: 80%;
}
</style>
