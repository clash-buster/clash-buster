<template>
  <v-card color="blue-grey darken-1" class="white--text">
    <v-layout mb-4>
      <v-flex xs12 pa-3>
        <h1 style="text-transform: uppercase">Project DBEI</h1>
      </v-flex>

      <v-flex pa-0>
        <!-- <v-img :src="require('../assets/clash-placeholder.png')" width="350px" /> -->
      </v-flex>
    </v-layout>
  </v-card>
</template>

<script>
export default {
  name: "ProjectDetail",
  props: ["clash"],
  data: () => ({
    dialog: false
  }),
  computed: {
    selectedOption() {
      return this.$store.state.selectedOption;
    }
  },
  methods: {
    clearSelection() {
      this.$store.commit("setSelectedOption", null);
    }
  }
};
</script>
