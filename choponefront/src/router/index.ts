import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: "/",
      name: "home",
      component: Home,
    },
    {
      path: "/process",
      name: "process",
      component: () => import("../views/Process.vue"),
    },
    {
      path: "/analysis",
      name: "analysis",
      component: () => import("../views/Analysis.vue"),
    },
    {
      path: "/about",
      name: "about",
      component: () => import("../views/About.vue"),
    },
    {
      path: "/docs",
      name: "docs",
      component: () => import("../views/Docs.vue"),
    },
    {
      path: "/support",
      name: "support",
      component: () => import("../views/Support.vue"),
    },
    {
      path: "/privacy",
      name: "privacy",
      component: () => import("../views/Privacy.vue"),
    },
    {
      path: "/:pathMatch(.*)*",
      name: "not-found",
      component: () => import("../views/NotFound.vue"),
    },
  ],
});

export default router;
