<template>
  <v-card>
    <v-card-title>Clash #{{clash.id}}: {{clash.type}}</v-card-title>
    <v-img
      :src="require('../assets/' + clash.image)"
      onmouseover
      style="cursor: pointer"
      @click="ViewClash()"
    />
  </v-card>
</template>

<script>
export default {
  name: "ClashCard",
  data: () => ({}),
  props: ["clash"],
  methods: {
    ViewClash() {
      const clash = this.clash;

      this.$router.push({
        name: "clash",
        params: {
          clash: clash
        }
      });
    }
  }
};
</script>
