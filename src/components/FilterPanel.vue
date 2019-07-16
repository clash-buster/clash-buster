<template>
  <v-layout mb-4>
    <v-expansion-panel>
      <v-expansion-panel-content>
        <template v-slot:header>
          <h5>Advanced Sort</h5>
        </template>
        <v-card>
          <v-layout>
            <v-flex pl-4 pr-4>
              <v-slider
                v-model="cost"
                append-icon="attach_money"
                :max="4"
                :min="1"
                label="Cost"
                color="#ed2349"
                @change="setSliders"
                ticks
              ></v-slider>
            </v-flex>
            <v-flex xs3 mr-4 pt-2>
              <v-select
                :items="phases"
                name="phases"
                label="Filter by Phase"
                item-text="name"
                item-value="key"
                v-model="clashPhase"
                @change="onChange"
                dense
              />
            </v-flex>
          </v-layout>
          <v-layout>
            <v-flex xs6 pl-4 pr-2>
              <v-slider
                v-model="viability"
                :max="4"
                :min="1"
                label="Viability"
                color="#ed2349"
                @change="setSliders"
                ticks
              ></v-slider>
            </v-flex>
            <v-flex xs6 pl-2 pr-4>
              <v-slider
                v-model="scheduleImpact"
                :max="4"
                :min="1"
                label="Schedule Impact"
                color="#ed2349"
                @change="setSliders"
                ticks
              ></v-slider>
            </v-flex>
          </v-layout>
          <v-layout mb-4>
            <v-flex v-for="discipline in disciplinesInvolved" :key="discipline" xs2 pl-4>
              <v-checkbox
                v-model="selected"
                :label="discipline"
                :value="discipline"
                color="#ed2349"
                @change="setDisciplines"
                hide-details
              ></v-checkbox>
            </v-flex>
          </v-layout>
        </v-card>
      </v-expansion-panel-content>
    </v-expansion-panel>
  </v-layout>
</template>

<script>
export default {
  name: "FilterPanel",
  data: () => ({
    clashPhase: "all",
    phases: [
      { name: "All", key: "all" },
      { name: "Design Development", key: "dd" },
      { name: "Construction Documentation", key: "cd" },
      { name: "Construction Administration", key: "ca" }
    ],
    cost: 4,
    scheduleImpact: 4,
    viability: 4,
    selected: [
      "Architectural",
      "Structural",
      "Mechanical",
      "Electrical",
      "Plumbing",
      "Fire"
    ],
    disciplinesInvolved: [
      "Architectural",
      "Structural",
      "Mechanical",
      "Electrical",
      "Plumbing",
      "Fire"
    ]
  }),
  methods: {
    setDisciplines() {
      this.$store.commit("setDisciplines", this.selected);
    },
    setSliders() {
      this.$store.commit("setCost", this.cost);
      this.$store.commit("setviability", this.viability);
      this.$store.commit("setScheduleImpact", this.scheduleImpact);
    },
    onChange(phase) {
      this.$store.commit("setFilter", phase);
    }
  }
};
</script>

<style>
.v-expansion-panel {
  background-color: rgba(255, 255, 255, 0) !important;
  box-shadow: none !important;
  -webkit-box-shadow: none !important;
}
.v-expansion-panel__header {
  background-color: rgba(255, 255, 255, 0) !important;
}
</style>
