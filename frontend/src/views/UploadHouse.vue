<template>
  <div class="container">
  </div>
</template>

<script>
export default {
  name: "login",
  components: {},
  data() {
    return {
      loginData: {
        email: "",
        password: ""
      }
    };
  },
  methods: {
    login() {
      this.$axios
        .post("/api/houses/random", this.loginData)
        .then(response => {
          // JSON responses are automatically parsed.
          if (response.status == 200) {
            window.console.log("logged in!");
          }
        })
        .catch(err => {
          window.console.log(err);
        });
    }
  }
};
</script>

<style scoped>
.container {
  padding-top: 2rem;
  min-height: 500px;
}
</style>