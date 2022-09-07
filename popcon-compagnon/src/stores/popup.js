import { defineStore } from "pinia";

export const usePopupStore = defineStore({
  id: "popup",
  state: () => ({
    isVisible: false,
    title: "",
    body: "",
  }),

  actions: {
    show(newTitle, newBody) {
      this.isVisible = true;
      this.title = newTitle;
      this.body = newBody;
    },

    hide() {
      this.isVisible = false;
    },
  },
});
