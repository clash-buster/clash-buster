import Vue from "vue";
import "./plugins/vuetify";
import App from "./App.vue";
import VueRouter from "vue-router";
import AllClashes from "./components/AllClashes";
import Clash from "./components/Clash";

Vue.config.productionTip = false;
Vue.use(VueRouter);

const router = new VueRouter({
  routes: [
    { path: "/", component: AllClashes, props: true },
    { path: "/clash", component: Clash, name: "clash", props: true }
  ]
});

new Vue({
  render: h => h(App),
  router
}).$mount("#app");
