<template>
  <v-container>
    <ClashCardDetail :clash="clash" />

    <v-layout mt-5>
      <v-flex>
        <h1>Possible Solutions</h1>
      </v-flex>
      <v-flex xs4>
        <v-select
          :items="phases"
          name="phases"
          label="Filter by Phase"
          prepend-icon="mdi-filter"
          item-text="name"
          item-value="key"
          v-model="clashPhase"
          @change="onChange"
          dense
        />
      </v-flex>
    </v-layout>
    <FilterPanel />
    <v-layout column>
      <v-flex
        v-show="filteredSolutions"
        style="animation: resultsIn 0.5s"
        v-for="(solution, index) in filteredSolutions"
        :key="index"
        mb-3
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
    clashPhase: "all",
    phases: [
      { name: "All", key: "all" },
      { name: "Design Development", key: "dd" },
      { name: "Construction Documentation", key: "cd" },
      { name: "Construction Administration", key: "ca" },
      { name: "Post Occupancy", key: "po" }
    ]
  }),
  mounted() {},
  methods: {
    onChange(phase) {
      this.clashPhase = phase;
    }
  },
  computed: {
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

      // let sortBy = this.sort || "cost";
      // if (sortBy === "disciplinesAffected") {
      //   solutions.sort((a, b) => a[sortBy].length < b[sortBy].length);
      // } else {
      //   solutions.sort((a, b) =>
      //     a[sortBy] > b[sortBy] ? 1 : b[sortBy] > a[sortBy] ? -1 : 0
      //   );
      // }

      return filtered;
    }
  },
  methods: {
    onChange(sort) {
      this.sort = sort;
    }
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
