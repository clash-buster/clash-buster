<template>
  <v-card>
    <v-flex pl-4 pt-2>
      <h5>PHASE: {{phase}}</h5>
      <h2>
        Solution {{solution.id}}
        <v-btn v-if="!optionExists" @click="setOption(solution.id)" small icon>
          <v-icon color="#ed2349">star_border</v-icon>
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
      <v-flex pa-2>
        <v-layout>
          <v-flex xs4>
            <h3>Cost</h3>
            <h3>Viability</h3>
            <h3>Schedule Impact</h3>
            <h3>Disciplines Involved</h3>
          </v-flex>
          <v-flex class="data">
            <h3>{{cost}}</h3>
            <h3>{{solution.viability}}</h3>
            <h3>{{solution.scheduleImpact}}</h3>
            <h3>{{solution.disciplinesAffected.join(', ')}}</h3>
          </v-flex>
        </v-layout>
      </v-flex>
    </v-layout>
  </v-card>
</template>

<script>
export default {
  name: "SolutionCard",
  props: ["solution"],
  data: () => ({
    selectedOption: "",
    dialog: false
  }),
  methods: {
    setOption(id) {
      this.selectedOption = id;
      this.$store.commit("setSelectedOption", id);
    },
    enlargeView(src) {}
  },
  computed: {
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
</style>
