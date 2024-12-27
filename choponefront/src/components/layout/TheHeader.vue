<script setup lang="ts">
import { ref } from "vue";

const menuItems = ref([
  { name: "首页", path: "/" },
  { name: "数据处理", path: "/process" },
  { name: "分析工具", path: "/analysis" },
  { name: "关于我们", path: "/about" },
]);
</script>

<template>
  <header class="header">
    <div class="header-content">
      <div class="logo-container">
        <img src="@/assets/full_logo.png" alt="Chopone Logo" class="logo" />
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
  background: linear-gradient(135deg, #1a237e, #0d47a1);
  padding: 0.75rem 0;
  position: fixed;
  width: 100vw;
  left: 0;
  top: 0;
  z-index: 100;
  height: 56px;
}

.header-content {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.logo-container {
  display: flex;
  align-items: center;
}

.logo {
  height: 36px;
  width: auto;
}

.navigation {
  flex: 1;
  display: flex;
  justify-content: flex-end;
}

.nav-list {
  list-style: none;
  display: flex;
  gap: 2rem;
  margin: 0;
  padding: 0;
}

.nav-link {
  color: white;
  text-decoration: none;
  font-size: 1.1rem;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  transition: background-color 0.3s;
}

.nav-link:hover {
  background-color: rgba(255, 255, 255, 0.1);
}
</style>
