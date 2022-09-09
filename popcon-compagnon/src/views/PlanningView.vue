<template>
  <div>
    <div class="flex items-center justify-center px-3 pt-6">
      <label class="font-semibold" for="input">Rechercher:</label>
      <input
        v-model="query"
        id="input"
        type="search"
        placeholder="Nom ou description…"
        class="font-semibold mx-2 px-3 py-1 border-2 border-solid border-popcon-blue rounded-lg outline-none text-popcon-blue focus:border-popcon-green"
      />

      <label class="font-semibold" for="select">Choisir une date:</label>
      <select
        id="select"
        v-model="selectedDate"
        class="font-semibold mx-2 px-2 py-1 border-2 border-solid border-popcon-blue rounded-lg outline-none text-popcon-blue focus:border-popcon-green"
      >
        <option value="">Tous les jours</option>
        <option v-for="(date, i) in dates" :value="date" :key="i">
          {{ displayDay(date) }}
        </option>
      </select>

      <button
        v-if="selectedDate || query"
        @click="selectedDate = query = ''"
        type="button"
        class="ml-2 px-3 py-1 uppercase font-bold text-white text-sm bg-popcon-orange rounded-lg"
      >
        X
      </button>
    </div>
    <div class="mt-6 overflow-x-auto w-full relative">
      <table class="w-full">
        <thead>
          <tr class="bg-popcon-green text-white">
            <th class="font-semibold py-3 border-2 border-solid border-white">
              Nom
            </th>

            <th
              class="hidden font-semibold py-3 border-2 border-solid border-white xl:table-cell"
            >
              Description
            </th>

            <th class="font-semibold py-3 border-2 border-solid border-white">
              Début
            </th>
            <th class="font-semibold py-3 border-2 border-solid border-white">
              Durée
            </th>
            <th class="font-semibold py-3 border-2 border-solid border-white">
              Zone
            </th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="(event, i) in displayedEvents"
            :key="i"
            class="even:bg-sky-100 odd:bg-white text-gray-700"
          >
            <!-- TODO style for ended activities -->
            <!-- TODO style for current ongoing activities -->
            <!-- TODO add to calendar ? -->
            <td class="font-semibold p-1 md:p-2 lg:p-4 lg:pl-8">
              {{ event.nom }}
            </td>

            <td
              class="hidden font-semibold p-1 md:p-2 lg:p-4 lg:pl-8 xl:table-cell"
            >
              {{ event.description }}
            </td>

            <td class="font-semibold p-1 md:p-2 lg:p-4">
              {{ displayDate(event) }}
            </td>
            <td class="font-semibold p-1 md:p-2 lg:p-4">
              {{ displayDuration(event) }}
            </td>
            <td class="font-semibold p-1 md:p-2 lg:p-4">
              <RouterLink
                v-if="event.zone"
                :to="mapUrl(event)"
                class="text-popcon-orange underline hover:no-underline"
                title="Cliquez pour voir où se déroule cet évènement."
                >{{ event.zone }}</RouterLink
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

  data() {
    return {
      query: "",
      events: [],
      dates: [],
      selectedDate: new Date().toDateString(),
    };
  },

  methods: {
    async fetchPlanning() {
      const request = await fetch("/donnees/planning.json");
      const planning = await request.json();
      this.events = Object.values(planning.activites);

      this.events.sort((eventOne, eventTwo) => {
        const dateOne = new Date(eventOne.debut).getTime();
        const dateTwo = new Date(eventTwo.debut).getTime();

        return dateOne - dateTwo;
      });

      this.getDates();
    },

    displayDate(eventObj) {
      return new Date(eventObj.debut).toLocaleString(undefined, {
        weekday: "long",
        hour: "numeric",
        minute: "numeric",
      });
    },

    displayDay(date) {
      return new Date(date).toLocaleString(undefined, { weekday: "long" });
    },

    displayDuration(eventObj) {
      let duration = eventObj.duree;
      try {
        duration = td.parse(duration);
      } catch {
        console.error("duree invalide", eventObj);
        return duration;
      }
      let output = "";
      if (duration.hours) {
        output += duration.hours + " heures ";
      }
      if (duration.minutes) {
        output += duration.minutes + " minutes";
      }
      return output;
    },

    mapUrl(event) {
      return {
        name: "map",
        query: {
          zone: event.zone.toLowerCase().replace(" ", "_"),
        },
      };
    },

    /**
     * Gets the dates from the object and parses it to DD/MM/YYYY format.
     * Makes an array of dates without duplicates.
     */
    getDates() {
      const events = this.events;
      const dates = events.map((event) => {
        const eventDate = event.debut;
        const parsedDate = new Date(eventDate);
        return parsedDate.toDateString();
      });
      const uniqueDates = Array.from(new Set(dates));
      this.dates = uniqueDates;

      if (this.dates.indexOf(this.selectedDate) < 0) {
        this.selectedDate = "";
      }
    },
  },

  computed: {
    /**
     * Returns all the events that match the query.
     * @returns {Array<Object>}
     */
    filteredEvents() {
      const query = this.query.toLowerCase();

      return this.events.filter((eventObj) => {
        const findInName = eventObj.nom.toLowerCase().indexOf(query) !== -1;
        const findInDesc =
          eventObj.description.toLowerCase().indexOf(query) !== -1;
        const findInKeywords =
          eventObj.mots_clef.join("").toLowerCase().indexOf(query) !== -1;
        const findDate =
          new Date(eventObj.debut).toDateString().indexOf(this.selectedDate) !==
          -1;

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
    displayedEvents() {
      return this.filteredEvents;
    },
  },

  created() {
    this.fetchPlanning();
  },
};
</script>
