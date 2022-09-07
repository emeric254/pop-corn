import { createRouter, createWebHistory } from "vue-router";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: () => import("../views/HomeView.vue"),
    },
    {
      path: "/map/:zone?",
      name: "map",
      component: () => import("../views/MapView.vue"),
    },
    {
      path: "/planning",
      name: "planning",
      component: () => import("../views/PlanningView.vue"),
    },
  ],
});

export default router;
