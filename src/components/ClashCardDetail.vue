<template>
  <v-card color="cyan darken-1" class="white--text">
    <v-layout>
      <v-flex xs12 pa-3>
        <h1 style="text-transform: uppercase">Clash #{{clash.id}}</h1>

        <v-layout align-content-end mb-4>
          <v-flex xs6>
            <h3>Location</h3>
            <h3>Type</h3>
            <h3>Disciplines Affected</h3>
          </v-flex>
          <v-flex class="data">
            <h3>{{clash.roomName}} {{clash.roomNumber}}</h3>
            <h3>{{ clash.type }}</h3>
            <h3>{{clash.disciplinesAffected.join(', ')}}</h3>
          </v-flex>
        </v-layout>

        <v-layout>
          <v-flex xs6>
            <h3>Selected Option</h3>
          </v-flex>
          <v-flex class="data">
            <h3>{{selectedOption || 'none'}}</h3>
          </v-flex>
        </v-layout>
        <v-layout>
          <v-flex xs6></v-flex>
          <v-flex class="data">
            <v-btn
              v-if="selectedOption"
              @click="clearSelection"
              color="#ed2349"
              class="white--text"
              small
            >
              Edit
              <v-icon right color="white">mdi-eraser</v-icon>
            </v-btn>
            <v-btn
              v-if="selectedOption"
              @click="submitOption"
              color="#ed2349"
              class="white--text"
              small
            >
              Submit
              <v-icon right color="white">send</v-icon>
            </v-btn>
          </v-flex>
        </v-layout>
      </v-flex>

      <v-flex pa-0>
        <v-img
          :src="require('../assets/test/' + clash.image)"
          width="350px"
          @click.stop="dialog=true"
        />
        <v-dialog v-model="dialog" max-width="800">
          <v-card>
            <v-img :src="require('../assets/test/' + clash.image)" />
          </v-card>
        </v-dialog>

        <!-- <v-img :src="require('../assets/clash-placeholder.png')" width="350px" /> -->
      </v-flex>
    </v-layout>
  </v-card>
</template>

<script>
export default {
  name: "ClashCardDetail",
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
