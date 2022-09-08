<template>
  <main
    class="container mx-auto flex flex-col content-around place-content-evenly h-screen w-full max-w-full"
  >
    <div class="flex justify-center">
      <a href="popcon.show">
        <img src="@/assets/popcon.png" />
      </a>
    </div>
    <div
      class="flex flex-col lg:flex-row items-center justify-evenly pt-4 gap-8"
    >
      <router-link to="/map" v-slot="{ carte }">
        <button
          class="px-12 py-4 rounded-lg text-xl cursor-pointer border-2 border-solid border-popcon-orange text-popcon-orange hover:text-popcon-green hover:border-popcon-green active:bg-gree-700 focus:outline-none focus:ring focus:ring-green-300 transition-colors duration-200"
          @click="carte"
        >
          Carte du salon
        </button>
      </router-link>
      <router-link to="/planning" v-slot="{ planning }">
        <button
          class="px-12 py-4 rounded-lg text-xl cursor-pointer border-2 border-solid border-popcon-orange text-popcon-orange hover:text-popcon-green hover:border-popcon-green active:bg-green-700 focus:outline-none focus:ring focus:ring-green-300 transition-colors duration-200"
          @click="planning"
        >
          Planning des activités
        </button>
      </router-link>
    </div>
  </main>
</template>

<script>
export default {
  data() {
    return {
      titre: "PopCon " + new Date().getFullYear(),
    };
  },
};
</script>

<style scoped>
h1 {
  text-align: center;
}
img {
  max-width: 155px;
  height: auto;
}
</style>
