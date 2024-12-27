<script setup lang="ts">
import { ref } from "vue";

const menuItems = ref([
  { name: "首页", path: "/" },
  { name: "数据处理", path: "/404" },
  { name: "关于我们", path: "/404" },
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
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  height: 56px;
  z-index: 100;
}

.header-content {
  height: 100%;
  padding: 0 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.logo-container {
  height: 100%;
  display: flex;
  align-items: center;
}

.logo {
  height: 36px;
  width: auto;
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
  transition: background-color 0.3s;
}

.nav-link:hover {
  background-color: rgba(255, 255, 255, 0.1);
}

.router-link-active {
  background-color: rgba(255, 255, 255, 0.1);
}
</style>
