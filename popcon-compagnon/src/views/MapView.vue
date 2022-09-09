<template>
  <div class="flex justify-center">
    <div class="relative">
      <img src="@/assets/map.jpg" />
      <div
        v-if="isLoading"
        class="flex justify-center items-center absolute top-0 left-0 w-full h-full"
      >
        Loading…
      </div>
      <MapSvg
        class="absolute top-0 left-0 w-full h-full mapsvg"
        @mousedown="onMapClick"
      />
    </div>
  </div>
</template>

<script>
import MapSvg from "@/assets/map.svg";
import { mapStores } from "pinia";
import { usePopupStore } from "@/stores/popup";

export default {
  components: {
    MapSvg,
  },

  data() {
    return {
      mapData: {},
      isLoading: true,
    };
  },

  computed: {
    ...mapStores(usePopupStore),
  },

  watch: {
    "$route.query.zone": {
      handler(_, oldZone) {
        this.openZonePopup(oldZone);
      },
    },
  },

  methods: {
    onMapClick(event) {
      const zone = event.target;
      const zoneName = zone.getAttribute("id");

      if (zoneName !== null) {
        this.$router.push({
          name: "map",
          query: {
            zone: zoneName,
          },
        });
      }
    },

    getZonePath(zoneName) {
      return document.querySelector('path[id="' + zoneName + '"]');
    },

    async fetchData() {
      const body = await fetch("/donnees/carte.json");
      const data = await body.json();
      this.mapData = data.zones;
      this.isLoading = false;
    },

    /**
     * Opens the popup with the information from the query parameters.
     * @param {String} oldZone The name of the zone that was previously selected.
     */
    openZonePopup(oldZone) {
      const zoneName = this.$route.query.zone;

      // Zone previously selected, unselect it.
      if (oldZone) {
        const zonePath = this.getZonePath(oldZone);
        if (zonePath) {
          zonePath.classList.remove("selected");
        }
      }

      if (zoneName) {
        const zonePath = this.getZonePath(zoneName);
        if (zonePath) {
          zonePath.classList.add("selected");

          // mettre l'element au milieu de l'ecran
          zonePath.scrollIntoView({
            behavior: "smooth",
            block: "center",
            inline: "nearest",
          });
        }

        const zoneData = this.mapData[zoneName];
        if (zoneData) {
          this.popupStore.show(zoneData.nom, zoneData.description);
        }
      }
    },
  },

  async created() {
    await this.fetchData();
    this.openZonePopup();
  },

  unmounted() {
    this.popupStore.hide();
  },
};
</script>

<style scoped>
.mapsvg {
  pointer-events: fill;
}

:deep() .mapsvg path {
  fill: transparent;
  stroke: none;
  transition: fill 0.2s ease;

  @apply cursor-pointer;
}

:deep() .mapsvg path:hover {
  stroke-linecap: butt;

  fill: rgba(129, 236, 236, 0.3);

  filter: drop-shadow(0px 0px 24px rgba(0, 0, 0, 0.5));

  @apply stroke-2 stroke-black;
}

:deep() .mapsvg path.selected {
  fill: rgba(60, 255, 128, 0.6);

  filter: drop-shadow(0px 0px 24px rgba(0, 0, 0, 0.5) blur(1px));

  @apply animate-pulse stroke-2 stroke-cyan-900;
}
</style>
