<template>
  <main class="flex flex-1 items-center justify-center">
    <LoginForm v-if="!loginStore.loggedIn" />
  </main>
</template>

<script>
import { useLoginStore } from "@/stores/login.js";
import { mapStores } from "pinia";
import LoginForm from "../components/LoginForm.vue";

export default {
  components: {
    LoginForm,
  },

  computed: {
    ...mapStores(useLoginStore),
  },

  methods: {},
};
</script>
