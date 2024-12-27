<script setup lang="ts">
import TheHeader from "./components/layout/TheHeader.vue";
import TheFooter from "./components/layout/TheFooter.vue";
import HomePage from "./views/HomePage.vue";
</script>

<template>
  <div class="app">
    <TheHeader />
    <main class="main-content">
      <router-view v-slot="{ Component }">
        <component :is="Component" />
      </router-view>
    </main>
    <TheFooter />
  </div>
</template>

<style>
/* Reset and base styles */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
    Oxygen, Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
  line-height: 1.6;
  color: #333;
  background-color: #fff;
  margin: 0;
  padding: 0;
  overflow-x: hidden;
}

.app {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  background-color: #fff;
  width: 100%;
  overflow-x: hidden;
}

.main-content {
  flex: 1;
  background-color: #fff;
}

/* Global utility classes */
.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 2rem;
}

/* Typography */
h1,
h2,
h3,
h4,
h5,
h6 {
  line-height: 1.2;
}

a {
  color: inherit;
  text-decoration: none;
}

/* Responsive design */
@media (max-width: 768px) {
  .container {
    padding: 0 1rem;
  }
}
</style>
