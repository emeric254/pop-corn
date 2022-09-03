<template>
  <Transition name="fade">
    <div
      v-if="popupStore.isVisible"
      class="fixed top-0 left-0 w-full h-full flex justify-center items-center bg-popup-mask"
    >
      <div class="p-4 rounded-xl bg-white shadow-lg relative">
        <button
          @click="hidePopup"
          title="Fermer"
          class="w-5 h-5 flex justify-center items-center border border-solid border-gray-900 rounded-full absolute top-3 right-3"
        >&times;</button>
        <h3>{{ popupStore.title }}</h3>
        <p>{{ popupStore.body }}</p>
      </div>
    </div>
  </Transition>
</template>

<script>
import { mapStores } from 'pinia';
import { usePopupStore } from '@/stores/popup';

export default {
  computed: {
    ...mapStores(usePopupStore)
  },

  methods: {
    hidePopup () {
      this.popupStore.hide();
      this.$router.replace("/map");
    },

    listenEscKey (event) {
      if (event.key === 'Escape') {
        this.hidePopup();
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

<style>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
