import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  // user state
  state: {
    userId: null,
    userRole: null,
    userName: null,
  },

  // get user state
  getters: {
    isLoggedIn: state => {
      if (state.userId || localStorage.getItem("userId")) {
        return true
      } else {
        return false
      }
    },
    isProvider: state => {
      if (state.userRole === "provider" || localStorage.getItem("userRole") === "provider") {
        return true
      } else {
        return false
      }
    },
    getUserId: state => {
      return state.userId ? state.userId : localStorage.getItem("userId")
    },
    getUserRole: state => {
      return state.userRole ? state.userRole : localStorage.getItem("userRole")
    },
    getUserName: state => {
      return state.userName ? state.userName : localStorage.getItem("userName")
    }
  },

  // user state mutations
  mutations: {
    login(state, userData) {
      state.userId = userData.userId;
      state.userRole = userData.userRole;
      state.userName = userData.userName;
      localStorage.setItem("userId", userData.userId);
      localStorage.setItem("userRole", userData.userRole);
      localStorage.setItem("userName", userData.userName)
    },
    logout(state) {
      state.userId = null;
      state.userRole = null;
      state.userName = null;
      localStorage.removeItem("userId");
      localStorage.removeItem("userRole");
      localStorage.removeItem("userName")
    }
  },
  actions: {
  }
})
