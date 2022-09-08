import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import CarteView from "../views/CarteView.vue";
import PlanningView from "../views/PlanningView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
    },
    {
      path: "/carte",
      name: "carte",
      component: CarteView,
    },
    {
      path: "/planning",
      name: "planning",
      component: PlanningView,
    },
  ],
});

export default router;
