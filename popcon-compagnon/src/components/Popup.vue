<template>
  <Transition name="fade">
    <div
      v-if="popupStore.isVisible"
      class="fixed top-0 left-0 w-full h-full flex justify-center items-center bg-popup-mask"
    >
      <div class="rounded-xl bg-white shadow-lg relative overflow-hidden">
        <div class="bg-sky-50 flex items-center justify-between p-3">
          <h3 class="text-popcon-blue font-bold">{{ popupStore.title }}</h3>
          <button
            @click="hidePopup"
            title="Fermer"
            class="w-5 h-5 pb-0.5 flex justify-center items-center border-2 border-solid border-popcon-orange rounded-full text-popcon-orange hover:text-popcon-green hover:border-popcon-green transition-colors duration-200"
          >&times;</button>
        </div>

        <p class="text-gray-700 p-3">{{ popupStore.body }}</p>
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
