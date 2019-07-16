<template>
  <v-container>
    <ClashCardDetail :clash="clash" />

    <v-layout mt-5>
      <v-flex>
        <h1>Possible Solutions</h1>
      </v-flex>
      <v-flex xs8>
        <FilterPanel />
      </v-flex>
    </v-layout>

    <v-layout row wrap>
      <v-flex
        v-show="shownSolutions"
        style="animation: resultsIn 0.5s"
        v-for="(solution, index) in shownSolutions"
        :key="index"
        mb-3
        pl-2
        pr-2
        xs6
      >
        <SolutionCard :solution="solution" />
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import SolutionCard from "./SolutionCard";
import ClashCardDetail from "./ClashCardDetail";
import FilterPanel from "./FilterPanel";

export default {
  name: "Clash",
  props: ["clash"],
  components: { SolutionCard, ClashCardDetail, FilterPanel },
  data: () => ({
    sort: ""
  }),
  mounted() {},
  computed: {
    clashPhase() {
      return this.$store.state.filter;
    },
    filteredSolutions() {
      let filtered = [];
      let solutions = this.clash.solutions;

      Object.keys(solutions).forEach(phase => {
        if (phase === this.clashPhase) {
          solutions[phase].map(solution => {
            solution["phase"] = phase;
            filtered.push(solution);
          });
        } else if (this.clashPhase === "all") {
          solutions[phase].map(solution => {
            solution["phase"] = phase;
            filtered.push(solution);
          });
        }
      });
      return filtered;
    },
    shownSolutions() {
      let solutions = this.filteredSolutions;
      let selectedDisciplines = this.$store.state.disciplinesInvolved;
      let sortingVariables = [
        { name: "cost", value: this.$store.state.cost },
        { name: "viability", value: this.$store.state.viability },
        { name: "scheduleImpact", value: this.$store.state.scheduleImpact }
      ];

      // Sorting first by low cost to high cost by default
      solutions.sort((a, b) =>
        a["cost"] > b["cost"] ? 1 : b["cost"] > a["cost"] ? -1 : 0
      );

      // Filtering based on cost, viability, and schedule impact
      sortingVariables.forEach(variable => {
        solutions = solutions.filter(solution => {
          return solution[variable.name] <= variable.value;
        });
      });

      // FUTURE TODO: Filtering based on disciplines involved
      return solutions;
    }
  },
  methods: {
    onChange(sort) {
      this.sort = sort;
    },
    checkIfExists() {}
  }
};
</script>

<style>
ul {
  font-size: 12pt;
}
.data h3 {
  font-weight: normal !important;
}
.v-text-field {
  margin: 0 !important;
  padding: 0 !important;
}
@keyframes resultsIn {
  0% {
    transform: scale(1);
    opacity: 0;
  }
  0.01% {
    transform: scale(0.8);
    opacity: 1;
  }
  100% {
    transform: scale(1);
  }
}
</style>
