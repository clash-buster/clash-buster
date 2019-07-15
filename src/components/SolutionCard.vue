<template>
  <v-card>
    <v-layout>
      <v-flex xs4>
        <v-img :src="require('../assets/' + solution.image)" height="250" />
      </v-flex>
      <v-flex pa-2>
        <h3>Solution {{solution.id}}</h3>
        <ul>
          <li>Description: {{solution.description}}</li>
          <li>Cost: {{solution.cost}}</li>
          <li>Constructability: {{solution.constructability}}</li>
          <li>Schedule Impact: {{solution.time}}</li>
        </ul>
      </v-flex>
    </v-layout>
  </v-card>
</template>

<script>
export default {
  name: "SolutionCard",
  props: ["solution"],
  data: () => ({}),
  mounted() {
    console.log(this.solution);
  }
};
</script>
