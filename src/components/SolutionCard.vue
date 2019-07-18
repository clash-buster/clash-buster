<template>
  <v-card>
    <v-flex pl-4 pt-2>
      <h5>PHASE: {{phase}}</h5>
      <h2>
        Solution {{solution.id}}
        <v-btn v-if="!selectedOption" @click="setOption(solution.id)" small icon>
          <v-icon color="#ed2349">star_border</v-icon>
        </v-btn>
        <v-btn
          v-if="selectedOption===solution.id && optionExists"
          @click="setOption(null)"
          small
          icon
        >
          <v-icon color="#ed2349">star</v-icon>
        </v-btn>
      </h2>
      <h4>{{solution.description}}</h4>
    </v-flex>
    <v-img :src="require('../assets/test/' + solution.image)" @click="dialog=true" height="250" />
    <v-layout>
      <v-dialog v-model="dialog" max-width="800">
        <v-card>
          <v-img :src="require('../assets/test/' + solution.image)" />
        </v-card>
      </v-dialog>
      <v-container pa-2 align-center>
        <v-layout class="score" style="align-items: flex-end">
          <v-flex xs3 ml-2 mr-1>
            <h1>{{cost}}</h1>
            <h3>Cost</h3>
          </v-flex>
          <v-flex xs3 ml-1 mr-1>
            <v-progress-circular
              :size="55"
              :width="7"
              :rotate="-90"
              :value="shownViabilityScore"
              color="#ed2349"
            >
              <h2>{{solution.viability}}</h2>
            </v-progress-circular>
            <h3>Viability</h3>
          </v-flex>
          <v-flex xs4 ml-1 mr-1>
            <v-progress-circular
              :size="55"
              :width="7"
              :rotate="-90"
              :value="shownScheduleScore"
              color="#ed2349"
            >
              <h2>{{solution.scheduleImpact}}</h2>
            </v-progress-circular>
            <h3>Schedule Impact</h3>
          </v-flex>
          <v-flex xs4 ml-1 mr-1>
            <span>{{solution.disciplinesAffected.join(', ')}}</span>
            <h3>Disciplines</h3>
          </v-flex>
        </v-layout>
      </v-container>
    </v-layout>
  </v-card>
</template>

<script>
export default {
  name: "SolutionCard",
  props: ["solution"],
  data: () => ({
    selectedOption: "",
    dialog: false,
    scheduleImpact: 0,
    viability: 0
  }),
  mounted() {
    setInterval(() => {
      while (this.scheduleImpact < this.shownScheduleScore) {
        this.scheduleImpact += 1;
      }
      while (this.viability < this.shownViabilityScore) {
        this.viability += 1;
      }
    }, 20);
  },
  methods: {
    setOption(id) {
      this.selectedOption = id;
      this.$store.commit("setSelectedOption", id);
    },
    enlargeView(src) {}
  },
  computed: {
    shownScheduleScore() {
      return (this.solution.scheduleImpact / 4) * 100;
    },
    shownViabilityScore() {
      return (this.solution.viability / 4) * 100;
    },
    optionExists() {
      return this.$store.state.selectedOption;
    },
    cost() {
      let cost = "";
      for (let i = 0; i < this.solution.cost; i++) {
        cost += "$";
      }
      return cost;
    },
    phase() {
      switch (this.solution.phase) {
        case "dd":
          return "Design Development";
        case "cd":
          return "Construction Documentation";
        case "ca":
          return "Construction Administration";
      }
    }
  },
  mounted() {}
};
</script>

<style>
h2 {
  color: #00acc1;
  font-size: 20pt;
  font-family: "Fjalla One", sans-serif;
  font-weight: normal;
  margin-bottom: -5px;
  text-transform: uppercase;
}
h4 {
  margin-bottom: 20px;
}
h5 {
  color: #757575;
  text-transform: uppercase;
}
ul {
  padding: 0 !important;
}
li {
  list-style: none;
}
.score h1 {
  color: #ed2349;
  font-size: 24pt;
}
</style>
