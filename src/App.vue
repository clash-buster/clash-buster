<template>
  <div>
    <Navigation />
    <v-app class="application">
      <router-link to="/"></router-link>
      <router-link to="/clash"></router-link>
      <router-view></router-view>
    </v-app>
  </div>
</template>

<script>
import Navigation from "./components/Navigation";

export default {
  name: "app",
  components: { Navigation },
  data: () => ({}),
  mounted() {},
  methods: {}
};
</script>

<style>
.application--wrap {
  min-height: calc(100vh - 50px) !important;
}
* {
  box-sizing: border-box;
}
body {
  margin: 0;
}
.application {
  margin-top: 50px;
}
</style>
