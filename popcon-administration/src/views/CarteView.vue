<template>
  <div
    class="flex flex-col content-evenly place-content-center h-screen w-full max-w-full"
  >
    <h1 class="text-center pt-4 text-xl">Edition de la Carte</h1>
    <textarea
      :disabled="chargement || !carteStore.carte"
      :readonly="enregistrement"
      model="carteStore.carte.activite"
      class="m-4 border rounded flex-grow disabled:cursor-not-allowed"
    ></textarea>
    <div class="flex content-around justify-around pb-2">
      <button
        :disabled="enregistrement || chargement"
        class="py-2 px-4 border rounded-lg bg-red-300 disabled:cursor-not-allowed"
      >
        <LoadingSpinner v-if="chargement" />
        Recharger
      </button>
      <button
        :disabled="enregistrement || chargement || !carteStore.carte"
        class="py-2 px-4 border rounded-lg bg-green-300 disabled:cursor-not-allowed"
      >
        <LoadingSpinner v-if="enregistrement" />
        Enregistrer
      </button>
    </div>
  </div>
</template>

<script>
import { useCarteStore } from "@/stores/carte.js";
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
    };
  },

  computed: {
    ...mapStores(useCarteStore),
  },

  mounted() {
    this.chargement = true;
  },

  methods: {},
};
</script>
