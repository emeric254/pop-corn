<template>
  <div class="flex justify-center">
    <div class="relative">
      <img src="@/assets/map.jpg" />
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
    }
  },

  computed: {
    ...mapStores(usePopupStore)
  },

  methods: {
    onMapClick (event) {
      const zone = event.target;
      const label = zone.getAttribute('inkscape:label');
      if (label !== null) {
        const zoneData = this.mapData[label];
        this.popupStore.show(zoneData.nom, zoneData.description);
      }
    },

    async fetchData () {
      const body = await fetch('/map.json');
      const data = await body.json();
      this.mapData = data;
    }
  },

  created () {
    this.fetchData();
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
</style>
