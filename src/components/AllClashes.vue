<template>
  <v-container align-content-center>
    <h1>All Clashes</h1>
    <v-layout>
      <v-flex v-for="clash in clashes" :key="clash.id" xs6 ma-2>
        <ClashCard :clash="clash" />
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import Clashes from "../assets/clashes.json";
import ClashCard from "./ClashCard";

export default {
  name: "AllClashes",
  components: { ClashCard },
  data: () => ({
    clashes: Clashes
  })
};
</script>
