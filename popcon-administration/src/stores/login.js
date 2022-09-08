import { defineStore } from "pinia";

export const useLoginStore = defineStore({
  id: "login",
  state: () => ({
    loggedIn: false,
  }),
  actions: {
    login() {
      this.loggedIn = true;

      // TODO request popcon-organisation server to perform a proper login
    },
  },
});
