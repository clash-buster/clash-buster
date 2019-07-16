<template>
  <v-layout mb-4>
    <v-expansion-panel>
      <v-expansion-panel-content>
        <template v-slot:header>
          <h5>Advanced Sort</h5>
        </template>
        <v-card>
          <v-flex xs12 pl-4 pr-4>
            <v-slider
              v-model="cost"
              append-icon="attach_money"
              :max="4"
              :min="1"
              label="Cost"
              color="amber darken-4"
              ticks
            ></v-slider>
          </v-flex>
          <v-layout>
            <v-flex xs6 pl-4 pr-2>
              <v-slider
                v-model="constructability"
                :max="4"
                :min="1"
                label="Constructability"
                color="amber darken-4"
                ticks
              ></v-slider>
            </v-flex>
            <v-flex xs6 pl-2 pr-4>
              <v-slider
                v-model="scheduleImpact"
                :max="4"
                :min="1"
                label="Schedule Impact"
                color="amber darken-4"
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
                color="amber darken-4"
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
    cost: 4,
    constructability: 4,
    scheduleImpact: 4,
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
  })
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
