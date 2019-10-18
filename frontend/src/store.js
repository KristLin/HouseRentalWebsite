import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    userId: null,
    userRole: null
  },
  getters: {
    isLoggedIn: state => {
      if (state.userId || localStorage.getItem("userId")) {
        return true
      } else {
        return false
      }
    },
    isProvider: state => {
      if (state.userRole === "provider" || localStorage.getItem("userId") === "provider") {
        return true
      } else {
        return false
      }
    },
    getUserId: state => {
      return state.userId ? state.userId : localStorage.getItem("userId")
    }
  },
  mutations: {
    login(state, userData) {
      state.userId = userData.userId;
      state.userRole = userData.userRole;
      localStorage.setItem("userId", userData.userId);
      localStorage.setItem("userRole", userData.userRole);
    },
    logout(state) {
      state.userId = null;
      state.userRole = null;
      localStorage.removeItem("userId");
      localStorage.removeItem("userRole");
    }
  },
  actions: {
  }
})
