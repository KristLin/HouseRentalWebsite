<template>
  <div>
    <div class="container">
      <p>My Account</p>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: "myAccount",
  components: {},

  data() {
    return {
      userData: ""
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