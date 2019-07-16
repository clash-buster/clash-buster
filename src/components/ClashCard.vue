<template>
  <v-card color="cyan" class="white--text">
    <v-card-title>
      <h3>{{clash.id}} {{clash.type}}</h3>
    </v-card-title>
    <v-img
      :src="require('../assets/test/' + clash.image)"
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
