<template>
  <div class="app">
    <TheHeader />
    <main class="main">
      <router-view />
    </main>
    <TheFooter />
    <Toast />
  </div>
</template>

<script setup lang="ts">
import TheHeader from "@/components/common/TheHeader.vue";
import TheFooter from "@/components/common/TheFooter.vue";
import Toast from "@/components/common/Toast.vue";
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
    Oxygen, Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
  line-height: 1.6;
  color: #e2e8f0;
  background-color: #1a1a1a;
}

.app {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  position: relative;
}

.background-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(120deg, #1a1a1a 0%, #2d3436 100%);
  opacity: 0.8;
  z-index: -1;
  clip-path: polygon(0 0, 100% 0, 100% 85%, 0 100%);
}

main {
  flex: 1;
  margin-top: 56px;
}

a {
  color: inherit;
  text-decoration: none;
}

button {
  cursor: pointer;
  border: none;
  outline: none;
  font-weight: 500;
}

h1,
h2,
h3,
h4,
h5,
h6 {
  line-height: 1.2;
  font-weight: 600;
}

.low-poly-card {
  background: #1e1e1e;
  border-radius: 12px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
  position: relative;
  overflow: hidden;
}

.low-poly-card::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 4px;
  background: linear-gradient(90deg, #6366f1, #a855f7);
}
</style>
