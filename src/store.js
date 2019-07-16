import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    cost: 4,
    viability: 4,
    scheduleImpact: 4,
    selectedOption: "",
    filter: "all",
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
    setviability(state, viability) {
      state.viability = viability;
    },
    setScheduleImpact(state, scheduleImpact) {
      state.scheduleImpact = scheduleImpact;
    },
    setSelectedOption(state, selected) {
      state.selectedOption = selected;
    },
    setFilter(state, filter) {
      state.filter = filter;
    }
  }
});
