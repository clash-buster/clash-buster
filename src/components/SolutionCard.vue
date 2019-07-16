<template>
  <v-card>
    <v-layout>
      <v-flex xs4>
        <v-img :src="require('../assets/' + solution.image)" height="250" />
      </v-flex>
      <v-flex pa-2>
        <h5>PHASE: {{phase}}</h5>
        <h2>Solution {{solution.id}}</h2>
        <h4>{{solution.description}}</h4>

        <v-layout>
          <v-flex xs4>
            <h3>Cost</h3>
            <h3>Constructability</h3>
            <h3>Schedule Impact</h3>
            <h3>Disciplines Involved</h3>
          </v-flex>
          <v-flex class="data">
            <h3>{{cost}}</h3>
            <h3>{{solution.constructability}}</h3>
            <h3>{{solution.time}}</h3>
            <h3>
              <span
                v-for="(discipline, index) in solution.disciplinesAffected"
                :key="index"
              >{{discipline}}</span>
            </h3>
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
  data: () => ({}),
  computed: {
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
  color: #607d8b;
  font-size: 20pt;
  margin-bottom: -5px;
  text-transform: uppercase;
}
h4 {
  margin-bottom: 20px;
}
h5 {
  color: #bdbdbd;
  text-transform: uppercase;
}
ul {
  padding: 0 !important;
}
li {
  list-style: none;
}
</style>
