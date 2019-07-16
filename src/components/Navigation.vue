<template>
  <v-toolbar app dense>
    <v-toolbar-title class="headline text-uppercase">
      <span>
        <a href="/">clash ></a>
      </span>
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
  color: black !important;
}
</style>
