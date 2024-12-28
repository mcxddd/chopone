import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";
import NotFound from "../views/NotFound.vue";
import Tools from "../views/Tools.vue";
import PdfCompress from "../views/tools/PdfCompress.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: Home,
    },
    {
      path: "/tools",
      name: "tools",
      component: Tools,
    },
    {
      path: "/tools/pdf-compress",
      name: "pdf-compress",
      component: PdfCompress,
    },
    {
      path: "/:pathMatch(.*)*",
      name: "not-found",
      component: NotFound,
    },
  ],
});

export default router;
