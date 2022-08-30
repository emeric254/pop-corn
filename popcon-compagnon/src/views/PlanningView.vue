<template>
  <div>
    <input
      v-model="query"
      type="search"
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
          v-for="(event, i) in filteredEvents"
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
            {{ event.zone }}
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
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
    }
  },

  computed: {
    filteredEvents () {
      const query = this.query.toLowerCase();
      if (query.length < 3) {
        return this.events;
      }
      return this.events.filter(eventObj => {
        const findInName = eventObj.nom.toLowerCase().indexOf(query) !== -1;
        const findInDesc = eventObj.description.toLowerCase().indexOf(query) !== -1;
        const findInKeywords = eventObj.mots_clef.join("").toLowerCase().indexOf(query) !== -1;

        return findInName || findInDesc || findInKeywords;
      })
    }
  },

  created () {
    this.fetchPlanning();
  },
}
</script>
