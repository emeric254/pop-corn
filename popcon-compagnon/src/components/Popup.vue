<template>
  <Transition name="fade">
    <div
      v-if="popupStore.isVisible"
      @click.self="hidePopup"
      :style="{
        top: top + 'px',
        left: left + 'px',
        width: width + 'px',
        height: height + 'px',
      }"
      class="absolute flex justify-center items-center bg-popup-mask"
    >
      <div class="rounded-xl bg-white shadow-lg relative overflow-hidden">
        <div class="bg-sky-50 flex items-center justify-between p-3">
          <h3 class="text-popcon-blue font-bold pr-2">
            {{ popupStore.title }}
          </h3>
          <button
            @click="hidePopup"
            title="Fermer"
            class="w-5 h-5 pb-0.5 flex justify-center items-center border-2 border-solid border-popcon-orange rounded-full text-popcon-orange hover:text-popcon-green hover:border-popcon-green transition-colors duration-200"
          >
            &times;
          </button>
        </div>

        <p v-if="popupStore.body" class="text-gray-700 p-3">
          {{ popupStore.body }}
        </p>
      </div>
    </div>
  </Transition>
</template>

<script>
import { mapStores } from "pinia";
import { usePopupStore } from "@/stores/popup";

export default {
  data() {
    return {
      timeout: 5,
      debounce: null,
      top: 0,
      left: 0,
      width: 0,
      height: 0,
    };
  },

  computed: {
    ...mapStores(usePopupStore),
  },

  methods: {
    hidePopup() {
      this.popupStore.hide();
    },

    listenEscKey(event) {
      if (event.key === "Escape") {
        this.hidePopup();
      }
    },

    changePosition() {
      // https://developer.mozilla.org/en-US/docs/Web/API/Visual_Viewport_API
      console.log(visualViewport);

      this.top = visualViewport.pageTop;
      this.left = visualViewport.pageLeft;
      this.width = visualViewport.width;
      this.height = visualViewport.height;
    },

    positionEvent() {
      clearTimeout(this.debounce);
      this.debounce = setTimeout(this.changePosition, this.timeout);
    },
  },

  mounted() {
    // esc
    window.addEventListener("keydown", this.listenEscKey);

    // viewport
    window.addEventListener("scroll", this.positionEvent);
    visualViewport.addEventListener("resize", this.positionEvent);
    visualViewport.addEventListener("scroll", this.positionEvent);

    // initialise la position
    this.changePosition();
  },

  unmounted() {
    // esc
    window.removeEventListener("keydown", this.listenEscKey);

    // viewport
    window.removeEventListener("scroll", this.positionEvent);
    visualViewport.removeEventListener("resize", this.positionEvent);
    visualViewport.addEventListener("scroll", this.positionEvent);
  },
};
</script>

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
