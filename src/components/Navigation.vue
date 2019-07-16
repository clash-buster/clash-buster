<template>
  <v-toolbar app dense>
    <v-toolbar-side-icon>
      <v-img :src="require('../assets/clash.png')" contain></v-img>
    </v-toolbar-side-icon>
    <v-toolbar-title class="title">
      <a href="/">CLASH ></a>
    </v-toolbar-title>
    <v-spacer></v-spacer>
    <v-btn icon flat href target="_blank">
      <v-icon>mdi-account-circle</v-icon>
    </v-btn>
  </v-toolbar>
</template>

<script>
export default {
  name: "Navigation",
  data: () => ({})
};
</script>

<style>
a {
  text-decoration: none;
  color: #ed2349 !important;
  font-weight: 700;
}
.title {
  color: #ed2349;
}
</style>
