<template>
  <div>
    <div class="flex items-center">
      <label for="input">Chercher:</label>
      <input
        v-model="query"
        id="input"
        type="search"
        placeholder="Nom ou description…"
        class="mx-2 px-3 py-1 border-2 border-solid border-popcon-blue rounded-lg outline-none text-popcon-blue focus:border-popcon-green"
      />
      <button
        v-if="query"
        @click="query = ''"
        type="button"
        class="ml-2 px-3 py-1 uppercase font-bold text-white text-sm bg-popcon-orange rounded-lg"
      >
        Vider
      </button>
      <label for="select">Choisir une date:</label>
      <select
        id="select"
        v-model="selectedDate"
        class="mx-2 px-2 py-1 border-2 border-solid border-popcon-blue rounded-lg outline-none text-popcon-blue focus:border-popcon-green"
      >
        <option value="">Tous les jours</option>
        <option v-for="(date, i) in dates" :value="date" :key="i">
          {{ date }}
        </option>
      </select>
      <button
        v-if="selectedDate"
        @click="selectedDate = ''"
        type="button"
        class="ml-2 px-3 py-1 uppercase font-bold text-white text-sm bg-popcon-orange rounded-lg"
      >
        Vider
      </button>
    </div>
    <div class="mt-6 overflow-x-auto w-full relative">
      <table class="w-full">
        <thead>
          <tr class="bg-popcon-green text-white">
            <th class="py-2">Nom</th>
            <th class="py-2">Description</th>
            <th class="py-2">Début</th>
            <th class="py-2">Durée</th>
            <th class="py-2">Zone</th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="(event, i) in displayedEvents"
            :key="i"
            class="even:bg-sky-100 odd:bg-white text-gray-700"
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
              {{ displayDuration(event) }}
            </td>
            <td class="p-2">
              <RouterLink
                :to="mapUrl(event)"
                class="text-popcon-orange underline hover:no-underline"
                title="Cliquez pour voir où se déroule cet évènement."
                >Voir sur la carte 📍</RouterLink
              >
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import { RouterLink } from "vue-router";
import * as td from "tinyduration";

export default {
  components: {
    RouterLink,
  },

  data () {
    return {
      query: "",
      events: [],
      dates: [],
      selectedDate: "",
    }
  },

  methods: {
    async fetchPlanning() {
      const request = await fetch("/donnees/planning.json");
      const planning = await request.json();
      this.events = Object.values(planning.activites);
      this.getDates();
    },

    displayDate(eventObj) {
      return new Date(eventObj.debut).toLocaleString();
    },

    displayDuration(eventObj) {
      const duration = td.parse(eventObj.duree);
      let output = "";
      if (duration.hours) {
        output += duration.hours + " heures ";
      }
      if (duration.minutes) {
        output += duration.minutes + " minutes";
      }
      return output;
    },

    mapUrl (event) {
      return {
        name: "map",
        params: {
          zone: event.zone,
        }
      }
    },

    /**
     * Gets the dates from the object and parses it to DD/MM/YYYY format.
     * Makes an array of dates without duplicates.
     */
    getDates () {
      const events = this.events;
      const dates = events.map((event) => {
        const eventDate = event.debut;
        const parsedDate = new Date(eventDate);
        return parsedDate.toLocaleDateString();
      });
      const uniqueDates = Array.from(new Set(dates));
      this.dates = uniqueDates;
    }
  },

  computed: {
    /**
     * Returns all the events that match the query.
     * @returns {Array<Object>}
     */
    filteredEvents () {
      const query = this.query.toLowerCase();

      return this.events.filter(eventObj => {
        const findInName = eventObj.nom.toLowerCase().indexOf(query) !== -1;
        const findInDesc = eventObj.description.toLowerCase().indexOf(query) !== -1;
        const findInKeywords = eventObj.mots_clef.join("").toLowerCase().indexOf(query) !== -1;
        const findDate = this.displayDate(eventObj).indexOf(this.selectedDate) !== -1;

        if (query === "") {
          return findDate;
        }

        return findInName || findInDesc || findInKeywords;
      });
    },

    /**
     * Returns the filtered events and sorts them by date.
     * @returns {Array<Object>}
     */
    displayedEvents () {
      return this.filteredEvents.sort((eventOne, eventTwo) => {
        const dateOne = new Date(eventOne.debut).getTime();
        const dateTwo = new Date(eventTwo.debut).getTime();

        return dateOne - dateTwo;
      });
    },
  },

  created() {
    this.fetchPlanning();
  },
};
</script>
