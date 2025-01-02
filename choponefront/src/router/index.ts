import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/home/Home.vue";
import NotFound from "../views/NotFound.vue";
import Tools from "../views/tools/ToolsView.vue";
import PdfCompress from "../views/tools/pdf-compress/PdfCompressView.vue";
import AiChat from "../views/aichat/AiChat.vue";

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
      path: "/aichat",
      name: "aichat",
      component: AiChat,
    },
    {
      path: "/:pathMatch(.*)*",
      name: "not-found",
      component: NotFound,
    },
  ],
});

export default router;
