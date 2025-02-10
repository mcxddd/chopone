import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import SettingsView from "../views/SettingsView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      redirect: "/home",
    },
    {
      path: "/home",
      name: "home",
      component: HomeView,
      meta: { title: "主页" },
    },
    {
      path: "/placeholder1",
      name: "placeholder1",
      component: HomeView,
      meta: { title: "功能1" },
    },
    {
      path: "/placeholder2",
      name: "placeholder2",
      component: HomeView,
      meta: { title: "功能2" },
    },
    {
      path: "/placeholder3",
      name: "placeholder3",
      component: HomeView,
      meta: { title: "功能4" },
    },
    {
      path: "/settings",
      name: "settings",
      component: SettingsView,
      meta: { title: "设置" },
    },
  ],
});

export default router;
