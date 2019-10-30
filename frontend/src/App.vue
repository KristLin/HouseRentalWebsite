<template>
  <div id="app">
    <Header />
    <router-view />
    <Footer />
  </div>
</template>

<script>
import Header from "@/components/Header.vue";
import Footer from "@/components/Footer.vue";

export default {
  components: {
    Header,
    Footer
  }
};
</script>

<style>
@import url("https://fonts.googleapis.com/css?family=Nunito&display=swap");
#app {
  font-family: "Nunito", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

.swal-button--confirm {
  padding: 7px 19px;
  border-radius: 2px;
  background-color: black;
  font-size: 12px;
}

.swal-button--confirm:hover {
  background-color: #3c9d9b !important;
}

.swal-button--cancel {
  padding: 7px 19px;
  border-radius: 2px;
  font-size: 12px;
}
</style>
