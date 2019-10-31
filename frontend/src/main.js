import Vue from 'vue'
import App from './App.vue'
import router from './router'

import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'

import axios from 'axios'
import store from './store'

import * as VueGoogleMaps from 'vue2-google-maps'
import VueSwal from 'vue-swal'
import * as VueSpinnersCss from "vue-spinners-css";

Vue.use(VueSwal)
Vue.use(VueSpinnersCss)

Vue.prototype.$axios = axios
// axios.defaults.headers.post['Content-Type'] = 'application/json';

Vue.config.productionTip = false

Vue.use(VueGoogleMaps, {
  load: {
    key: process.env.VUE_APP_GOOGLE_MAP_KEY,
    libraries: 'places', // This is required if you use the Autocomplete plugin
  },
  installComponents: true
})

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
