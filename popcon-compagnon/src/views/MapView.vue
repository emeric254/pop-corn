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
import { mapStores } from 'pinia';
import { usePopupStore } from '@/stores/popup';

export default {
  components: {
    MapSvg
  },

  data () {
    return {
      mapData: {},
      isLoading: true,
    }
  },

  computed: {
    ...mapStores(usePopupStore)
  },

  watch: {
    "$route.params.zone": {
      handler (_, oldZone) {
        this.openZonePopup(oldZone);
      }
    }
  },

  methods: {
    onMapClick (event) {
      const zone = event.target;
      const zoneName = zone.getAttribute('inkscape:label');

      if (zoneName !== null) {
        this.$router.push({
          name: "map",
          params: {
            zone: zoneName,
          }
        })
      }
    },

    getZonePath (zoneName) {
      return document.querySelector('path[inkscape\\:label="' + zoneName + '"]');
    },

    async fetchData () {
      const body = await fetch('/map.json');
      const data = await body.json();
      this.mapData = data;
      this.isLoading = false;
    },

    /**
     * 
     * @param {String} oldZone The name of the zone that was previously selected.
     */
    openZonePopup (oldZone) {
      const zoneName = this.$route.params.zone;

      // Zone previously selected, unselect it.
      if (oldZone) {
        this.getZonePath(oldZone).classList.remove("selected");
      }

      if (zoneName) {
        const zoneData = this.mapData[zoneName];

        if (zoneData) {
          this.getZonePath(zoneName).classList.add("selected");
          this.popupStore.show(zoneData.nom, zoneData.description);
        }
      }
    }
  },

  async created () {
    await this.fetchData();
    this.openZonePopup();
  },

  unmounted () {
    this.popupStore.hide();
  }
}
</script>

<style>
.mapsvg {
  pointer-events: fill;
}

.mapsvg path {
  cursor: pointer;
  fill: transparent;
  stroke: none;
  transition: fill 0.2s ease;
}

.mapsvg path:hover {
  fill: rgba(129, 236, 236, 0.5);
}

.mapsvg path.selected {
  fill: rgba(255, 0, 0, 0.5);
}
</style>
