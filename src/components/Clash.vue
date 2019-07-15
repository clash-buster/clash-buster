<template>
  <v-container>
    <h1>Clash #{{clash.id}}</h1>
    <ul>
      <li>Type: {{ clash.type }}</li>
      <li>
        Disciplines Affected:
        <span
          v-for="(discipline, index) in clash.disciplinesAffected"
          :key="index"
        >{{discipline}},</span>
      </li>
      <li>Project Phase: {{clash.projectPhase}}</li>
    </ul>

    <v-flex>
      <img :src="require('../assets/' + clash.image)" height="200" />
    </v-flex>
    <v-flex></v-flex>

    <v-layout>
      <v-flex>
        <h1>Possible Solutions</h1>
      </v-flex>
      <v-flex>
        <v-select
          :items="sortBy"
          name="sortBy"
          label="Sort By"
          prepend-icon="mdi-filter"
          item-text="name"
        />
      </v-flex>
    </v-layout>
    <v-layout column>
      <v-flex v-for="(solution, index) in clash.solutions" :key="index" mb-3>
        <SolutionCard :solution="solution" />
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import SolutionCard from "./SolutionCard";

export default {
  name: "Clash",
  props: ["clash"],
  components: { SolutionCard },
  data: () => ({
    sortBy: [
      { key: "cost", name: "Cost" },
      { key: "constructability", name: "Constructability" },
      { key: "scheduleImpact", name: "Schedule Impact" },
      { key: "disciplines", name: "Number of Disciplines Involved" }
    ]
  }),
  mounted() {}
};
</script>
