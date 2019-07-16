import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    cost: 4,
    constructability: 4,
    scheduleImpact: 4,
    disciplinesInvolved: [
      "Architectural",
      "Structural",
      "Mechanical",
      "Electrical",
      "Plumbing",
      "Fire"
    ]
  },
  mutations: {
    setDisciplines(state, disciplines) {
      state.disciplinesInvolved = disciplines;
    },
    setCost(state, cost) {
      state.cost = cost;
    },
    setConstructability(state, constructability) {
      state.constructability = constructability;
    },
    setScheduleImpact(state, scheduleImpact) {
      state.scheduleImpact = scheduleImpact;
    }
  }
});
