<script setup lang="ts">
import { ref } from "vue";
import { useRouter } from "vue-router";

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
  <van-tabbar v-model="active" @change="onChange">
    <van-tabbar-item icon="friends-o">功能1</van-tabbar-item>
    <van-tabbar-item icon="comment-o">功能2</van-tabbar-item>
    <van-tabbar-item icon="home-o">主页</van-tabbar-item>
    <van-tabbar-item icon="search">功能4</van-tabbar-item>
    <van-tabbar-item icon="setting-o">设置</van-tabbar-item>
  </van-tabbar>
</template>
