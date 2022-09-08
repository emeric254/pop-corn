<script setup>
import LoadingSpinner from "../components/LoadingSpinner.vue";
</script>

<template>
  <div class="flex flex-col items-center">
    <form
      @submit.prevent="onSubmit"
      class="flex flex-col w-80 rounded-lg gap-2"
    >
      <input
        class="p-2 border border-slate-400 rounded-lg"
        v-model="email"
        type="email"
        placeholder="Identifiant …"
        required
      />
      <input
        class="p-2 border rounded-lg border-slate-400"
        v-model="password"
        type="password"
        placeholder="Mot de passe …"
        required
      />
      <button
        :disabled="loading"
        class="p-2 rounded-lg bg-emerald-300 text-white font-bold uppercase cursor-pointer disabled:cursor-not-allowed transition-opacity delay-300 hover:bg-emeral-100 active:bg-green-700 focus:outline-none focus:ring focus:ring-green-300 transition-colors duration-200 hover:text-popcon-green hover:border-popcon-green active:bg-green-700 focus:outline-none focus:ring focus:ring-green-300"
        type="submit"
      >
        <LoadingSpinner v-if="loading" />
        Connexion
      </button>
    </form>
  </div>
</template>

<script>
import { useLoginStore } from "@/stores/login.js";
import { mapStores } from "pinia";

export default {
  data: () => ({
    email: "",
    password: "",
    loading: false,
  }),

  computed: {
    ...mapStores(useLoginStore),
  },

  methods: {
    onSubmit() {
      this.loading = true;
      this.loginStore
        .connexion(this.email, this.password)
        .then(() => (this.loading = false));
    },
  },
};
</script>
