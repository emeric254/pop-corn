<template>
  <div
    class="flex flex-col content-evenly place-content-center h-screen w-full max-w-full"
  >
    <h1 class="text-center pt-4 text-xl">Edition du Planning</h1>
    <textarea
      :disabled="chargement || !texte"
      :readonly="enregistrement"
      v-model="texte"
      class="m-4 border rounded flex-grow disabled:cursor-not-allowed"
    ></textarea>
    <div class="flex content-around justify-around pb-2">
      <button
        @click="recharger"
        :disabled="enregistrement || chargement"
        class="py-2 px-4 border rounded-lg bg-red-300 disabled:cursor-not-allowed"
      >
        <LoadingSpinner v-if="chargement" />
        Recharger
      </button>
      <button
        @click="sauvegarder"
        :disabled="enregistrement || chargement || !texte"
        class="py-2 px-4 border rounded-lg bg-green-300 disabled:cursor-not-allowed"
      >
        <LoadingSpinner v-if="enregistrement" />
        Enregistrer
      </button>
    </div>
  </div>
</template>

<script>
import { usePlanningStore } from "@/stores/planning.js";
import { useLoginStore } from "@/stores/login.js";
import { mapStores } from "pinia";
import LoadingSpinner from "../components/LoadingSpinner.vue";

export default {
  components: {
    LoadingSpinner,
  },

  data() {
    return {
      chargement: false,
      enregistrement: false,
      texte: "",
    };
  },

  computed: {
    ...mapStores(usePlanningStore),
    ...mapStores(useLoginStore),
  },

  mounted() {
    if (!this.loginStore.loggedIn) {
      this.$router.push("/");
      return;
    }

    this.recharger();
  },

  methods: {
    recharger() {
      this.chargement = true;
      this.planningStore.charger().then(() => {
        this.texte = JSON.stringify(
          this.planningStore.planning.activites,
          null,
          8
        );
        this.chargement = false;
      });
    },
    sauvegarder() {
      this.enregistrement = true;
      this.planningStore.planning.activites = JSON.parse(this.texte);
      this.planningStore
        .enregistrer()
        .then(() => (this.enregistrement = false));
    },
  },
};
</script>
