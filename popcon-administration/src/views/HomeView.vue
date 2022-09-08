<template>
  <main
    class="container mx-auto flex flex-col content-around place-content-center h-screen w-full max-w-full"
  >
    <div class="flex justify-center pb-2">
      <img src="@/assets/popcon.png" />
    </div>
    <p class="text-center pb-12">Administration</p>
    <LoginForm v-if="!loginStore.loggedIn" />
    <HomeButtons v-else />
  </main>
</template>

<script>
import { useLoginStore } from "@/stores/login.js";
import { mapStores } from "pinia";
import LoginForm from "../components/LoginForm.vue";
import HomeButtons from "../components/HomeButtons.vue";

export default {
  components: {
    LoginForm,
    HomeButtons,
  },

  computed: {
    ...mapStores(useLoginStore),
  },

  methods: {},
};
</script>
