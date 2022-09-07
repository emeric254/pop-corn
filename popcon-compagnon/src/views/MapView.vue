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
    "$route.params.zone": {
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
          params: {
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
     * Opens the popup with the information from the parameters.
     * @param {String} oldZone The name of the zone that was previously selected.
     */
    openZonePopup(oldZone) {
      const zoneName = this.$route.params.zone;

      // Zone previously selected, unselect it.
      if (oldZone) {
        const zonePath = this.getZonePath(oldZone);
        if (zonePath) {
          zonePath.classList.remove("selected");
        }
      }

      if (zoneName) {
        const zoneData = this.mapData[zoneName];

        if (zoneData) {
          const zonePath = this.getZonePath(zoneName);
          if (zonePath) {
            zonePath.classList.add("selected");
          }
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
  cursor: pointer;
  fill: transparent;
  stroke: none;
  transition: fill 0.2s ease;
}

:deep() .mapsvg path:hover {
  stroke: black;
  stroke-width: 2px;
  stroke-linecap: butt;

  fill: rgba(129, 236, 236, 0.3);

  filter: drop-shadow(0px 0px 16px rgba(0, 0, 0, 0.4));
}

:deep() .mapsvg path.selected {
  stroke: black;
  stroke-width: 2px;

  fill: rgba(0, 255, 55, 0.3);

  filter: drop-shadow(0px 0px 16px rgba(0, 0, 0, 0.4));
}
</style>
