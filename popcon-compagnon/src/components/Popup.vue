<template>
  <div
    v-if="popupStore.isVisible"
    class="fixed top-0 left-0 w-full h-full flex justify-center items-center"
  >
    <div class="p-4 rounded-xl bg-white">
      <button @click="popupStore.hide">Close</button>
      <h3>{{ popupStore.title }}</h3>
      <p>{{ popupStore.body }}</p>
    </div>
  </div>
</template>

<script>
import { mapStores } from 'pinia';
import { usePopupStore } from '@/stores/popup';

export default {
  computed: {
    ...mapStores(usePopupStore)
  },

  methods: {
    listenEscKey (event) {
      if (event.key === 'Escape') {
        this.popupStore.hide();
      }
    }
  },

  mounted () {
    window.addEventListener('keydown', this.listenEscKey);
  },

  destroyed () {
    window.removeEventListener('keydown', this.listenEscKey);
  }
}
</script>

