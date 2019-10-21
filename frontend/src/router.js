import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import(/* webpackChunkName: "about" */ './views/About.vue')
    },
    {
      path: '/contact',
      name: 'contact',
      component: () => import(/* webpackChunkName: "contact" */ './views/Contact.vue')
    },
    {
      path: '/login',
      name: 'login',
      component: () => import(/* webpackChunkName: "login" */ './views/Login.vue')
    },
    {
      path: '/signup',
      name: 'signup',
      component: () => import(/* webpackChunkName: "signup" */ './views/Signup.vue')
    },
    {
      path: '/search',
      name: 'search',
      component: () => import(/* webpackChunkName: "search" */ './views/Search.vue')
    },
    {
      path: '/house',
      name: 'house',
      component: () => import(/* webpackChunkName: "house" */ './views/House.vue')
    },
    {
      path: '/myAccount',
      name: 'myAccount',
      component: () => import(/* webpackChunkName: "uploadHouse" */ './views/MyAccount.vue')
    },
    {
      path: '/myHouses',
      name: 'myHouses',
      component: () => import(/* webpackChunkName: "uploadHouse" */ './views/MyHouses.vue')
    },
    {
      path: '/uploadHouse',
      name: 'uploadHouse',
      component: () => import(/* webpackChunkName: "uploadHouse" */ './views/UploadHouse.vue')
    }
  ]
})
