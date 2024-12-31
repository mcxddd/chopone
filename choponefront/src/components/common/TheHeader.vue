<script setup lang="ts">
import { ref } from "vue";

const menuItems = ref([
  { name: "首页", path: "/" },
  { name: "小工具", path: "/tools" },
  { name: "关于", path: "/404" },
]);

const isSidebarOpen = ref(false);

const toggleSidebar = () => {
  isSidebarOpen.value = !isSidebarOpen.value;
};
</script>

<template>
  <header class="header">
    <div class="header-content">
      <!-- Hamburger Menu Button -->
      <button class="hamburger-btn" @click="toggleSidebar">
        <span class="hamburger-icon"></span>
      </button>

      <div class="logo-container">
        <router-link to="/" class="logo">CHOPONE</router-link>
      </div>

      <!-- Desktop Navigation -->
      <nav class="navigation desktop-nav">
        <ul class="nav-list">
          <li v-for="item in menuItems" :key="item.path" class="nav-item">
            <router-link :to="item.path" class="nav-link">{{
              item.name
            }}</router-link>
          </li>
        </ul>
      </nav>

      <!-- Mobile Sidebar -->
      <div
        class="sidebar-overlay"
        v-if="isSidebarOpen"
        @click="toggleSidebar"
      ></div>
      <nav class="sidebar" :class="{ 'sidebar-open': isSidebarOpen }">
        <ul class="sidebar-nav-list">
          <li
            v-for="item in menuItems"
            :key="item.path"
            class="sidebar-nav-item"
          >
            <router-link
              :to="item.path"
              class="sidebar-nav-link"
              @click="toggleSidebar"
            >
              {{ item.name }}
            </router-link>
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
  background: linear-gradient(120deg, #1e1e1e 0%, #2d3436 100%);
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
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
  color: #e2e8f0;
  font-size: 1.5rem;
  font-weight: 700;
  letter-spacing: 2px;
  text-decoration: none;
  padding: 0.5rem;
  border-radius: 4px;
  transition: all 0.3s;
}

.logo:hover {
  background: rgba(99, 102, 241, 0.1);
}

/* Desktop Navigation */
.desktop-nav {
  display: flex;
}

.nav-list {
  display: flex;
  gap: 2rem;
  list-style: none;
}

.nav-link {
  color: #e2e8f0;
  font-size: 1rem;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  transition: all 0.3s;
  position: relative;
  text-decoration: none;
}

.nav-link::after {
  content: "";
  position: absolute;
  bottom: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 0;
  height: 2px;
  background: #6366f1;
  transition: width 0.3s;
}

.nav-link:hover::after {
  width: 80%;
}

.router-link-active::after {
  width: 80%;
}

/* Hamburger Button */
.hamburger-btn {
  display: none;
  background: none;
  border: none;
  cursor: pointer;
  padding: 0.5rem;
  z-index: 102;
  transition: transform 0.3s ease;
}

.hamburger-icon {
  display: block;
  width: 20px;
  height: 2px;
  background: #e2e8f0;
  position: relative;
  transition: all 0.3s ease;
}

.hamburger-icon::before,
.hamburger-icon::after {
  content: "";
  position: absolute;
  width: 20px;
  height: 2px;
  background: #e2e8f0;
  transition: all 0.3s ease;
}

.hamburger-icon::before {
  top: -6px;
}

.hamburger-icon::after {
  bottom: -6px;
}

/* Hamburger Animation when sidebar is open */
.sidebar-open ~ .hamburger-btn .hamburger-icon {
  background: transparent;
}

.sidebar-open ~ .hamburger-btn .hamburger-icon::before {
  transform: rotate(45deg);
  top: 0;
}

.sidebar-open ~ .hamburger-btn .hamburger-icon::after {
  transform: rotate(-45deg);
  bottom: 0;
}

/* Sidebar */
.sidebar {
  position: fixed;
  top: 0;
  left: -140px;
  width: 140px;
  height: 100vh;
  background: linear-gradient(120deg, #1e1e1e 0%, #2d3436 100%);
  z-index: 101;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  padding-top: 56px;
  box-shadow: 2px 0 8px rgba(0, 0, 0, 0.3);
}

.sidebar-open {
  transform: translateX(140px);
}

.sidebar-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
  z-index: 100;
  opacity: 0;
  transition: opacity 0.3s ease;
}

.sidebar-overlay[v-if] {
  opacity: 1;
}

.sidebar-nav-list {
  list-style: none;
  padding: 0.6rem;
}

.sidebar-nav-item {
  margin: 0.4rem 0;
}

.sidebar-nav-link {
  color: #e2e8f0;
  text-decoration: none;
  font-size: 0.95rem;
  display: block;
  padding: 0.7rem 0.8rem;
  border-radius: 4px;
  transition: all 0.2s ease;
}

.sidebar-nav-link:hover {
  background: rgba(99, 102, 241, 0.1);
  transform: translateX(4px);
}

/* Mobile Responsive */
@media (max-width: 768px) {
  .desktop-nav {
    display: none;
  }

  .hamburger-btn {
    display: block;
  }

  .header-content {
    padding: 0 1rem;
  }
}
</style>
