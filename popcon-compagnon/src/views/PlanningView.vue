<template>
  <div>
    <label for="input">Chercher:</label>
    <input
      v-model="query"
      type="search"
      placeholder="Nom ou description…"
      class="mx-2 px-1 border-2 border-solid border-slate-300 rounded-sm outline-slate-400 text-sm"
    >
    <table>
      <thead>
        <tr>
          <th>Nom</th>
          <th>Description</th>
          <th>Début</th>
          <th>Durée</th>
          <th>Zone</th>
        </tr>
      </thead>
      <tbody>
        <tr
          v-for="(event, i) in displayedEvents"
          :key="i"
          class="even:bg-slate-100 odd:bg-slate-200"
        >
          <td class="p-2">
            {{ event.nom }}
          </td>
          <td class="p-2">
            {{ event.description }}
          </td>
          <td class="p-2">
            {{ displayDate(event) }}
          </td>
          <td class="p-2">
            {{ event.duree }}
          </td>
          <td class="p-2">
            <RouterLink
              :to="mapUrl(event)"
              class="text-sky-500 underline hover:no-underline"
              title="Cliquez pour voir où se déroule cet évènement."
            >Voir sur la carte 📍</RouterLink>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import { RouterLink } from 'vue-router';

export default {
  components: {
    RouterLink,
  },

  data () {
    return {
      query: "",
      events: [],
    }
  },

  methods: {
    async fetchPlanning () {
      const request = await fetch('/planning.json');
      const planning = await request.json();
      this.events = Object.values(planning);
    },

    displayDate (eventObj) {
      return new Date(eventObj.debut).toLocaleString();
    },

    mapUrl (event) {
      return {
        name: "map",
        params: {
          zone: event.zone,
        }
      }
    }
  },

  computed: {
    filteredEvents () {
      const query = this.query.toLowerCase();
      if (query.length < 1) {
        return this.events;
      }
      return this.events.filter(eventObj => {
        const findInName = eventObj.nom.toLowerCase().indexOf(query) !== -1;
        const findInDesc = eventObj.description.toLowerCase().indexOf(query) !== -1;
        const findInKeywords = eventObj.mots_clef.join("").toLowerCase().indexOf(query) !== -1;

        return findInName || findInDesc || findInKeywords;
      })
    },

    displayedEvents () {
      return this.filteredEvents.sort((eventOne, eventTwo) => {
        const dateOne = new Date(eventOne.debut).getTime();
        const dateTwo = new Date(eventTwo.debut).getTime();

        return dateOne - dateTwo;
      })
    }
  },

  created () {
    this.fetchPlanning();
  },
}
</script>
