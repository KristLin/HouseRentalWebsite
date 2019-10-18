<template>
  <div>
    <div class="container-fluid">
      <div class="container">
        <h2>Join us.</h2>
        <hr />
        <div class="row">
          <!-- for layout purpose -->
          <div class="col-md-2"></div>

          <!-- input user data -->
          <div class="col-md-4 user-info">
            <div class="form-group">
              <input
                type="email"
                v-model.lazy="userData.email"
                class="form-control input-lg"
                placeholder="Email Address"
                required
              />
            </div>
            <div class="form-group">
              <input
                v-model.lazy="userData.name"
                class="form-control input-lg"
                placeholder="Your Name"
                required
              />
            </div>
            <div class="form-group">
              <input
                type="tel"
                v-model.lazy="userData.phone"
                class="form-control input-lg"
                placeholder="Phone Number"
                required
              />
            </div>

            <div class="form-group">
              <input
                type="password"
                v-model.lazy="userData.password"
                class="form-control input-lg"
                placeholder="Password"
                required
              />
            </div>
            <div class="form-group">
              <input
                type="password"
                v-model.lazy="checkedData.password2"
                class="form-control input-lg"
                placeholder="Password Confirm"
                required
              />
            </div>
            <!-- choose role -->
            <div class="form-group">
              <div class="role-pick">
                <input
                  type="radio"
                  name="role"
                  value="tenant"
                  v-model.lazy="userData.role"
                  required
                />
                <label>Tenant</label>
              </div>
              <div class="role-pick">
                <input
                  type="radio"
                  name="role"
                  value="provider"
                  v-model.lazy="userData.role"
                  required
                />
                <label>Provider</label>
              </div>
            </div>
          </div>

          <!-- for layout purpose -->
          <div class="col-md-1"></div>

          <!-- show user info -->
          <div class="col-md-3 confirm-box">
            <h6>Please Confirm Your Information:</h6>
            <hr />
            <div class="confirm-info">
              <p>Email: {{ userData.email }}</p>
              <p>Name: {{ userData.name }}</p>
              <p>Phone: {{ userData.phone }}</p>
            </div>
            <hr />
          </div>
        </div>

        <!-- check policy & terms and submit button -->
        <div>
          <p>
            <input type="checkbox" v-model.lazy="checkedData.checkedPolicy" required />
            By clicking the checkbox you're agree to our policy & terms
          </p>
          <div class="register-button-div">
            <button @click="registerAccount" class="my-btn form-control my-4">Register</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "signup",
  components: {},
  data() {
    return {
      // user data that will be post to the backend server
      userData: {
        name: "",
        email: "",
        phone: "",
        password: "",
        role: ""
      },
      // used to check if the user is able to register
      checkedData: {
        password2: "",
        checkedPolicy: ""
      }
    };
  },
  methods: {
    registerAccount() {
      // raise alert if user info is not complete
      for (let key in this.userData) {
        if (this.userData[key] === "") {
          alert("The register form is not complete!");
          return;
        }
      }
      // raise alert if two password are not matched
      if (this.userData.password !== this.checkedData.password2) {
        alert("Passwords are not matched!");
      } else {
        this.$axios
          .post("/api/users/", this.userData)
          .then(response => {
            // JSON responses are automatically parsed.
            if (response.status == 200) {
              let [userId, userRole] = response.data.split(" ");
              let authUserData = {
                userId: userId,
                userRole: userRole
              };
              this.$store.commit("authUser", authUserData);

              window.console.log("user rigistered!");
              window.console.log("user id: " + userId);
              window.console.log("user role: " + userRole);
              alert("rigistered!");
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
  }
};
</script>

<style scoped>
.container {
  padding-top: 2rem;
  min-height: 500px;
}

.user-info {
  margin-top: 1rem;
  margin-bottom: auto;
}

.role-pick {
  display: inline;
  margin-right: 1rem;
  margin-left: auto;
}

.role-pick label {
  margin-left: 6px;
}

.confirm-box {
  margin-top: 3rem;
  margin-bottom: auto;
}
.confirm-info {
  text-align: left;
}

.register-button-div {
  margin: auto;
  width: 50%;
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