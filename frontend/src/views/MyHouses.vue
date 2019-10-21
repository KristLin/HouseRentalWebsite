<template>
  <div>
    <div class="container">
      <p>My Houses</p>
      <router-link class="nav-link" to="/uploadHouse" active-class="active" exact>Upload</router-link>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: "myHouses",
  components: {},

  data() {
    return {
      userHouses: []
    };
  },

  methods: {}
};
</script>

<style scoped>
.container {
  padding-top: 2rem;
  min-height: 500px;
}
</style>