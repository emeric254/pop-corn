import { defineStore } from "pinia";
import { useLoginStore } from "./login";

export const useCarteStore = defineStore({
  id: "carte",
  state: () => ({
    carte: { zones: [] },
  }),
  actions: {
    async charger() {
      const login = useLoginStore();

      const r = await fetch("/api/carte/zones", {
        headers: { Authorization: "Bearer " + login.token },
      });

      this.carte = await r.json();

      if (!this.carte || !this.carte.zones) {
        this.carte = { zones: [] };
      }
    },
    async enregistrer() {
      const login = useLoginStore();

      console.log(this.carte);

      const r = await fetch("/api/carte/zones", {
        method: "PUT",
        headers: { Authorization: "Bearer " + login.token,
          Accept: "application/json",
          "Content-Type": "application/json",
        },
        body: JSON.stringify(this.carte),
      });

      console.log(r.json());
    },
  },
});
