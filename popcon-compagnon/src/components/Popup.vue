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
      <div
        class="rounded-xl bg-white sm:shadow-lg overflow-hidden grow md:grow-0"
      >
        <div
          class="bg-sky-50 flex items-center justify-between px-3 py-2 md:p-4"
        >
          <h3
            :style="{ 'font-size': 24 * scale + 'px' }"
            class="text-popcon-blue font-bold pr-1 md:pr-3"
          >
            {{ popupStore.title }}
          </h3>
          <button
            :style="{ 'font-size': 32 * scale + 'px' }"
            @click="hidePopup"
            title="Fermer"
            class="w-2 h-1 sm:w-3 sm:h-2 md:w-5 md:h-5 md:pb-0.5 flex justify-center items-center rounded-full text-popcon-orange hover:text-popcon-green hover:border-popcon-green transition-colors duration-200"
          >
            &times;
          </button>
        </div>

        <p
          v-if="popupStore.body"
          :style="{ 'font-size': 24 * scale + 'px' }"
          class="text-gray-700 px-2 py-1 md:p-3"
        >
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
      scale: 1,
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
      console.debug(visualViewport);

      this.top = visualViewport.pageTop;
      this.left = visualViewport.pageLeft;
      this.width = visualViewport.width;
      this.height = visualViewport.height;

      // resize texte
      this.scale = 1 / visualViewport.scale;
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
