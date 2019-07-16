<template>
  <v-container align-content-center>
    <!-- <ProjectDetail /> -->
    <v-layout>
      <v-flex>
        <h1>All Clashes</h1>
      </v-flex>
    </v-layout>
    <v-layout>
      <v-flex v-for="clash in sortedClashes" :key="clash.id" xs4 ma-2>
        <ClashCard :clash="clash" />
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import Clashes from "../assets/clashesTest.json";
import ClashCard from "./ClashCard";
import ProjectDetail from "./ProjectDetail";

export default {
  name: "AllClashes",
  components: { ClashCard, ProjectDetail },
  data: () => ({
    project: { name: "Project DBEI", clashes: Clashes }
  }),
  computed: {
    sortedClashes() {
      let clashes = this.project.clashes;

      if (this.clashPhase !== "All") {
        clashes = clashes.filter(
          element => element.projectPhase == this.clashPhase
        );
      }

      return clashes;
    }
  }
};
</script>
