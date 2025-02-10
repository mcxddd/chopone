<script setup lang="ts">
import { onMounted } from "vue";
import { useUserStore } from "../stores/user";

const userStore = useUserStore();

onMounted(() => {
  userStore.fetchIp();
});
</script>

<template>
  <div class="home">
    <div class="header">
      <h2>Welcome</h2>
      <p class="subtitle">很高兴见到你</p>
    </div>
    <van-cell-group inset>
      <van-cell title="IP Address" :value="userStore.ip" />
      <van-cell
        title="Status"
        :value="userStore.isOnline ? 'Online' : 'Offline'"
      />
    </van-cell-group>
  </div>
</template>

<style lang="scss" scoped>
@use "../styles/index.scss" as *;

.home {
  padding: var(--van-padding-md);
}

.header {
  margin-bottom: var(--van-padding-md);

  h2 {
    font-size: 32px;
    margin-bottom: 8px;
    color: #{$text-color};
  }

  .subtitle {
    font-size: 16px;
    color: #{$text-color-secondary};
  }
}
</style>
