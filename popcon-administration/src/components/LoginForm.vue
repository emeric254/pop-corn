<template>
  <form
    @submit.prevent="onSubmit"
    class="flex flex-col w-80 shadow-lg rounded-lg"
  >
    <input
      class="p-2 border border-slate-400 rounded-t-lg"
      v-model="email"
      type="email"
      placeholder="E-mail…"
      required
    />
    <input
      class="p-2 border-x border-b border-slate-400"
      v-model="password"
      type="password"
      placeholder="Mot de passe…"
      required
    />
    <button
      :disabled="loading"
      class="p-2 rounded-b-lg bg-emerald-300 text-white font-bold uppercase cursor-pointer disabled:opacity-50 transition-opacity delay-300"
      type="submit"
    >Connexion</button>
  </form>
</template>

<script>
import { useLoginStore } from '@/stores/login.js'
import { mapStores } from 'pinia'

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
    onSubmit () {
      this.loading = true;
      setTimeout(() => {
        this.loginStore.login();
      }, 2000);
    }
  }
}
</script>
