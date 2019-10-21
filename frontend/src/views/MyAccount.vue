<template>
  <div>
    <div class="container">
      <div class="row">
        <div class="col-lg-5 col-md-6 col-sm-4">
          <img src class="user-profile" />
          <p class="form-control border-0">Profile</p>
        </div>
        <div class="col-lg-2 col-md-2 col-sm-2 text-right">
          <label class="form-group form-control border-0">Email:</label>
          <label class="form-group form-control border-0">Name:</label>
          <label class="form-group form-control border-0">Phone:</label>
          <label class="form-group form-control border-0">Password:</label>
          <label class="form-group form-control border-0">Confirm:</label>
          <label class="form-group form-control border-0">Role:</label>
        </div>
        <div class="col-lg-5 col-md-4 col-sm-6">
          <div class="form-group">
            <input
              type="email"
              v-model.lazy="updatedUserData.email"
              class="form-control"
              :placeholder="userData.email"
              required
            />
          </div>
          <div class="form-group">
            <input
              v-model.lazy="updatedUserData.name"
              class="form-control"
              :placeholder="userData.name"
              required
            />
          </div>
          <div class="form-group">
            <input
              type="tel"
              v-model.lazy="updatedUserData.phone"
              class="form-control"
              :placeholder="userData.phone"
              required
            />
          </div>

          <div class="form-group">
            <input
              type="password"
              v-model.lazy="updatedUserData.password"
              class="form-control"
              placeholder="New Password"
              required
            />
          </div>
          <div class="form-group">
            <input
              type="password"
              v-model.lazy="updatedUserData.password2"
              class="form-control"
              placeholder="New Password Confirm"
              required
            />
          </div>
          <!-- choose role -->
          <div class="form-group mt-3">
            <div class="d-inline mx-1">
              <input
                type="radio"
                name="role"
                value="tenant"
                v-model="updatedUserData.role"
                class="mx-1"
              />
              <label>Tenant</label>
            </div>
            <div class="d-inline mx-1">
              <input
                type="radio"
                name="role"
                value="provider"
                v-model="updatedUserData.role"
                class="mx-1"
              />
              <label>Provider</label>
            </div>
          </div>
        </div>
      </div>
      <hr />
      <div class="button-area">
        <button class="btn btn-success form-control" @click="updateAccount">Update Account</button>
        <button class="btn btn-danger form-control my-1" @click="deleteAccount">Delete Account</button>
      </div>
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
      userData: {},
      updatedUserData: {}
    };
  },

  methods: {
    updateAccount() {
      // if one of the password input are not empty, check if they are matched
      if (this.updatedUserData.password || this.updatedUserData.password2) {
        if (this.updatedUserData.password !== this.updatedUserData.password2) {
          alert("Passwords not matched!");
          return;
        }
      }
      let usedUpdatedUserData = this.updatedUserData;
      // remove unused field
      delete usedUpdatedUserData["password2"];
      window.console.log(usedUpdatedUserData);
      this.$axios
        .patch(
          "/api/users/" + this.$store.getters.getUserId,
          usedUpdatedUserData
        )
        .then(response => {
          window.console.log(response);
          alert("User info is updated!");
        })
        .catch(error => window.console.log(error.response));
    },
    deleteAccount() {
      this.$axios
        .delete("/api/users/" + this.$store.getters.getUserId)
        .then(response => {
          window.console.log(response);
          alert("User account is deleted!");
          this.$store.commit("logout");
          this.$router.push({ name: "home" });
        })
        .catch(error => window.console.log(error.response));
    }
  },
  created() {
    this.$axios
      .get("/api/users/" + this.$store.getters.getUserId)
      .then(response => {
        this.userData = response.data;
        this.updatedUserData.role = this.userData.role;
      })
      .catch(error => {
        window.console.log(error);
      });
  }
};
</script>

<style scoped>
.container {
  padding-top: 2rem;
  min-height: 500px;
}

.user-profile {
  width: 200px;
  height: 200px;
  object-fit: cover;
}

.button-area {
  margin: auto;
  width: 300px;
}

@media screen and (max-width: 768px) {
  .user-profile {
    width: 150px;
    height: 150px;
    object-fit: cover;
  }
}
</style>