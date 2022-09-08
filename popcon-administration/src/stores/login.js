import { defineStore } from "pinia";

export const useLoginStore = defineStore({
  id: "login",
  state: () => ({
    loggedIn: false,
    token: "",
  }),
  actions: {
    async connexion(email, password) {
      const form = new URLSearchParams();
      form.append("username", email);
      form.append("password", password);
      const r = await fetch("/api/jeton", {
        method: "POST",
        body: form,
      });
      const body = await r.json();

      this.token = body.access_token;

      this.loggedIn = true;

      // expire in 3600 seconds, refresh just before
      setTimeout(this.rafraichir, 3590000);
    },
    async rafraichir() {
      const r = await fetch("/api/jeton", {
        headers: { Authorization: "Bearer " + this.token },
      });
      const body = await r.json();

      this.token = body.access_token;

      // expire in 3600 seconds, refresh just before
      setTimeout(this.rafraichir, 3590000);
    },
  },
});
