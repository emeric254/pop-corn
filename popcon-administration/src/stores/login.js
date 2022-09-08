import { defineStore } from "pinia";

export const useLoginStore = defineStore({
  id: "login",
  state: () => ({
    loggedIn: false,
  }),
  actions: {
    login() {
      this.loggedIn = true;
    },
  },
});
