import { defineStore } from "pinia";

export const useCarteStore = defineStore({
  id: "carte",
  state: () => ({
    carte: null,
  }),
  actions: {
    charger() {
      this.carte = {
        activites: [],
      };

      // TODO request popcon-organisation server to get /carte
    },
    enregistrer() {
      // TODO request popcon-organisation server to post /carte
    }
  },
});
