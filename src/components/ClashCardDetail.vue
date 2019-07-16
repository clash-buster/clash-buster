<template>
  <v-card color="blue-grey darken-1" class="white--text">
    <v-layout>
      <v-flex xs12 pa-3>
        <h1 style="text-transform: uppercase">Clash #{{clash.id}}</h1>

        <v-layout align-content-end>
          <v-flex xs6>
            <h3>Location</h3>
            <h3>Type</h3>
            <h3>Disciplines Affected</h3>
          </v-flex>
          <v-flex class="data">
            <h3>{{clash.roomName}} {{clash.roomNumber}}</h3>
            <h3>{{ clash.type }}</h3>
            <h3>
              <span
                v-for="(discipline, index) in clash.disciplinesAffected"
                :key="index"
              >{{discipline}},</span>
            </h3>
          </v-flex>
        </v-layout>
      </v-flex>

      <v-flex pa-0>
        <v-img :src="require('../assets/' + clash.image)" width="350px" />
      </v-flex>
    </v-layout>
  </v-card>
</template>

<script>
export default {
  name: "ClashCardDetail",
  props: ["clash"]
};
</script>
