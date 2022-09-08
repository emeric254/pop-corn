<script setup>
import { RouterLink } from "vue-router";
</script>

<template>
  <div class="flex justify-evenly pt-11">
    <router-link to="carte" v-slot="{ carte }">
      <button
        @click="carte"
        class="mr-2 px-8 h-24 bg-emerald-300 rounded-lg text-white font-bold text-2xl hover:drop-shadow-lg duration-300"
      >
        Editer la Carte
      </button>
    </router-link>
    <router-link to="planning" v-slot="{ planning }">
      <button
        @click="planning"
        class="ml-2 px-8 h-24 bg-emerald-300 rounded-lg text-white font-bold text-2xl hover:drop-shadow-lg duration-300"
      >
        Editer le Planning
      </button>
    </router-link>
  </div>
</template>
