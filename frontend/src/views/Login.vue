<template>
  <div>
    <div class="text-center container">
      <div class="login-container">
        <!-- <img
            class="mb-4"
            src="/docs/4.3/assets/brand/bootstrap-solid.svg"
            alt
            width="72"
            height="72"
        />-->
        <h1 class="h3 mb-3 font-weight-normal">Please sign in</h1>
        <label for="inputEmail" class="sr-only">Email address</label>
        <input
          type="email"
          v-model="loginData.email"
          class="form-control"
          placeholder="Email address"
          required
          autofocus
        />
        <label for="inputPassword" class="sr-only">Password</label>
        <input
          type="password"
          v-model="loginData.password"
          class="form-control"
          placeholder="Password"
          required
        />
        <button @click="login" class="btn btn-lg btn-primary btn-block" type="submit">Sign in</button>

        <p class="hint-text">
          Don't have an account?
          <router-link to="/signup">Sign up</router-link>here!
        </p>
      </div>
    </div>
  </div>
</template>

<script>
// import axios from "axios";

export default {
  name: "login",
  components: {},
  data() {
    return {
      loginData: {
        email: "",
        password: ""
      },
      res: "",
      err: ""
    };
  },
  methods: {
    login() {
      this.$axios
        // .get("/api/houses")
        .post("/api/users/login", this.loginData)
        .then(res => {
          window.console.log(res);
          this.res = res;
        })
        .catch(err => {
          window.console.log(err.response);
          this.err = err;
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
.login-container {
  margin: auto;
  width: 300px;
}
.hint-text {
  margin-top: 10px;
}
</style>