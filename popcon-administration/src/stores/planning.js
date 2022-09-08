import { defineStore } from "pinia";
import { useLoginStore } from "./login";

export const usePlanningStore = defineStore({
  id: "planning",
  state: () => ({
    planning: { activites: [] },
  }),
  actions: {
    async charger() {
      const login = useLoginStore();

      const r = await fetch("/api/planning/activites", {
        headers: { Authorization: "Bearer " + login.token },
      });

      this.planning = await r.json();

      if (!this.planning || !this.planning.activites) {
        this.planning = { activites: [] };
      }
    },
    async enregistrer() {
      const login = useLoginStore();

      console.log(this.planning);

      const r = await fetch("/api/planning/activites", {
        method: "PUT",
        headers: {
          Authorization: "Bearer " + login.token,
          Accept: "application/json",
          "Content-Type": "application/json",
        },
        body: JSON.stringify(this.planning),
      });

      console.log(await r.json());
    },
  },
});
