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

        <button @click="login" class="my-btn form-control my-4">Log in</button>

        <p class="hint-text">
          Don't have an account?
          <router-link class="mx-1 sign-up-link" to="/signup">Sign up</router-link>here!
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
      // raise alert if login form is not complete
      for (let key in this.loginData) {
        if (this.loginData[key] === "") {
          alert("The login form is not complete!");
          return;
        }
      }
      this.$axios
        .post("/api/users/login", this.loginData)
        .then(response => {
          // JSON responses are automatically parsed.
          if (response.status == 200) {
            let [userId, userRole] = response.data.split(" ");
            let authUserData = {
              userId: userId,
              userRole: userRole
            };
            this.$store.commit("login", authUserData);

            window.console.log("user logged in!");
            window.console.log("user id: " + userId);
            window.console.log("user role: " + userRole);
            alert("logged in!");
            this.$router.push({
              name: "search"
            });
          }
        })
        .catch(err => {
          window.console.log(err.response);
          alert(err.response.data);
        });
    }
  }
};
</script>

<style scoped>
.container {
  padding-top: 2rem;
  min-height: 500px;
  margin-top: 100px;
  margin-bottom: 80px;
}
.login-container {
  margin: auto;
  width: 300px;
}

.sign-up-link {
  color: #3c9d9b;
}

.my-btn {
  border: none;
  background-color: black;
  color: white;
}

.my-btn:hover {
  border: none;
  background-color: #3c9d9b;
  color: white;
}
</style>