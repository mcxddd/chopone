<script setup lang="ts">
import { ref } from "vue";
import { useRouter } from "vue-router";
import TabBar from "./components/TabBar.vue";

const router = useRouter();
const active = ref(0);

const onChange = (index: number) => {
  switch (index) {
    case 0:
      router.push("/placeholder1");
      break;
    case 1:
      router.push("/placeholder2");
      break;
    case 2:
      router.push("/home");
      break;
    case 3:
      router.push("/placeholder3");
      break;
    case 4:
      router.push("/settings");
      break;
  }
};
</script>

<template>
  <router-view />
  <TabBar />
</template>
